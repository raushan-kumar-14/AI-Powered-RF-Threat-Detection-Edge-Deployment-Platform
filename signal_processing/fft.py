"""
FFT utilities for RF IQ signals.
"""

import numpy  as np

import matplotlib.pyplot as plt


def compute_fft(iq_signal: np.ndarray):
    """
    Compute FFT and frequency axis.

    Parameters
    ----------
    iq_signal : np.ndarray
        Complex IQ samples.

    Returns
    -------
    frequencies : np.ndarray
        Frequency bins.

    spectrum : np.ndarray
        FFT values.
    """

    n = len(iq_signal)

    spectrum = np.fft.fft(iq_signal)

    frequencies = np.fft.fftfreq(n)

    return frequencies, spectrum




def compute_fft_magnitude(spectrum):
    """
    Compute magnitude spectrum.
    """
    return np.abs(spectrum)


def compute_power_spectrum(spectrum):
    """
    Compute power spectrum.
    """
    return np.abs(spectrum) ** 2


def plot_fft(frequencies, spectrum, title="FFT Spectrum"):
    """
    Plot FFT magnitude.
    """

    magnitude = np.abs(spectrum)

    plt.figure(figsize=(12, 5))

    plt.plot(frequencies, magnitude)

    plt.title(title)

    plt.xlabel("Normalized Frequency")

    plt.ylabel("Magnitude")

    plt.grid(True)

    plt.tight_layout()

    plt.show()
    
def shift_fft(frequencies, spectrum):
    """
    Shift FFT so zero frequency is centered.
    """

    shifted_freq = np.fft.fftshift(frequencies)
    shifted_spectrum = np.fft.fftshift(spectrum)

    return shifted_freq, shifted_spectrum


def magnitude_db(spectrum):
    """
    Convert FFT magnitude into decibels.
    """

    magnitude = np.abs(spectrum)

    return 20 * np.log10(magnitude + 1e-12)

def plot_shifted_fft(frequencies, spectrum, title="Centered FFT"):

    shifted_freq, shifted_spectrum = shift_fft(
        frequencies,
        spectrum
    )

    magnitude = magnitude_db(shifted_spectrum)

    plt.figure(figsize=(12,5))

    plt.plot(
        shifted_freq,
        magnitude
    )

    plt.title(title)

    plt.xlabel("Normalized Frequency")

    plt.ylabel("Magnitude (dB)")

    plt.grid(True)

    plt.tight_layout()

    plt.show()