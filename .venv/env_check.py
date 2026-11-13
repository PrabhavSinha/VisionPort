
import sys
import platform
import subprocess
from datetime import datetime
from importlib.metadata import version, PackageNotFoundError

REPORT_FILE = "env_report.md"

packages = [
    "torch",
    "torchvision",
    "ultralytics",
    "streamlit",
    "fastapi",
    "uvicorn",
    "pandas",
    "pillow",
]

report = []

def add(text):
    print(text)
    report.append(text)

add("# VisionPort Environment Report")
add(f"\nGenerated: {datetime.now()}")
add("\n## System Information")
add(f"- Operating System: {platform.platform()}")
add(f"- Python Version: {sys.version}")
add(f"- Python Executable: {sys.executable}")

add("\n## Installed Packages")

for package in packages:
    try:
        installed_version = version(package)
        add(f"- {package}: {installed_version}")
    except PackageNotFoundError:
        add(f"- {package}: NOT INSTALLED")

add("\n## NVIDIA GPU Information")

try:
    result = subprocess.run(
        ["nvidia-smi"],
        capture_output=True,
        text=True,
        timeout=10
    )

    if result.returncode == 0:
        add("```text")
        add(result.stdout)
        add("```")
    else:
        add("NVIDIA GPU information unavailable.")
        add(result.stderr)

except FileNotFoundError:
    add("nvidia-smi not found. NVIDIA driver may be unavailable.")

except subprocess.TimeoutExpired:
    add("nvidia-smi timed out.")

add("\n## PyTorch and CUDA Check")

try:
    import torch

    add(f"- PyTorch Version: {torch.__version__}")
    add(f"- CUDA Available: {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        add(f"- CUDA Version: {torch.version.cuda}")
        add(f"- cuDNN Version: {torch.backends.cudnn.version()}")
        add(f"- GPU Name: {torch.cuda.get_device_name(0)}")

        # Test computation on GPU
        a = torch.randn(1000, 1000, device="cuda")
        b = torch.randn(1000, 1000, device="cuda")
        c = torch.matmul(a, b)

        torch.cuda.synchronize()

        add("- GPU Matrix Multiplication: SUCCESS")
        add(f"- Output Shape: {list(c.shape)}")

    else:
        add("- GPU Matrix Multiplication: SKIPPED")
        add("- PyTorch will use CPU for this test.")

except Exception as error:
    add(f"- PyTorch check failed: {error}")

with open(REPORT_FILE, "w", encoding="utf-8") as file:
    file.write("\n".join(report))

print(f"\nReport saved to {REPORT_FILE}")