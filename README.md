# Miktos Workflows - Blender 3D Skills

> Pre-built Blender workflow expertise and 3D content creation skills for the Miktos Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Blender](https://img.shields.io/badge/Blender-F5792A?logo=blender&logoColor=white)](https://blender.org)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://python.org)

This repository contains a curated collection of Blender workflow skills, 3D content creation expertise, and automated Blender Python scripts designed for the Miktos Agent. These workflows enable professional 3D content creation through natural language commands.

## ✨ Features

- **Expert Blender Skills**: Pre-built expertise for complex 3D content creation
- **Natural Language Interface**: Execute professional workflows through simple commands
- **Modular Design**: Mix and match workflow components for custom 3D pipelines
- **Professional Quality**: Optimized for production-level Blender output
- **Well Documented**: Clear instructions and parameter explanations
- **Version Controlled**: Track changes and improvements to 3D workflows

## 🚀 Quick Start

### Prerequisites

- **Miktos Desktop App** (hosts the Miktos Agent)
- **Blender** 3.0+ (automatically connected via Miktos Agent)
- **Python** 3.11+ (for local AI texture generation)

### Installation

```bash
# Clone the repository
git clone https://github.com/Miktos-Universe/miktos-workflows.git
cd miktos-workflows

# The workflows are automatically detected by Miktos Agent
# No additional installation required
```

### Using Workflows

1. **Via Miktos Desktop**: Natural language commands like "Create steampunk robot"
2. **Via Agent API**: Use the Miktos Agent REST API to execute Blender workflows
3. **Direct Blender**: Import Python scripts directly into Blender

## 📁 Workflow Categories

### 🎨 Image Generation

#### Basic Text-to-Image

- Simple text prompt to image generation
- Configurable resolution and quality settings
- Support for multiple art styles

#### Advanced Text-to-Image

- Multi-prompt composition
- Style transfer capabilities
- Advanced sampling methods
- ControlNet integration

#### Image-to-Image

- Style transfer and artistic effects
- Image enhancement and upscaling
- Color correction and artistic filters

### 🎬 Animation & Video

#### Basic Animation

- Simple animated sequences
- Interpolation between keyframes
- Basic motion effects

#### Advanced Animation

- Complex character animation
- Camera movement and effects
- Multi-layer composition

### 🖼️ Image Enhancement

#### Upscaling & Enhancement

- AI-powered image upscaling
- Detail enhancement and sharpening
- Noise reduction and cleanup

#### Style & Effects

- Artistic style application
- Color grading and tone mapping
- Special visual effects

### 🔧 Utility Workflows

#### Preprocessing

- Image preparation and formatting
- Batch processing utilities
- Format conversion tools

#### Postprocessing

- Output formatting and optimization
- Metadata management
- Quality control and validation

## 📋 Available Workflows

### Image Generation

| Workflow | Description | Difficulty | Models Required |
|----------|-------------|------------|-----------------|
| `basic_txt2img.json` | Simple text-to-image generation | Beginner | SD 1.5 or SDXL |
| `advanced_txt2img.json` | Advanced text-to-image with ControlNet | Intermediate | SD 1.5, ControlNet |
| `style_transfer.json` | Apply artistic styles to images | Intermediate | SD 1.5, Style models |
| `img2img_enhance.json` | Enhance and stylize existing images | Beginner | SD 1.5 |

### Animation

| Workflow | Description | Difficulty | Models Required |
|----------|-------------|------------|-----------------|
| `basic_animation.json` | Simple 2D animation sequences | Intermediate | SD 1.5, AnimateDiff |
| `character_animation.json` | Character-focused animation | Advanced | SD 1.5, ControlNet, AnimateDiff |

### Enhancement

| Workflow | Description | Difficulty | Models Required |
|----------|-------------|------------|-----------------|
| `upscale_4x.json` | 4x image upscaling | Beginner | RealESRGAN |
| `face_enhance.json` | Facial feature enhancement | Intermediate | GFPGAN, CodeFormer |

## 🛠️ Model Requirements

### Core Models

#### Stable Diffusion Models (Choose one or more)

- **SD 1.5**: `runwayml/stable-diffusion-v1-5`
- **SDXL**: `stabilityai/stable-diffusion-xl-base-1.0`
- **SDXL Turbo**: `stabilityai/sdxl-turbo`

#### ControlNet Models (Optional but recommended)

- **Canny**: `lllyasviel/sd-controlnet-canny`
- **Depth**: `lllyasviel/sd-controlnet-depth`
- **OpenPose**: `lllyasviel/sd-controlnet-openpose`

### Enhancement Models

#### Upscaling Models

- **RealESRGAN**: `Real-ESRGAN 4x+`
- **ESRGAN**: `ESRGAN 4x`

#### Face Enhancement

- **GFPGAN**: `GFPGANv1.4`
- **CodeFormer**: `CodeFormer`

### Animation Models

#### Animation-Specific

- **AnimateDiff**: `guoyww/animatediff`
- **SadTalker**: `SadTalker models`

### Installation Guide

Models are automatically downloaded by the Miktos AI Bridge when needed. For manual installation:

1. **Automatic Download** (Recommended)

   ```text
   Models are automatically downloaded when first used
   Storage location: ./models/ (configurable)
   ```

2. **Manual Download**

   ```bash
   # Download using huggingface-hub
   huggingface-cli download runwayml/stable-diffusion-v1-5 --local-dir ./models/sd15
   
   # Or use git-lfs
   git lfs clone https://huggingface.co/runwayml/stable-diffusion-v1-5 ./models/sd15
   ```

## 🎯 Usage Examples

### Via Miktos Desktop

1. Open Miktos Desktop application
2. Navigate to the Workflow Library
3. Browse available categories
4. Select a workflow template
5. Customize parameters as needed
6. Click "Generate" to execute

### Via API

```bash
# Execute a workflow via REST API
curl -X POST "http://localhost:8000/api/v1/workflows/basic_txt2img/execute" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A beautiful sunset over mountains",
    "steps": 30,
    "cfg_scale": 7.5,
    "width": 512,
    "height": 512
  }'
```

### Direct ComfyUI Import

1. Open ComfyUI web interface
2. Click "Load" button
3. Select workflow JSON file
4. Customize nodes as needed
5. Click "Queue Prompt" to execute

## 🔧 Customization

### Modifying Workflows

Workflows are stored as JSON files that can be edited:

```json
{
  "workflow_name": "Custom Text-to-Image",
  "description": "My custom workflow",
  "nodes": {
    "1": {
      "class_type": "CLIPTextEncode",
      "inputs": {
        "text": "{{prompt}}",
        "clip": ["4", 0]
      }
    }
  },
  "parameters": {
    "prompt": {
      "type": "string",
      "default": "A beautiful landscape",
      "description": "Text prompt for generation"
    }
  }
}
```

### Creating New Workflows

1. **Design in ComfyUI**: Create your workflow in ComfyUI interface
2. **Export**: Use "Save (API Format)" to export as JSON
3. **Add Metadata**: Include workflow metadata and parameter definitions
4. **Test**: Validate the workflow works correctly
5. **Document**: Add clear documentation and examples
6. **Submit**: Create a pull request to add to the collection

### Parameter Customization

Most workflows support customizable parameters:

```text
Common Parameters:
- prompt: Text description of desired output
- negative_prompt: What to avoid in the output
- steps: Number of denoising steps (20-50 recommended)
- cfg_scale: Prompt adherence strength (7-15 recommended)
- width/height: Output dimensions
- seed: Random seed for reproducibility
```

## 🧪 Testing Workflows

### Validation Script

```bash
# Validate all workflows
python scripts/validate_workflows.py

# Test specific workflow
python scripts/test_workflow.py workflows/image_generation/basic_txt2img.json
```

### Quality Assurance

Each workflow includes:

- **Parameter validation**: Ensures valid input ranges
- **Model compatibility**: Checks required models are available
- **Output verification**: Validates expected output format
- **Performance benchmarks**: Execution time and resource usage

## 🤝 Contributing

We welcome contributions of new workflows and improvements!

### Contribution Guidelines

1. **Follow the Template**: Use our workflow template structure
2. **Test Thoroughly**: Ensure workflows work with default parameters
3. **Document Clearly**: Include comprehensive documentation
4. **Optimize Performance**: Consider resource usage and execution time
5. **Version Compatibility**: Ensure compatibility with current ComfyUI version

### Workflow Submission Process

1. Fork the repository
2. Create a new branch: `git checkout -b feature/my-new-workflow`
3. Add your workflow files:
   - JSON workflow file
   - Documentation (README.md)
   - Example outputs (if applicable)
   - Test scripts
4. Test the workflow thoroughly
5. Submit a pull request with:
   - Clear description of the workflow
   - Use cases and benefits
   - Required models and dependencies
   - Example outputs

### Workflow Standards

- **Naming**: Use descriptive, lowercase names with underscores
- **Structure**: Follow the standard workflow JSON format
- **Documentation**: Include inline comments and external documentation
- **Parameters**: Define clear, validated parameters
- **Compatibility**: Test with multiple model versions

## 📊 Workflow Metrics

### Performance Guidelines

- **Execution Time**: Target under 30 seconds for basic workflows
- **Memory Usage**: Keep peak memory under 8GB for standard workflows
- **Model Size**: Document required model sizes and storage needs
- **Compatibility**: Test with both SD 1.5 and SDXL models when applicable

### Quality Standards

- **Output Quality**: Consistent, high-quality results
- **Parameter Sensitivity**: Robust across parameter ranges
- **Error Handling**: Graceful failure with helpful error messages
- **Documentation**: Complete usage instructions and examples

## 🐛 Troubleshooting

### Common Issues

#### Workflow Won't Load

- Check JSON syntax validity
- Verify all required models are installed
- Ensure ComfyUI custom nodes are available

#### Poor Quality Output

- Adjust prompt and negative prompt
- Increase step count (try 30-50 steps)
- Modify CFG scale (try 7-12 range)
- Check model compatibility

#### Memory Errors

- Reduce image dimensions
- Use lower precision models
- Close other applications
- Consider batch size reduction

#### Slow Execution

- Enable GPU acceleration
- Optimize workflow node order
- Use faster sampling methods
- Consider model quantization

### Getting Help

- **GitHub Issues**: Report bugs and request features
- **Discussions**: Ask questions and share ideas
- **Documentation**: Check our comprehensive docs
- **Community**: Join our Discord server

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- **[Miktos Desktop](https://github.com/Miktos-Universe/miktos-desktop)**: Cross-platform desktop application
- **[Miktos AI Bridge](https://github.com/Miktos-Universe/miktos-ai-bridge)**: Python FastAPI backend for AI operations
- **[Miktos Docs](https://github.com/Miktos-Universe/miktos-docs)**: Comprehensive documentation

## 🙏 Acknowledgments

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) for the amazing workflow system
- [Stability AI](https://stability.ai) for Stable Diffusion models
- The AI art community for inspiration and feedback
- All contributors who share their workflows

---

Built with ❤️ by the Miktos team

[Organization](https://github.com/Miktos-Universe) • [Website](https://miktos.com) • [Twitter](https://twitter.com/MiktosAI)
