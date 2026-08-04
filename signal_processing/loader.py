from pathlib import Path
import pickle
import numpy as np


def load_npy(file_path: str | Path) -> np.ndarray:
    """
    Load IQ samples stored in NumPy (.npy) format.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    return np.load(file_path)


def load_radioml(file_path: str | Path) -> dict:
    """
    Load the DeepSig RadioML 2016.10A dataset.

    Parameters
    ----------
    file_path : str | Path
        Path to RML2016.10a_dict.pkl

    Returns
    -------
    dict
        Dictionary containing RadioML dataset.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    with open(file_path, "rb") as file:
        dataset = pickle.load(file, encoding="latin1")

    return dataset