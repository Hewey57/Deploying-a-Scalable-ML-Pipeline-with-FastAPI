import pytest
# TODO: add necessary import
import os
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

from ml.model import train_model
from ml.data import process_data
import numpy as np

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    Test whether synthetic classification data is generated correctly.
    """
    X, y = make_classification(n_samples=50, n_features=5, random_state=42)
    assert X.shape == (50, 5), f"Unexpected shape for X: {X.shape}"
    assert y.shape == (50,), f"Unexpected shape for y: {y.shape}"


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Test whether the census.csv file has rows and columns.
    """
    filepath = os.path.join("data", "census.csv")
    assert os.path.exists(filepath), f"File not found: {filepath}"
    df = pd.read_csv(filepath)

    assert df.shape[0] > 0, "CSV file contains 0 rows."
    assert df.shape[1] > 0, "CSV file contains 0 columns."

# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    Test whether the model is trained as a RandomForestClassifier.
    """
    # Create mock training data
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)

    model = train_model(X, y)

    assert isinstance(model, RandomForestClassifier), f"Model is not RandomForestClassifier, got {type(model)}"