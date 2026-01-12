from lightgbm import LGBMClassifier
import pandas as pd

def train_model(X: pd.DataFrame, y: pd.Series):
    """
    Train LightGBM credit risk model.
    """

    model = LGBMClassifier(
        objective="binary",
        class_weight="balanced",
        n_estimators=200,
        max_depth=5,
        learning_rate=0.1,
        random_state=42
    )

    model.fit(X, y)
    return model
