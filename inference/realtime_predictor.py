"""
Real-time RF signal prediction pipeline.
"""

from signal_processing.stft import compute_stft
from spectrogram_generation.spectrogram import save_spectrogram

from inference.predict import RFPredictor

import tempfile
import os


class RealtimePredictor:

    def __init__(self, model_path):

        self.predictor = RFPredictor(model_path)

    def predict(self, iq):

        frequencies, times, Zxx = compute_stft(iq)

        temp = tempfile.NamedTemporaryFile(
            suffix=".png",
            delete=False
        )

        temp.close()

        save_spectrogram(
            frequencies,
            times,
            Zxx,
            temp.name
        )

        prediction = self.predictor.predict(
            temp.name
        )

        os.remove(temp.name)

        return prediction