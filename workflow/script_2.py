
import pandas as pd

# --- file paths ---
input_csv = "../data/raw/gdp-data.csv"
output_csv = "../data/preprocessed/gdp-capita.csv"

# --- read the data ---
df = pd.read_csv(input_csv)
df = df.fillna(0)
# --- identify id columns (not years) ---
id_vars = ["geo", "name"]

# --- everything else is a year ---
value_vars = [c for c in df.columns if c not in id_vars]

# --- unpivot (melt) ---
tidy = df.melt(
    id_vars=id_vars,
    value_vars=value_vars,
    var_name="year",
    value_name="gdpcapita"
)

# --- optional cleanup ---
tidy["year"] = tidy["year"].astype(int)

# --- save ---
tidy.to_csv(output_csv, index=False)

print(f"Tidy CSV written to {output_csv}")

