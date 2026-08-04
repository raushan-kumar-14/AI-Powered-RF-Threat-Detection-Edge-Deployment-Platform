"""
Export trained CNN model to ONNX.
"""

from pathlib import Path

import torch

from training.cnn_model import RFThreatCNN


def export_onnx(
    model_path,
    output_path,
    num_classes=11,
):

    device = torch.device("cpu")

    model = RFThreatCNN(
        num_classes=num_classes,
    )

    model.load_state_dict(
        torch.load(
            model_path,
            map_location=device,
        )
    )

    model.eval()

    dummy_input = torch.randn(
        1,
        3,
        128,
        128,
    )

    Path(output_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    torch.onnx.export(
        model,
        dummy_input,
        output_path,
        export_params=True,
        opset_version=17,
        do_constant_folding=True,
        input_names=["input"],
        output_names=["output"],
        dynamic_axes={
            "input": {0: "batch_size"},
            "output": {0: "batch_size"},
        },
    )

    print("=" * 60)
    print("ONNX model exported successfully.")
    print(output_path)
    print("=" * 60)