"""
TensorRT conversion utilities.
"""

from pathlib import Path


def convert_to_tensorrt(onnx_path: str):

    onnx_path = Path(onnx_path)

    if not onnx_path.exists():
        raise FileNotFoundError(onnx_path)

    print("=" * 60)
    print("TensorRT Conversion")
    print("=" * 60)

    print("Input Model :", onnx_path)

    print()
    print("Normally the following command is executed:")
    print()

    print(
        f"trtexec --onnx={onnx_path} "
        "--saveEngine=models/exported/rf_detector.engine"
    )

    print()
    print("TensorRT conversion completed (simulation).")