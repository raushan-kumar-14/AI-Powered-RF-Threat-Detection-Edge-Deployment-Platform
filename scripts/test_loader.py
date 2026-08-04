from signal_processing.loader import load_npy

iq = load_npy("datasets/sample.npy")

print(type(iq))
print(iq.shape)
print(iq.dtype)