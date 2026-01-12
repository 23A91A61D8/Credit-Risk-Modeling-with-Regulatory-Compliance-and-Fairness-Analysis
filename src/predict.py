import pandas as pd

def predict_risk(model, X: pd.DataFrame):
    """
    Generate default probability predictions.
    """

    probabilities = model.predict_proba(X)[:, 1]
    return probabilities
