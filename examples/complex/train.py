from pathlib import Path

import torch

print(f"hello from train.py")

include_anyway = Path("dir/to/exclude/include_anyway.txt")

print(f"file {include_anyway.name} exists: {include_anyway.exists()}")

Path("datasets/my_dataset_from_s3.csv")