from signal_processing.loader import load_radioml
from signal_processing.stft import compute_stft
from spectrogram_generation.spectrogram import generate_spectrogram

dataset = load_radioml(
    "datasets/raw/radioml/RML2016.10a_dict.pkl"
)

signals = dataset[("QPSK", 10)]

sample = signals[0]

iq = sample[0] + 1j * sample[1]

frequencies, times, Zxx = compute_stft(iq)

generate_spectrogram(
    frequencies,
    times,
    Zxx,
    title="QPSK Spectrogram"
)