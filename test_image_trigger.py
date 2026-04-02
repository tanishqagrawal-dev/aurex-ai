#!/usr/bin/env python3
"""
Test script to simulate image generation trigger from the assistant
"""
import os
import sys
import subprocess
from time import sleep

# Change to workspace directory
os.chdir(r"c:\Users\tanis\OneDrive\Desktop\jarvis ai")

print("=" * 50)
print("Testing Image Generation Trigger")
print("=" * 50)

# Simulate what the assistant does
print("\n[1] Simulating FirstLayerDMM decision...")
ImageGenerationQuery = "generate image of a lion"
print(f"    Decision: {ImageGenerationQuery}")

print("\n[2] Writing trigger to ImageGeneration.data...")
trigger_file = r"Frontend\Files\ImageGeneration.data"
with open(trigger_file, "w") as f:
    f.write(f"{ImageGenerationQuery},True")
print(f"    Wrote: '{ImageGenerationQuery},True'")

print("\n[3] Reading back to verify...")
with open(trigger_file, "r") as f:
    content = f.read()
print(f"    Read: '{content}'")

print("\n[4] Getting Python executable...")
venv_python = os.path.join(os.getcwd(), ".venv", "Scripts", "python.exe")
if os.path.exists(venv_python):
    python_exe = venv_python
    print(f"    Using venv: {python_exe}")
else:
    python_exe = sys.executable
    print(f"    Using system Python: {python_exe}")

print("\n[5] Starting ImageGeneration.py subprocess...")
try:
    p1 = subprocess.Popen([python_exe, r'Backend\ImageGeneration.py'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        stdin=subprocess.PIPE, shell=False)
    print(f"    Process started (PID: {p1.pid})")
    
    print("\n[6] Waiting for completion (max 120 seconds)...")
    try:
        stdout, stderr = p1.communicate(timeout=120)
        print(f"    Process completed with exit code: {p1.returncode}")
        if stdout:
            print(f"    STDOUT:\n{stdout.decode()}")
        if stderr:
            print(f"    STDERR:\n{stderr.decode()}")
    except subprocess.TimeoutExpired:
        p1.kill()
        print("    Process timed out after 120 seconds")
    
except Exception as e:
    print(f"    ERROR: {e}")
    import traceback
    traceback.print_exc()

print("\n[7] Checking generated images...")
data_dir = r"Data"
lion_images = [f for f in os.listdir(data_dir) if "lion" in f.lower() and f.endswith(".jpg")]
print(f"    Found {len(lion_images)} lion images: {lion_images}")

print("\n" + "=" * 50)
print("Test Complete!")
print("=" * 50)
