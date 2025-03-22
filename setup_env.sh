#!/bin/bash

# Set environment name
ENV_NAME="gif_compositor"

# Create conda environment
conda create -y -n $ENV_NAME python=3.9

# Activate environment
eval "$(conda shell.bash hook)"
conda activate $ENV_NAME

# Install dependencies from requirements.txt
conda install -y -c conda-forge pillow

echo "Environment '$ENV_NAME' has been created and activated with all dependencies installed."
echo "To activate this environment in the future, run: conda activate $ENV_NAME"
