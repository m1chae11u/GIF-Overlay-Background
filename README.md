# GIF-Overlay-Background
This repository contains a Python script that overlays a square animated GIF with a transparent background onto a rectangular solid color PNG background, producing a single composite animated GIF. The script processes each frame of the input GIF, centers it over the background, and preserves its animation timing.

## Setup
1. Make sure you have conda installed on your system
2. Set up the environment using the provided script:
   ```bash
   chmod +x setup_env.sh
   ./setup_env.sh
   ```
3. This will create and activate a conda environment with all required dependencies

## Usage
After setting up the environment, you can run the script as follows:

```bash
python gifcompositor.py foreground.gif background.png output.gif
```

The script will center the animated GIF over the background image and preserve all animation timing from the original GIF.

### Parameters:
- `foreground.gif`: Path to the input square GIF with transparency
- `background.png`: Path to the rectangular solid color PNG background
- `output.gif`: Path for the output composite GIF
