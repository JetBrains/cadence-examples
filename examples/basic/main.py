import torch
from pathlib import Path

print(f"hello from main.py, torch version: {torch.__version__}")

outputs = Path("outputs")
outputs.mkdir(parents=True, exist_ok=True)

new_file = outputs / "new_file.txt"
new_file.write_text(f"hello from main.py again, torch version is still: {torch.__version__}")
