from signal_processing.loader import load_radioml
from signal_processing.visualization import plot_all
import numpy as np

# Load the RadioML dataset
dataset = load_radioml(
    "datasets/raw/radioml/RML2016.10a_dict.pkl"
)

# Select one modulation and one SNR
modulation = "QPSK"
snr = 10

# Get all recordings for this key
signals = dataset[(modulation, snr)]

sample = signals[0]

i_samples = sample[0]
q_samples = sample[1]

iq = i_samples + 1j * q_samples


print("=" * 60)
print("SIGNAL INFORMATION")
print("=" * 60)

print(f"Modulation : {modulation}")
print(f"SNR        : {snr} dB")

print(f"\nArray Type : {type(signals)}")
print(f"Shape      : {signals.shape}")
print(f"Data Type  : {signals.dtype}")

print("\nNumber of recordings:", len(signals))



print("\nSingle Recording Shape:", sample.shape)



print("\nComplex IQ Shape:", iq.shape)
print("Complex IQ Data Type:", iq.dtype)

print("\nFirst 10 I samples:")
print(i_samples[:10])

print("\nFirst 10 Q samples:")
print(q_samples[:10])

print("\nFirst 10 Complex IQ samples:")
print(iq[:10])

print("\nGenerating visualizations...")

plot_all(iq)