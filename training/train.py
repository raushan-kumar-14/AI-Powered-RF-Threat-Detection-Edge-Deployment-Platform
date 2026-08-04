"""
CNN training script.
"""

from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import random_split, DataLoader
from torchvision import transforms

from training.dataset import SpectrogramDataset
from training.cnn_model import RFThreatCNN


def train():

    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])

    dataset = SpectrogramDataset(
        "datasets/processed/spectrograms",
        transform=transform,
    )

    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size

    train_dataset, val_dataset = random_split(
        dataset,
        [train_size, val_size],
    )

    train_loader = DataLoader(
        train_dataset,
        batch_size=32,
        shuffle=True,
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=32,
        shuffle=False,
    )

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    print(f"Using device: {device}")

    model = RFThreatCNN(
        num_classes=len(dataset.classes)
    ).to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001,
    )

    epochs = 5

    best_accuracy = 0.0

    checkpoint_dir = Path("models/checkpoints")
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    for epoch in range(epochs):

        model.train()

        running_loss = 0.0

        for images, labels in train_loader:

            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()

            outputs = model(images)

            loss = criterion(outputs, labels)

            loss.backward()

            optimizer.step()

            running_loss += loss.item()

        train_loss = running_loss / len(train_loader)

        print(
            f"Epoch {epoch+1}/{epochs} "
            f"| Train Loss: {train_loss:.4f}"
        )

        accuracy = validate(
            model,
            val_loader,
            device,
        )

        if accuracy > best_accuracy:

            best_accuracy = accuracy

            torch.save(
                model.state_dict(),
                checkpoint_dir / "best_model.pth",
            )

            print("Best model saved.")


def validate(model, loader, device):

    model.eval()

    correct = 0
    total = 0

    with torch.no_grad():

        for images, labels in loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            predictions = outputs.argmax(dim=1)

            total += labels.size(0)

            correct += (
                predictions == labels
            ).sum().item()

    accuracy = correct / total

    print(f"Validation Accuracy: {accuracy:.4f}")

    return accuracy


if __name__ == "__main__":
    train()