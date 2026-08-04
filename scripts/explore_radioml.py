from signal_processing.loader import load_radioml

# Load dataset
dataset = load_radioml(
    "datasets/raw/radioml/RML2016.10a_dict.pkl"
)

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print(f"Dataset Type : {type(dataset)}")
print(f"Total Keys   : {len(dataset)}")

# Extract all modulation classes
modulations = sorted(set(mod for mod, snr in dataset.keys()))

# Extract all SNR values
snr_values = sorted(set(snr for mod, snr in dataset.keys()))

print("\nModulation Classes:")
print(modulations)

print("\nNumber of Modulation Classes:", len(modulations))

print("\nAvailable SNR Values:")
print(snr_values)

print("\nNumber of SNR Levels:", len(snr_values))