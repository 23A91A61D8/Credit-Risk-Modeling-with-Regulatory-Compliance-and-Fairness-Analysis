import pandas as pd
import numpy as np

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess raw credit data.
    """

    df = df.copy()

    # Drop unnecessary index column
    if "Unnamed: 0" in df.columns:
        df.drop(columns=["Unnamed: 0"], inplace=True)

    # Create proxy target variable
    df["default"] = np.where(
        (df["Credit amount"] > df["Credit amount"].median()) &
        (df["Duration"] > df["Duration"].median()),
        1,
        0
    )

    return df
