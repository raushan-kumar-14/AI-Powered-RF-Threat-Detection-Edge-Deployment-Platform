from edge_deployment.tensorrt_export import convert_to_tensorrt

convert_to_tensorrt(
    "models/exported/rf_threat_detector.onnx"
)