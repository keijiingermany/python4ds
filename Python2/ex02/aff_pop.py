import matplotlib.pyplot as plt
import pandas as pd

from load_csv import load


def convert_population(value: str) -> float:
    """
    Convert population string (e.g., '127k', '29M') to float.
    """
    if pd.isna(value):
        return float('nan')
    if isinstance(value, (int, float)):
        return float(value)

    value = str(value).strip()
    if value.endswith('M'):
        return float(value[:-1]) * 1_000_000
    elif value.endswith('k'):
        return float(value[:-1]) * 1_000
    else:
        return float(value)


def main() -> None:
    """
    Compare population between two countries (1800-2050).
    """
    try:
        df = load("../population_total.csv")
        if df is None or "country" not in df.columns:
            return

        country_a = "Luxembourg"
        country_b = "Iceland"

        data = df.set_index("country")
        if country_a not in data.index or country_b not in data.index:
            print("Error: country not found")
            return

        years = [str(y) for y in range(1800, 2051)]

        sa = data.loc[country_a].reindex(years).apply(convert_population)
        sb = data.loc[country_b].reindex(years).apply(convert_population)

        x = list(range(1800, 2051))
        plt.plot(x, sa.values, label=country_a)
        plt.plot(x, sb.values, label=country_b)
        plt.title("Population comparison")
        plt.xlabel("Year")
        plt.ylabel("Population")

        # Format y-axis to show values in millions (M)
        def format_population(value, pos):
            if value >= 1_000_000:
                return f'{value/1_000_000:.0f}M'
            elif value >= 1_000:
                return f'{value/1_000:.0f}k'
            return f'{value:.0f}'

        from matplotlib.ticker import FuncFormatter
        plt.gca().yaxis.set_major_formatter(FuncFormatter(format_population))

        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
