from pathlib import Path

import torch

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_DIR = PROJECT_ROOT / "datasets"

MODEL_DIR = PROJECT_ROOT / "models"

LOG_DIR = PROJECT_ROOT / "logs"

OUTPUT_DIR = PROJECT_ROOT / "outputs"



DEVICE = "cuda" if torch.cuda.is_available() else "cpu"