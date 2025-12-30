import pandas as pd
import matplotlib.pyplot as plt

from load_csv import load


def main() -> None:
    """
    Plot life expectancy of the campus country.
    """
    try:
        df = load("../life_expectancy_years.csv")
        if df is None or "country" not in df.columns:
            print("Error: could not load dataset")
            return

        country = "Luxembourg"
        data = df.set_index("country")
        if country not in data.index:
            print(f"Error: {country} not found in dataset")
            return

        s = data.loc[country].apply(pd.to_numeric, errors="coerce")
        years = s.index.astype(int)

        plt.plot(years, s.values, label=country)
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
