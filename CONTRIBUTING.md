# Contributing to Miktos Workflows

We love your input! We want to make contributing to Miktos Workflows as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of workflows
- Submitting a fix
- Proposing new workflow templates
- Becoming a maintainer

## We Develop with GitHub

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## We Use [GitHub Flow](https://guides.github.com/introduction/flow/index.html)

Pull requests are the best way to propose changes to the codebase:

1. Fork the repo and create your branch from `main`.
2. If you've added workflow templates, ensure they're well-documented.
3. If you've changed APIs, update the documentation.
4. Ensure your workflow templates are valid JSON.
5. Make sure your code lints.
6. Issue that pull request!

## Workflow Contribution Guidelines

### Workflow Templates

When contributing workflow templates:

1. **Structure**: Follow the established directory structure
2. **Documentation**: Include clear descriptions and usage examples
3. **Testing**: Test workflows with ComfyUI before submitting
4. **Metadata**: Include proper metadata and tags

### Directory Structure

```text
workflows/
├── image-generation/
│   ├── basic/
│   ├── advanced/
│   └── experimental/
├── image-processing/
├── video/
└── audio/
```

### Workflow Template Format

Each workflow should include:

- `workflow.json` - The ComfyUI workflow
- `README.md` - Documentation and usage instructions
- `examples/` - Example inputs/outputs (if applicable)
- `metadata.json` - Workflow metadata

Example metadata.json:

```json
{
  "name": "Basic Image Generation",
  "description": "Simple text-to-image generation workflow",
  "category": "image-generation",
  "difficulty": "beginner",
  "tags": ["text-to-image", "basic", "stable-diffusion"],
  "requirements": {
    "models": ["stable-diffusion-v1-5"],
    "nodes": ["CLIPTextEncode", "KSampler", "VAEDecode"]
  },
  "author": "Your Name",
  "version": "1.0.0"
}
```

## Any Contributions You Make Will Be Under the MIT Software License

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project.

## Report Bugs Using GitHub's [Issues](https://github.com/Miktos-Universe/miktos-workflows/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/Miktos-Universe/miktos-workflows/issues/new/choose).

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample workflow if possible
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Use a Consistent Coding Style

### JSON Formatting

- Use 2 spaces for indentation
- Use double quotes for strings
- Sort object keys alphabetically where possible
- Include trailing commas where allowed

### Documentation

- Use clear, concise language
- Include examples where helpful
- Follow markdown best practices
- Use proper heading hierarchy

## License

By contributing, you agree that your contributions will be licensed under its MIT License.

## Questions?

Don't hesitate to reach out! You can:

- Open an issue with the `question` label
- Join our community discussions
- Contact the maintainers directly

Thank you for contributing to Miktos Workflows! 🎨✨
