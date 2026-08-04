"""
Evaluate the trained CNN model.
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from training.dataset import SpectrogramDataset
from training.cnn_model import RFThreatCNN


def evaluate_model(model_path, dataset_path):

    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])

    dataset = SpectrogramDataset(
        dataset_path,
        transform=transform,
    )

    loader = DataLoader(
        dataset,
        batch_size=32,
        shuffle=False,
    )

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    model = RFThreatCNN(
        num_classes=len(dataset.classes)
    ).to(device)

    model.load_state_dict(
        torch.load(
            model_path,
            map_location=device,
        )
    )

    model.eval()

    y_true = []
    y_pred = []

    with torch.no_grad():

        for images, labels in loader:

            images = images.to(device)

            outputs = model(images)

            predictions = outputs.argmax(dim=1)

            y_true.extend(labels.numpy())

            y_pred.extend(
                predictions.cpu().numpy()
            )

    accuracy = accuracy_score(
        y_true,
        y_pred,
    )

    print("=" * 60)
    print("MODEL EVALUATION")
    print("=" * 60)

    print(f"Accuracy : {accuracy:.4f}")

    print("\nClassification Report\n")

    print(
        classification_report(
            y_true,
            y_pred,
            target_names=dataset.classes,
        )
    )

    print("\nConfusion Matrix\n")

    cm = confusion_matrix(
    y_true,
    y_pred,
    )

    print(cm)
    
    Path("outputs").mkdir(exist_ok=True)

    plot_confusion_matrix(
        cm,
        dataset.classes,
    )
    
def plot_confusion_matrix(cm, class_names):

    plt.figure(figsize=(10, 8))

    plt.imshow(cm, interpolation="nearest")

    plt.title("Confusion Matrix")

    plt.colorbar()

    tick_marks = np.arange(len(class_names))

    plt.xticks(
        tick_marks,
        class_names,
        rotation=45,
        ha="right",
    )

    plt.yticks(
        tick_marks,
        class_names,
    )

    plt.xlabel("Predicted Label")

    plt.ylabel("True Label")

    plt.tight_layout()

    plt.savefig(
        "outputs/confusion_matrix.png",
        dpi=300,
    )

    plt.show()