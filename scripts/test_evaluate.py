from training.evaluate import evaluate_model

evaluate_model(
    model_path="models/checkpoints/best_model.pth",
    dataset_path="datasets/processed/spectrograms",
)