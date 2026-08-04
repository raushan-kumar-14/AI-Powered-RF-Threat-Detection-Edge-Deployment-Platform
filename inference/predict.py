"""
Inference using exported ONNX model.
"""

from pathlib import Path

import numpy as np
import onnxruntime as ort

from PIL import Image
from torchvision import transforms


class RFPredictor:

    def __init__(self, model_path):

        self.session = ort.InferenceSession(model_path)

        self.input_name = self.session.get_inputs()[0].name

        self.classes = [
            "8PSK",
            "AM-DSB",
            "AM-SSB",
            "BPSK",
            "CPFSK",
            "GFSK",
            "PAM4",
            "QAM16",
            "QAM64",
            "QPSK",
            "WBFM",
        ]

        self.transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
        ])

    def predict(self, image_path):

        image = Image.open(image_path).convert("RGB")

        tensor = self.transform(image)

        tensor = tensor.unsqueeze(0)

        outputs = self.session.run(
            None,
            {
                self.input_name: tensor.numpy()
            }
        )

        scores = outputs[0][0]

        prediction = int(np.argmax(scores))

        exp_scores = np.exp(scores - np.max(scores))
        probabilities = exp_scores / np.sum(exp_scores)

        confidence = float(probabilities[prediction]) * 100

        return {
            "class": self.classes[prediction],
            "confidence": round(confidence, 2)
        }