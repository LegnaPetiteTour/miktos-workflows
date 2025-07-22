#!/usr/bin/env python3
"""
Miktos Agent Connector - Blender Addon
Professional 3D content creation through natural language

This addon connects Blender to the Miktos Agent for intelligent
3D content creation through conversational commands.
"""

bl_info = {
    "name": "Miktos Agent Connector",
    "author": "Miktos Platform",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "Properties > Material > Miktos Agent",
    "description": "Create professional 3D content through natural language commands",
    "category": "Material",
    "doc_url": "https://github.com/Miktos-Universe/miktos-workflows",
    "tracker_url": "https://github.com/Miktos-Universe/miktos-workflows/issues",
}

import bpy
import bmesh
import json
import asyncio
import threading
import time
import requests
from bpy.props import StringProperty, IntProperty, FloatProperty, BoolProperty, EnumProperty
from bpy.types import Panel, Operator, PropertyGroup, AddonPreferences
import websocket

# Global variables for connection state
miktos_agent_connected = False
current_task_id = None
generation_progress = 0.0
generation_status = "idle"

class MiktosAddonPreferences(AddonPreferences):
    """Addon preferences for Miktos Agent connection settings"""
    bl_idname = __name__

    miktos_agent_url = StringProperty(
        name="Miktos Agent URL",
        description="URL of the Miktos Agent server",
        default="http://localhost:8000",
    )
    
    websocket_url = StringProperty(
        name="WebSocket URL", 
        description="WebSocket URL for real-time updates",
        default="ws://localhost:8000/ws/blender",
    )
    
    auto_connect = BoolProperty(
        name="Auto Connect",
        description="Automatically connect to Miktos Agent on startup",
        default=True,
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "miktos_agent_url")
        layout.prop(self, "websocket_url")
        layout.prop(self, "auto_connect")


class MiktosTextureProperties(PropertyGroup):
    """Properties for AI texture generation"""
    
    prompt = StringProperty(
        name="Texture Prompt",
        description="Describe the texture you want to generate",
        default="rusty metal surface with scratches and weathering",
        maxlen=500,
    )
    
    negative_prompt = StringProperty(
        name="Negative Prompt",
        description="What to avoid in the texture",
        default="blurry, low quality, distorted",
        maxlen=500,
    )
    
    width = IntProperty(
        name="Width",
        description="Texture width in pixels",
        default=512,
        min=256,
        max=2048,
        step=256,
    )
    
    height = IntProperty(
        name="Height", 
        description="Texture height in pixels",
        default=512,
        min=256,
        max=2048,
        step=256,
    )
    
    steps = IntProperty(
        name="Generation Steps",
        description="Number of AI generation steps (more = better quality)",
        default=15,
        min=5,
        max=50,
    )
    
    cfg = FloatProperty(
        name="CFG Scale",
        description="How closely to follow the prompt (7.0 recommended)",
        default=7.0,
        min=1.0,
        max=20.0,
        step=0.5,
    )
    
    workflow_type = EnumProperty(
        name="Workflow Type",
        description="Type of texture generation workflow",
        items=[
            ("basic_texture", "Basic Texture", "Generate a single texture"),
            ("pbr_texture", "PBR Material", "Generate complete PBR material set"),
        ],
        default="basic_texture",
    )
    
    auto_apply = BoolProperty(
        name="Auto Apply",
        description="Automatically apply generated texture to selected objects",
        default=True,
    )


