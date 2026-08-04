from training.export_onnx import export_onnx

export_onnx(
    model_path="models/checkpoints/best_model.pth",
    output_path="models/exported/rf_threat_detector.onnx",
)