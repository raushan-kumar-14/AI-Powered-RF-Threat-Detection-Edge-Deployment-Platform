from signal_processing.loader import load_radioml
from signal_processing.stft import compute_stft

dataset = load_radioml(
    "datasets/raw/radioml/RML2016.10a_dict.pkl"
)

signals = dataset[("QPSK", 10)]

sample = signals[0]

iq = sample[0] + 1j * sample[1]

frequencies, times, Zxx = compute_stft(iq)

print("Frequencies Shape :", frequencies.shape)
print("Time Shape        :", times.shape)
print("STFT Shape        :", Zxx.shape)