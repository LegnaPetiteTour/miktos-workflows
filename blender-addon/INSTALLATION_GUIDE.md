# 🎨 Miktos Blender Addon - Installation & Usage Guide

## 📋 Prerequisites

- **Blender 3.0+** (tested with 3.6, 4.0+)

- **Miktos AI Bridge** running on `localhost:8000`

- **Python requests and websocket-client** (usually included with Blender)

## 🚀 Installation Steps

### 1. Install the Addon

### Option A: Manual Installation

```bash
# Copy the addon file to Blender's addons directory
cp __init__.py ~/.config/blender/[VERSION]/scripts/addons/miktos_ai_bridge.py

# On macOS:
cp __init__.py ~/Library/Application\ Support/Blender/[VERSION]/scripts/addons/miktos_ai_bridge.py

# On Windows:
copy __init__.py %APPDATA%\Blender Foundation\Blender\[VERSION]\scripts\addons\miktos_ai_bridge.py

```bash

### Option B: Install via Blender UI

1. Open Blender

2. Go to **Edit → Preferences → Add-ons**

3. Click **Install...** button

4. Select the `__init__.py` file

5. Enable "Miktos AI Bridge Connector"

### 2. Configure the Addon

1. In Blender Preferences → Add-ons → Miktos AI Bridge Connector

2. Set **AI Bridge URL**: `http://localhost:8000` (default)

3. Set **WebSocket URL**: `ws://localhost:8000/ws/blender`

4. Enable **Auto Connect** if desired

### 3. Start AI Bridge Server

```bash
cd /path/to/miktos-ai-bridge
python3 main.py

```bash

Wait for the server to show:

```bash
🚀 Starting Miktos AI Bridge...
Server will be available at: http://localhost:8000

```bash

## 🎯 Usage Instructions

### 1. Access the Panel

1. Select a mesh object in Blender

2. Go to **Properties Panel → Material Properties**

3. Find the **"Miktos AI Textures"** section

### 2. Connect to AI Bridge

1. Click **"Connect to AI Bridge"** button

2. Wait for ✅ **"Connected to AI Bridge"** confirmation

### 3. Generate AI Textures

1. **Choose Workflow Type**:
   - `Basic Texture`: Single texture generation
   - `PBR Material`: Complete PBR material set

2. **Enter Texture Prompt**:

   ```text
   weathered wooden planks with moss and dirt
   rusty metal surface with scratches
   smooth marble with subtle veining
   fabric texture with natural fibers
   ```

1. **Adjust Settings**:
   - **Resolution**: 512x512 (recommended), up to 2048x2048
   - **Steps**: 15-30 (higher = better quality, slower)
   - **CFG Scale**: 7.0 (how closely to follow prompt)

2. **Click "Generate AI Texture"**

### 4. Monitor Progress

- Watch the **real-time progress bar**

- Status updates: `Started → Executing → Completed`

- Typical generation time: **15-30 seconds**

### 5. Apply Generated Texture

- **Auto Apply** (default): Texture automatically applied to selected objects

- **Manual Apply**: Material created, manually assign to objects

## 🎨 Example Workflows

### Basic Texture Generation

```bash
Prompt: "old brick wall with weathering and moss"
Negative: "blurry, low quality, repetitive"
Steps: 20
CFG: 7.0
Resolution: 512x512

```bash

### PBR Material Set

```bash
Prompt: "polished copper surface with oxidation patterns"
Negative: "plastic, fake, unrealistic"
Steps: 25
CFG: 8.0
Resolution: 1024x1024

```bash

## 🔧 Advanced Features

### Real-Time WebSocket Updates

- Live progress monitoring

- Background processing

- Connection status indicators

### Blender Integration

- Automatic material creation

- Principled BSDF node setup

- Multi-object application

- Render engine detection

### AI Bridge Optimization

- Blender-specific workflows

- Optimized parameter handling

- Background task processing

## 🐛 Troubleshooting

### Connection Issues

**"Not Connected" Error**:

1. Ensure AI Bridge is running on `localhost:8000`

2. Check firewall settings

3. Verify URL in addon preferences

**WebSocket Connection Failed**:

1. Check WebSocket URL: `ws://localhost:8000/ws/blender`

2. Restart both Blender and AI Bridge

3. Check console for error messages

### Generation Issues

**"Generation Failed" Error**:

1. Check prompt length (max 500 characters)

2. Ensure valid parameters (steps 5-50, CFG 1-20)

3. Verify AI Bridge has workflows loaded

**Slow Generation**:

1. Reduce image resolution

2. Lower step count (15-20)

3. Check system resources

### Material Issues

**Texture Not Applied**:

1. Ensure objects are selected

2. Check "Auto Apply" is enabled

3. Manually assign material from Material Properties

## 📊 Performance Tips

### Optimal Settings

- **Resolution**: 512x512 for previews, 1024x1024 for final

- **Steps**: 15-20 for speed, 25-30 for quality

- **CFG**: 7.0-8.0 for most prompts

### System Optimization

- Close unnecessary applications

- Use SSD storage for faster I/O

- Ensure adequate RAM (8GB+ recommended)

## 🔗 Integration Testing

To verify your installation works:

```bash
cd miktos-workflows/blender-addon
python3 test_integration.py

```bash

Expected output:

```bash
✅ AI Bridge connection: Working
✅ Blender endpoints: Available
✅ Material generation: Functional
✅ WebSocket communication: Active

```bash

## 🆘 Support

### Log Files

- **Blender Console**: Check for addon errors

- **AI Bridge Logs**: Monitor server-side issues

- **System Console**: Terminal output for debugging

### Common Solutions

1. **Restart Blender** after addon installation

2. **Restart AI Bridge** if connection issues persist

3. **Check Python dependencies** in Blender's Python environment

4. **Verify file permissions** for addon installation

### Getting Help

- Check GitHub issues for known problems

- Review the integration test output

- Enable debug logging in AI Bridge

- Report issues with system information

---

**🎉 Enjoy creating AI-powered textures directly in Blender!**

*This addon represents the world's first real-time AI texture generation integration for Blender, enabling unprecedented creative workflows for 3D artists and developers.*