class MIKTOS_OT_connect_bridge(Operator):
    """Connect to Miktos AI Bridge"""
    bl_idname = "miktos.connect_bridge"
    bl_label = "Connect to AI Bridge"
    bl_description = "Connect to the Miktos AI Bridge server"
    
    def execute(self, context):
        global ai_bridge_connected
        
        prefs = context.preferences.addons[__name__].preferences
        
        try:
            # Test connection to AI Bridge
            response = requests.get(f"{prefs.ai_bridge_url}/health", timeout=5)
            
            if response.status_code == 200:
                ai_bridge_connected = True
                self.report({'INFO'}, "Successfully connected to Miktos AI Bridge!")
                
                # Start WebSocket connection for real-time updates
                self.start_websocket_connection(prefs.websocket_url)
                
            else:
                ai_bridge_connected = False
                self.report({'ERROR'}, f"Failed to connect: HTTP {response.status_code}")
                
        except Exception as e:
            ai_bridge_connected = False
            self.report({'ERROR'}, f"Connection failed: {str(e)}")
            
        return {'FINISHED'}
    
    def start_websocket_connection(self, websocket_url):
        """Start WebSocket connection in background thread"""
        def websocket_thread():
            try:
                ws = websocket.WebSocketApp(websocket_url,
                    on_message=self.on_websocket_message,
                    on_error=self.on_websocket_error,
                    on_close=self.on_websocket_close)
                ws.run_forever()
            except Exception as e:
                print(f"WebSocket error: {e}")
        
        thread = threading.Thread(target=websocket_thread, daemon=True)
        thread.start()
    
    def on_websocket_message(self, ws, message):
        """Handle WebSocket status messages"""
        global generation_progress, generation_status, current_task_id
        
        try:
            data = json.loads(message)
            
            # Update progress for current task
            if current_task_id and "task_updates" in data:
                for task in data["task_updates"]:
                    if task.get("task_id") == current_task_id:
                        generation_progress = task.get("progress", 0.0)
                        generation_status = task.get("status", "unknown")
                        
                        # Redraw UI to show progress
                        for area in bpy.context.screen.areas:
                            if area.type == 'PROPERTIES':
                                area.tag_redraw()
                                
        except Exception as e:
            print(f"WebSocket message error: {e}")
    
    def on_websocket_error(self, ws, error):
        print(f"WebSocket error: {error}")
    
    def on_websocket_close(self, ws, close_status_code, close_msg):
        print("WebSocket connection closed")


