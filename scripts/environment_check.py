import torch
import numpy
import pandas
import matplotlib

print("=" * 40)
print("Environment Check")
print("=" * 40)

print("PyTorch:", torch.__version__)
print("NumPy:", numpy.__version__)
print("Pandas:", pandas.__version__)
print("Matplotlib:", matplotlib.__version__)

print()

print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
else:
    print("Running on CPU")