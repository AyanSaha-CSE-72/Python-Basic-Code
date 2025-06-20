import os
import subprocess
import sys

# Required packages
packages = [
    "opencv-python",
    "mediapipe",
    "pycaw",
    "comtypes"
]

print("📦 Installing required Python packages...\n")

for package in packages:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Installed: {package}")
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install: {package}")

print("\n🎉 All done! Try running your volume control script again.")