class MIKTOS_OT_generate_texture(Operator):
    """Generate AI texture using Miktos AI Bridge"""
    bl_idname = "miktos.generate_texture"
    bl_label = "Generate AI Texture"
    bl_description = "Generate an AI texture based on the prompt"
    
    def execute(self, context):
        global ai_bridge_connected, current_task_id, generation_status
        
        if not ai_bridge_connected:
            self.report({'ERROR'}, "Not connected to AI Bridge. Click 'Connect' first.")
            return {'CANCELLED'}
        
        # Get properties
        props = context.scene.miktos_texture_props
        prefs = context.preferences.addons[__name__].preferences
        
        # Prepare workflow data
        workflow_data = {
            "workflow_type": "Basic Texture Generation" if props.workflow_type == "basic_texture" else "PBR Texture Set Generation",
            "parameters": {
                "prompt": props.prompt,
                "negative_prompt": props.negative_prompt,
                "width": props.width,
                "height": props.height,
                "steps": props.steps,
                "cfg": props.cfg,
            },
            "blender_info": {
                "blender_version": f"{bpy.app.version[0]}.{bpy.app.version[1]}",
                "render_engine": context.scene.render.engine,
                "selected_objects": len([obj for obj in context.selected_objects if obj.type == 'MESH'])
            }
        }
        
        try:
            # Execute workflow via Blender-specific endpoint
            response = requests.post(
                f"{prefs.ai_bridge_url}/api/v1/blender/generate-material",
                json=workflow_data,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                current_task_id = result.get("task_id")
                generation_status = "started"
                
                self.report({'INFO'}, f"Texture generation started! Task ID: {current_task_id}")
                
                # Start monitoring progress
                self.monitor_progress(context, prefs.ai_bridge_url, current_task_id)
                
            else:
                self.report({'ERROR'}, f"Failed to start generation: {response.text}")
                
        except Exception as e:
            self.report({'ERROR'}, f"Generation failed: {str(e)}")
            
        return {'FINISHED'}
    
    def monitor_progress(self, context, ai_bridge_url, task_id):
        """Monitor generation progress and apply texture when complete"""
        def progress_thread():
            global generation_status, generation_progress
            
            while generation_status not in ["completed", "error"]:
                try:
                    response = requests.get(f"{ai_bridge_url}/api/v1/task/{task_id}")
                    if response.status_code == 200:
                        task_data = response.json()
                        generation_status = task_data.get("status", "unknown")
                        generation_progress = task_data.get("progress", 0.0)
                        
                        if generation_status == "completed":
                            # Apply texture to selected objects
                            if context.scene.miktos_texture_props.auto_apply:
                                bpy.app.timers.register(
                                    lambda: self.apply_generated_texture(context, task_data)
                                )
                            break
                            
                    time.sleep(1)
                    
                except Exception as e:
                    print(f"Progress monitoring error: {e}")
                    break
        
        thread = threading.Thread(target=progress_thread, daemon=True)
        thread.start()
    
    def apply_generated_texture(self, context, task_data):
        """Apply the generated texture to selected objects"""
        try:
            # For now, create a simple material with the texture info
            # In a real implementation, this would download and apply the actual texture file
            
            selected_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
            
            if not selected_objects:
                return None
            
            # Create new material
            material_name = f"Miktos_AI_{int(time.time())}"
            material = bpy.data.materials.new(name=material_name)
            material.use_nodes = True
            
            # Get the principled BSDF node
            nodes = material.node_tree.nodes
            principled = nodes.get("Principled BSDF")
            
            if principled:
                # Add a note about the generated texture
                principled.inputs["Base Color"].default_value = (0.8, 0.6, 0.4, 1.0)  # Placeholder color
                
            # Apply material to selected objects
            for obj in selected_objects:
                if obj.data.materials:
                    obj.data.materials[0] = material
                else:
                    obj.data.materials.append(material)
            
            print(f"Applied AI-generated material '{material_name}' to {len(selected_objects)} objects")
            
        except Exception as e:
            print(f"Failed to apply texture: {e}")
        
        return None


class MIKTOS_PT_texture_panel(Panel):
    """Main panel for Miktos AI texture generation"""
    bl_label = "Miktos AI Textures"
    bl_idname = "MIKTOS_PT_texture_panel"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "material"
    
    def draw(self, context):
        layout = self.layout
        props = context.scene.miktos_texture_props
        
        # Connection status
        row = layout.row()
        if ai_bridge_connected:
            row.label(text="✅ Connected to AI Bridge", icon='LINKED')
        else:
            row.label(text="❌ Not Connected", icon='UNLINKED')
            
        # Connection button
        if ai_bridge_connected:
            layout.operator("miktos.generate_texture", icon='TEXTURE')
        else:
            layout.operator("miktos.connect_bridge", icon='PLUGIN')
        
        # Progress display
        if generation_status != "idle":
            layout.separator()
            
            # Status with icon
            status_icons = {
                "started": "PLAY",
                "executing": "RENDER_ANIMATION", 
                "completed": "CHECKMARK",
                "error": "ERROR"
            }
            icon = status_icons.get(generation_status, "INFO")
            
            layout.label(text=f"Status: {generation_status.title()}", icon=icon)
            
            if generation_status == "executing":
                # Progress bar
                progress_row = layout.row()
                progress_row.scale_y = 0.8
                progress_row.prop(context.scene, "frame_current", 
                                text=f"Progress: {generation_progress:.1f}%", 
                                slider=True, emboss=False)
                
            elif generation_status == "completed":
                layout.label(text="✅ Texture ready! Check your materials.", icon='MATERIAL')
        
        # Texture generation settings
        layout.separator()
        layout.label(text="Texture Settings:", icon='SETTINGS')
        
        layout.prop(props, "workflow_type")
        layout.prop(props, "prompt")
        layout.prop(props, "negative_prompt")
        
        # Advanced settings in a box
        box = layout.box()
        box.label(text="Advanced Settings:")
        
        row = box.row()
        row.prop(props, "width")
        row.prop(props, "height")
        
        row = box.row()
        row.prop(props, "steps")
        row.prop(props, "cfg")
        
        box.prop(props, "auto_apply")
        
        # Selected objects info
        layout.separator()
        selected_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
        if selected_objects:
            layout.label(text=f"Will apply to {len(selected_objects)} selected objects", icon='OBJECT_DATA')
        else:
            layout.label(text="Select mesh objects to apply texture", icon='INFO')


# Registration
classes = [
    MiktosAddonPreferences,
    MiktosTextureProperties,
    MIKTOS_OT_connect_bridge,
    MIKTOS_OT_generate_texture, 
    MIKTOS_PT_texture_panel,
]

def register():
    """Register addon classes and properties"""
    for cls in classes:
        bpy.utils.register_class(cls)
    
    # Add properties to scene
    bpy.types.Scene.miktos_texture_props = bpy.props.PointerProperty(type=MiktosTextureProperties)
    
    print("Miktos AI Bridge Connector registered successfully!")

def unregister():
    """Unregister addon classes and properties"""
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    # Remove properties from scene
    del bpy.types.Scene.miktos_texture_props
    
    print("Miktos AI Bridge Connector unregistered successfully!")

if __name__ == "__main__":
    register()
