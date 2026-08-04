"""
Backend prediction utilities.
"""

from inference.predict import RFPredictor

predictor = RFPredictor(
    "models/exported/rf_threat_detector.onnx"
)


def predict_image(image_path):
    return predictor.predict(image_path)