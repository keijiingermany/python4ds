import matplotlib.pyplot as plt
import pandas as pd
import sys

from ex00.load_csv import load

def convert_population_simple(value):
    """
    Simple conversion for strings like '127k', '29M' or plain numbers.
    - Removes commas, strips whitespace, handles k/K and m/M suffixes.
    - Returns float('nan') on failure.
    """
    if pd.isna(value):
        return float('nan')
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip().replace(',', '')
    if not s:
        return float('nan')
    try:
        suf = s[-1].lower()
        if suf == 'k':
            return float(s[:-1]) * 1_000
        if suf == 'm':
            return float(s[:-1]) * 1_000_000
        return float(s)
    except Exception:
        return float('nan')

def main() -> None:
    """
    test: understand pd.to_numeric and M/k conversion
    """
    df_pop = load("population_total.csv")
    df_life = load("life_expectancy_years.csv")
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    pop = df_pop.set_index("country")
    life = df_life.set_index("country")
    gdp = df_gdp.set_index("country")

    # ===== 数値変換 =====
    # GDP: may include 'k'/'M' suffixes in some years — use simple converter per-cell
    gdp = gdp.apply(lambda col: col.map(convert_population_simple))
    
    # Life: float 形式 → apply(pd.to_numeric) で大丈夫
    life = life.apply(pd.to_numeric, errors="coerce")
    
    # Population: M/k 形式 → 専用関数で処理 (per-cell)
    pop = pop.apply(lambda col: col.map(convert_population_simple))
    
    # ===== 確認: 年のデータをチェック =====
    year = sys.argv[1] if len(sys.argv) > 1 else "1900"
    print(f"\n=== Year {year} ===")
    # validate year exists in all dataframes
    if year not in pop.columns or year not in gdp.columns or year not in life.columns:
        available = sorted([c for c in gdp.columns if str(c).isdigit()])
        print(f"Error: year {year} not found in datasets")
        print("Available year columns (sample):", available[:10])
        return
    
    # ===== 3つをマージ（country index で自動的に結合） =====
    year_1900 = pd.concat([gdp[year], life[year], pop[year]], axis=1)
    year_1900.columns = ["gdp", "life_expectancy", "population"]
    print(year_1900.head(10))
    print(f"\nNon-NaN rows: {year_1900.notna().all(axis=1).sum()}")

    # ===== GDP Top 5 =====
    top5_gdp = year_1900.sort_values("gdp", ascending=False).head(50)
    print(f"\n=== Top 5 countries by GDP ({year}) ===")
    print(top5_gdp)

if __name__ == "__main__":
    main()

