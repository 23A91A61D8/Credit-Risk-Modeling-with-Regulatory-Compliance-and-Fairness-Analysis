import pandas as pd
import numpy as np

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create engineered features for credit risk modeling.
    """

    df = df.copy()

    # Ratio-based features
    df["credit_per_month"] = df["Credit amount"] / df["Duration"]
    df["credit_per_age"] = df["Credit amount"] / df["Age"]

    # Interaction features
    df["age_duration_interaction"] = df["Age"] * df["Duration"]

    # Transformations
    df["log_credit_amount"] = np.log1p(df["Credit amount"])

    return df
