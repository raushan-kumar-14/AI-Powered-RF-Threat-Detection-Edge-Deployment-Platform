from torchvision import transforms

from training.dataset import SpectrogramDataset

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

dataset = SpectrogramDataset(
    "datasets/processed/spectrograms",
    transform=transform
)

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("Total Images :", len(dataset))

print("Classes :")
print(dataset.classes)

print()

image, label = dataset[0]

print("Image Shape :", image.shape)
print("Label :", label)