from pathlib import Path

from signal_processing.loader import load_radioml
from signal_processing.stft import compute_stft
from spectrogram_generation.spectrogram import save_spectrogram

print("Loading dataset...")

dataset = load_radioml(
    "datasets/raw/radioml/RML2016.10a_dict.pkl"
)

output_root = Path(
    "datasets/processed/spectrograms"
)

total_images = 0

for key, recordings in dataset.items():

    modulation, snr = key

    class_folder = output_root / modulation

    class_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    for index, sample in enumerate(recordings[:10]):

        iq = sample[0] + 1j * sample[1]

        frequencies, times, Zxx = compute_stft(iq)

        filename = f"{modulation}_{snr}_{index}.png"

        save_spectrogram(
            frequencies,
            times,
            Zxx,
            class_folder / filename
        )

        total_images += 1

print("=" * 50)
print("Dataset generation completed.")
print(f"Images generated: {total_images}")
print("=" * 50)