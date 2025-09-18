from pathlib import Path

import torch

print(f"hello from test.py")

local_test_dataset = Path("datasets/local_test_dataset.csv")

print(f"file {local_test_dataset.name} exists: {local_test_dataset.exists()}")
