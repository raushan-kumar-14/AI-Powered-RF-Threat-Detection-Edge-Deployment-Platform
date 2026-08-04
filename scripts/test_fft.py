from signal_processing.loader import load_radioml
from signal_processing.fft import (
    compute_fft,
    plot_fft,
    plot_shifted_fft,
)

dataset = load_radioml(
    "datasets/raw/radioml/RML2016.10a_dict.pkl"
)

signals = dataset[("QPSK", 10)]

sample = signals[0]

iq = sample[0] + 1j * sample[1]

frequencies, spectrum = compute_fft(iq)

print("FFT Shape:", spectrum.shape)
print("Frequency Shape:", frequencies.shape)

print("\nFirst 10 Frequency Bins:")
print(frequencies[:10])

print("\nFirst 10 FFT Values:")
print(spectrum[:10])



plot_fft(
    frequencies,
    spectrum,
    title="QPSK FFT Spectrum"
)

plot_shifted_fft(
    frequencies,
    spectrum,
    title="Centered QPSK FFT Spectrum (dB)"
)