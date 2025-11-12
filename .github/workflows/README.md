# GitHub Workflows

This directory contains GitHub Actions workflows for the HoloCubic AIO Tool project.

## Workflows

### Build and Release

The workflows in this directory handle:
- Automated building of the application using PyInstaller
- Creating releases with compiled executables
- Cross-platform support for Windows, macOS, and Linux

## Release Process

To create a new release:

1. Update the version number in your code
2. Create and push a new tag:
   ```bash
   git tag -a v2.0.1 -m "Release 2.0.1"
   git push origin v2.0.1
   ```
3. The GitHub Actions workflow will automatically build and create a release

## Configuration

The build process uses the `CubicAIO_Tool.spec` file for PyInstaller configuration, which includes:
- Application entry point: `CubicAIO_Tool.py`
- Required data files: `cubictool.json`, `image` directory
- Hidden imports: `esptool`
- Application icon: `image/holo_256.ico`