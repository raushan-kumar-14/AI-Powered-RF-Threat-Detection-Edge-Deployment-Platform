from inference.predict import RFPredictor

predictor = RFPredictor(
    "models/exported/rf_threat_detector.onnx"
)

prediction = predictor.predict(
    "datasets/processed/spectrograms/QPSK/QPSK_-2_0.png"
)

print("=" * 60)
print("Prediction")
print("=" * 60)
print(prediction)