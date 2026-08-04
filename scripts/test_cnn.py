import torch

from training.cnn_model import RFThreatCNN

model = RFThreatCNN(num_classes=11)

print("=" * 60)
print(model)
print("=" * 60)

dummy = torch.randn(1, 3, 128, 128)

output = model(dummy)

print()

print("Input Shape :", dummy.shape)
print("Output Shape:", output.shape)