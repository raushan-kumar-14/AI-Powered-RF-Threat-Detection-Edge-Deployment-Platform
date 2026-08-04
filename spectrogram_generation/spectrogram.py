"""
Spectrogram generation utilities.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def generate_spectrogram(
    frequencies,
    times,
    Zxx,
    title="Spectrogram"
):
    """
    Display a spectrogram from STFT output.
    """

    magnitude = np.abs(Zxx)

    plt.figure(figsize=(10, 6))

    plt.pcolormesh(
        times,
        frequencies,
        20 * np.log10(magnitude + 1e-10),
        shading="gouraud"
    )

    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.colorbar(label="Magnitude (dB)")
    plt.tight_layout()
    plt.show()
    



def save_spectrogram(
    frequencies,
    times,
    Zxx,
    save_path,
    dpi=100
):
    """
    Save a spectrogram image to disk.
    """

    save_path = Path(save_path)
    save_path.parent.mkdir(parents=True, exist_ok=True)

    magnitude = np.abs(Zxx)

    plt.figure(figsize=(4, 4))

    plt.pcolormesh(
        times,
        frequencies,
        20 * np.log10(magnitude + 1e-10),
        shading="gouraud"
    )

    plt.axis("off")

    plt.tight_layout(pad=0)

    plt.savefig(
        save_path,
        dpi=dpi,
        bbox_inches="tight",
        pad_inches=0
    )

    plt.close()