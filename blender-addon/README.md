# Miktos AI Bridge Connector - Blender Addon

## 🎯 Overview

The Miktos AI Bridge Connector is a Blender addon that provides seamless integration with the Miktos AI Bridge for real-time AI texture generation directly within Blender.

## ✨ Features

### 🎨 AI Texture Generation

- **Text-to-Texture**: Generate textures from descriptive prompts
- **Real-time Progress**: Live progress updates via WebSocket
- **Multiple Workflows**: Basic textures and complete PBR material sets
- **Automatic Application**: Generated textures applied directly to selected objects

### 🔧 Blender Integration

- **Native UI**: Integrated into Blender's Properties panel (Material tab)
- **Object Selection**: Works with selected mesh objects
- **Material System**: Creates proper Blender materials with node setups
- **Background Processing**: Non-blocking texture generation

### 🌐 Network Communication

- **AI Bridge Connection**: Connects to Miktos AI Bridge server
- **WebSocket Updates**: Real-time status and progress monitoring
- **Error Handling**: Robust connection and error management
- **Connection Status**: Visual indicators for connection state

## 🚀 Installation

### Method 1: Manual Installation

1. Download the addon folder or zip file
2. Open Blender → Edit → Preferences → Add-ons
3. Click "Install..." and select the addon file
4. Enable "Miktos AI Bridge Connector" in the addon list

### Method 2: Developer Installation

1. Copy the `blender-addon` folder to your Blender addons directory:
   - **macOS**: `~/Library/Application Support/Blender/3.x/scripts/addons/`
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\3.x\scripts\addons\`
   - **Linux**: `~/.config/blender/3.x/scripts/addons/`
2. Restart Blender
3. Enable the addon in Preferences → Add-ons

## 🔧 Configuration

### AI Bridge Connection Settings

1. Go to Edit → Preferences → Add-ons → Miktos AI Bridge Connector
2. Configure connection settings:
   - **AI Bridge URL**: `http://localhost:8000` (default)
   - **WebSocket URL**: `ws://localhost:8000/ws/status` (default)
   - **Auto Connect**: Enable automatic connection on startup

### Prerequisites

- **Miktos AI Bridge**: Must be running on the specified URL
- **Python Modules**: `requests`, `websocket-client` (usually included with Blender)

## 🎨 Usage

### Basic Workflow

1. **Start AI Bridge**: Ensure Miktos AI Bridge server is running
2. **Open Material Properties**: Go to Properties panel → Material tab
3. **Connect**: Click "Connect to AI Bridge" button
4. **Select Objects**: Select mesh objects to apply texture to
5. **Configure Texture**: Set prompt and generation parameters
6. **Generate**: Click "Generate AI Texture" button
7. **Monitor Progress**: Watch real-time progress updates
8. **Automatic Application**: Texture automatically applied when complete

### Interface Overview

#### Connection Panel

- **Status Indicator**: Shows connection state (✅ Connected / ❌ Not Connected)
- **Connect Button**: Establishes connection to AI Bridge
- **Generate Button**: Starts texture generation process

#### Texture Settings

- **Workflow Type**: Choose between Basic Texture or PBR Material
- **Texture Prompt**: Describe the desired texture
- **Negative Prompt**: Specify what to avoid
- **Dimensions**: Set texture width and height (256-2048px)
- **Generation Steps**: Control quality vs speed (5-50 steps)
- **CFG Scale**: How closely to follow prompt (1.0-20.0)
- **Auto Apply**: Automatically apply to selected objects

#### Progress Monitoring

- **Real-time Status**: Shows current generation status
- **Progress Bar**: Visual progress indicator during generation
- **Object Count**: Shows how many objects will receive the texture

## 🔄 Workflow Types

### Basic Texture Generation

- **Description**: Generates a single texture image
- **Output**: Diffuse texture applied to Base Color
- **Best For**: Simple materials, prototyping, concept work

### PBR Material Generation

- **Description**: Generates complete PBR material set
- **Output**: Diffuse, Normal, Roughness, Metallic maps
- **Best For**: Realistic materials, production work, final renders

## 🛠️ Technical Details

