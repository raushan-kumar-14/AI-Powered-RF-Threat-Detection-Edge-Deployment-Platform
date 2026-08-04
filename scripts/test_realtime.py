from signal_processing.loader import load_radioml
from inference.realtime_predictor import RealtimePredictor

# Load dataset
dataset = load_radioml(
    "datasets/raw/radioml/RML2016.10a_dict.pkl"
)

# Select one signal
signals = dataset[("QPSK", 10)]

sample = signals[0]

# Convert to complex IQ
iq = sample[0] + 1j * sample[1]

# Load predictor
predictor = RealtimePredictor(
    "models/exported/rf_threat_detector.onnx"
)

# Predict
prediction = predictor.predict(iq)

print("=" * 60)
print("REAL-TIME RF PREDICTION")
print("=" * 60)
print("Predicted Signal:", prediction)