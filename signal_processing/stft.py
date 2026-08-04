"""
STFT utilities for RF IQ signals.
"""

import numpy as np
from scipy.signal import stft


def compute_stft(
    iq_signal: np.ndarray,
    nperseg: int = 32,
    noverlap: int = 16,
):
    """
    Compute Short-Time Fourier Transform.

    Parameters
    ----------
    iq_signal : np.ndarray
        Complex IQ samples.

    nperseg : int
        Window size.

    noverlap : int
        Number of overlapping samples.

    Returns
    -------
    frequencies
    times
    Zxx
    """

    frequencies, times, Zxx = stft(
        iq_signal,
        nperseg=nperseg,
        noverlap=noverlap,
        return_onesided=False,
    )

    return frequencies, times, Zxx