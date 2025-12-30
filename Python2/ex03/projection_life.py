import matplotlib.pyplot as plt
import pandas as pd

from load_csv import load


def convert_population(value):
    """
    Convert strings like '127k', '29M' to numbers.
    """
    if pd.isna(value):
        return float('nan')
    s = str(value).strip()
    
    if s.endswith('M'):
        return float(s[:-1]) * 1_000_000
    elif s.endswith('k'):
        return float(s[:-1]) * 1_000
    else:
        return pd.to_numeric(s, errors="coerce")


def main() -> None:
    """
    Plot life expectancy vs GDP per person for the year 1900.
    """
    try:
        year = "1900"

        gdp_df = load(
            "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
        life_df = load("../life_expectancy_years.csv")
        if gdp_df is None or life_df is None:
            return
        if "country" not in gdp_df.columns or "country" not in life_df.columns:
            return
        if year not in gdp_df.columns or year not in life_df.columns:
            print(f"Error: year {year} not found")
            return

        gdp = gdp_df.set_index("country")[year]
        life = life_df.set_index("country")[year]
        gdp = gdp.apply(convert_population)
        life = pd.to_numeric(life, errors="coerce")

        merged = pd.concat([gdp, life], axis=1).dropna()
        if merged.empty:
            print(f"Error: no valid data for year {year}")
            return
        plt.scatter(merged.iloc[:, 0], merged.iloc[:, 1], label=year)
        plt.title("Life expectancy vs GDP per person")
        plt.xlabel("GDP per person")
        plt.ylabel("Life expectancy")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
