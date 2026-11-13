
# VisionPort

## Project Overview

VisionPort is a computer vision project built using YOLOv8.
It processes uploaded images and performs object detection.

The project includes:
- Streamlit-based user interface
- FastAPI inference gateway
- Detailed inference request tracing
- PyTorch-based model execution
- GPU and CUDA environment checking

## Technologies Used

- Python
- YOLOv8
- PyTorch
- Streamlit
- FastAPI
- Uvicorn
- OpenCV

## Project Structure

```text
Visionport/
|
├── app.py
├── env_check.py
├── env_report.md
├── requirements.txt
├── README.md
├── .gitignore
|
├── data/
├── models/
├── eval/
├── optimise/
├── serve/
│   ├── __init__.py
│   ├── gateway.py
│   └── gateway_trace.py
|
├── train/
├── logs/
├── docs/
└── failures/
```

## Environment Setup

Create and activate a virtual environment.

Install the required packages:

    pip install -r requirements.txt

Check the Python and GPU environment:

    python env_check.py

The environment report is saved as env_report.md.

## Running the Project

### Streamlit Interface

    streamlit run app.py

### FastAPI Gateway

    uvicorn serve.gateway:app --reload

### FastAPI Gateway with Request Tracing

    uvicorn serve.gateway_trace:app --reload

### FastAPI Documentation

After starting the gateway, open:

    http://127.0.0.1:8000/docs

## Environment and GPU

The project uses PyTorch for model execution.

The env_check.py script checks:
- Python version
- Installed packages
- NVIDIA GPU information
- PyTorch version
- CUDA availability

## Current Limitations

- The current YOLOv8 model uses pretrained weights.
- Object detection is limited to the classes supported by the selected model.
- Custom object classes require suitable training data and model training.

## Development

The repository is organized to support future development
of training, evaluation, optimization and deployment modules.

## Git Development Workflow

The project uses Git for version control.

### Main Branch

The main branch contains the stable project version.

### Feature Branches

New features and improvements are developed
in separate branches.

Example:

    git switch -c feature/env-check

### Commit Changes

    git add .
    git commit -m "Describe your changes"

### Merge Changes

After completing a feature, switch to main
and merge the feature branch.

    git switch main
    git merge feature/env-check