### Architecture

```text
🔺 Blender Addon
├── 🎛️ UI Panel (Material Properties)
├── 🔗 AI Bridge Connection (HTTP + WebSocket)
├── 🎨 Material Creation System
├── 📊 Progress Monitoring
└── 🔄 Background Processing
```text

### API Integration

- **REST API**: Workflow execution and task management
- **WebSocket**: Real-time progress updates and status
- **Error Handling**: Connection timeouts and retry logic
- **Threading**: Non-blocking UI during generation

### Material System

- **Node Creation**: Automatic Principled BSDF setup
- **Texture Loading**: Loads generated textures into materials
- **Multi-object**: Applies to all selected mesh objects
- **Material Naming**: Automatic naming with timestamps

## 🧪 Testing

### Connection Test

1. Start Miktos AI Bridge server
2. Open Blender with addon installed
3. Go to Material Properties → Miktos AI panel
4. Click "Connect to AI Bridge"
5. Verify "✅ Connected" status appears

### Generation Test

1. Create a cube or select existing mesh
2. Set simple prompt: "red brick wall"
3. Click "Generate AI Texture"
4. Monitor progress updates
5. Verify material applied to object

### WebSocket Test

1. Monitor console output for WebSocket messages
2. Verify real-time progress updates in UI
3. Check connection persistence during generation

## 🔧 Troubleshooting

### Common Issues

#### Connection Failed

- **Cause**: AI Bridge server not running
- **Solution**: Start AI Bridge with `python3 main.py`
- **Check**: Verify server running at <http://localhost:8000/health>

#### WebSocket Errors

- **Cause**: Network connectivity issues
- **Solution**: Check firewall settings, try reconnecting
- **Check**: Verify WebSocket endpoint accessible

#### Generation Fails

- **Cause**: Invalid parameters or server error
- **Solution**: Check prompt length, verify parameters
- **Check**: Monitor AI Bridge server logs

#### Texture Not Applied

- **Cause**: No objects selected or material issues
- **Solution**: Select mesh objects before generation
- **Check**: Verify objects have material slots

### Debug Information

- **Console Output**: Monitor Blender console for debug messages
- **Server Logs**: Check AI Bridge server logs for errors
- **Network Tab**: Use browser dev tools to inspect API calls

## 🔮 Future Enhancements

### Planned Features

- **Texture Preview**: Preview before applying to objects
- **Batch Generation**: Generate multiple variations
- **Material Library**: Save and reuse generated materials
- **Custom Workflows**: User-defined generation workflows

### Advanced Integration

- **Render Engine Optimization**: Cycles and Eevee specific features
- **Animation Support**: Animated texture generation
- **Geometry Nodes**: Integration with geometry node workflows
- **Asset Browser**: Integration with Blender's asset system

## 📋 Requirements

### Blender Version

- **Minimum**: Blender 3.0+
- **Recommended**: Blender 3.6+ for best compatibility
- **Tested**: Blender 3.6, 4.0, 4.1

### System Requirements

- **OS**: macOS, Windows, Linux
- **Python**: 3.9+ (included with Blender)
- **Network**: Internet connection for AI Bridge communication
- **Memory**: 4GB+ RAM recommended for texture generation

### Dependencies

- **Miktos AI Bridge**: Must be running and accessible
- **Python Modules**: `requests`, `websocket-client` (auto-installed)

## 🤝 Contributing

### Development Setup

1. Clone the Miktos repository
2. Set up development environment
3. Link addon to Blender addons directory
4. Enable developer mode in Blender

### Testing Guidelines

- Test with different Blender versions
- Verify connection handling edge cases
- Test material application on various object types
- Validate WebSocket communication

## 📄 License

This addon is part of the Miktos Platform and follows the same licensing terms.

## 🆘 Support

- **Documentation**: Full API documentation at AI Bridge server `/docs`
- **Issues**: Report bugs on GitHub issue tracker
- **Community**: Join Miktos community discussions
- **Examples**: Sample workflows and materials provided

---

**🎉 Start creating AI-powered textures directly in Blender with the Miktos AI Bridge Connector!**
