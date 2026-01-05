from typing import Optional
import os
import pandas as pd


def load(path: str) -> Optional[pd.DataFrame]:
    """
    Load a CSV dataset and print its dimensions.
    """
    try:
        if not isinstance(path, str) or not path:
            print("Error: invalid path")
            return None

        if not os.path.isfile(path):
            print("Error: file not found")
            return None

        df = pd.read_csv(path, header=0)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception:
        print("Error: could not load dataset")
        return None


def main():
    """
    Simple local test.
    """
    df = load("../life_expectancy_years.csv")
    if df is not None:
        print(df)


if __name__ == "__main__":
    main()
