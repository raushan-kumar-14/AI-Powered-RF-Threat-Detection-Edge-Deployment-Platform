"""
Visualization utilities for RF IQ signals.

This module provides functions to visualize:
1. In-Phase (I) Component
2. Quadrature (Q) Component
3. Magnitude
4. Phase

Author: Raushan Kumar
Project: AI-Powered RF Threat Detection & Edge Deployment Platform
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_i_component(iq: np.ndarray) -> None:
    """
    Plot the In-Phase (I) component of IQ samples.

    Parameters
    ----------
    iq : np.ndarray
        Complex IQ samples.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(iq.real)
    plt.title("In-Phase (I) Component")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_q_component(iq: np.ndarray) -> None:
    """
    Plot the Quadrature (Q) component of IQ samples.

    Parameters
    ----------
    iq : np.ndarray
        Complex IQ samples.
    """
    plt.figure(figsize=(12, 4))
    plt.plot(iq.imag)
    plt.title("Quadrature (Q) Component")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_magnitude(iq: np.ndarray) -> None:
    """
    Plot the magnitude of IQ samples.

    Parameters
    ----------
    iq : np.ndarray
        Complex IQ samples.
    """
    magnitude = np.abs(iq)

    plt.figure(figsize=(12, 4))
    plt.plot(magnitude)
    plt.title("Signal Magnitude")
    plt.xlabel("Sample Index")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_phase(iq: np.ndarray) -> None:
    """
    Plot the phase of IQ samples.

    Parameters
    ----------
    iq : np.ndarray
        Complex IQ samples.
    """
    phase = np.angle(iq)

    plt.figure(figsize=(12, 4))
    plt.plot(phase)
    plt.title("Signal Phase")
    plt.xlabel("Sample Index")
    plt.ylabel("Phase (Radians)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_iq_constellation(iq: np.ndarray) -> None:
    """
    Plot the IQ constellation diagram.

    Parameters
    ----------
    iq : np.ndarray
        Complex IQ samples.
    """
    plt.figure(figsize=(6, 6))
    plt.scatter(iq.real, iq.imag, s=5)
    plt.title("IQ Constellation Diagram")
    plt.xlabel("In-Phase (I)")
    plt.ylabel("Quadrature (Q)")
    plt.grid(True)
    plt.axis("equal")
    plt.tight_layout()
    plt.show()
    
def plot_all(iq: np.ndarray, title: str = "IQ Signal") -> None:
    """
    Plot all visualizations for an IQ signal.

    Parameters
    ----------
    iq : np.ndarray
        Complex IQ samples.
    title : str
        Signal title (reserved for future use).
    """

    plot_i_component(iq)
    plot_q_component(iq)
    plot_magnitude(iq)
    plot_phase(iq)
    plot_iq_constellation(iq)