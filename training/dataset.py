"""
PyTorch Dataset for RF Spectrogram Images.
"""

from pathlib import Path

from PIL import Image

from torch.utils.data import Dataset


class SpectrogramDataset(Dataset):
    """
    Custom Dataset for RF spectrogram images.
    """

    def __init__(self, root_dir, transform=None):

        self.root_dir = Path(root_dir)
        self.transform = transform

        self.image_paths = []
        self.labels = []

        self.classes = sorted(
            [
                folder.name
                for folder in self.root_dir.iterdir()
                if folder.is_dir()
            ]
        )

        self.class_to_idx = {
            name: idx
            for idx, name in enumerate(self.classes)
        }

        for class_name in self.classes:

            class_folder = self.root_dir / class_name

            for image_path in class_folder.glob("*.png"):

                self.image_paths.append(image_path)
                self.labels.append(
                    self.class_to_idx[class_name]
                )

    def __len__(self):

        return len(self.image_paths)

    def __getitem__(self, index):

        image = Image.open(
            self.image_paths[index]
        ).convert("RGB")

        label = self.labels[index]

        if self.transform:
            image = self.transform(image)

        return image, label