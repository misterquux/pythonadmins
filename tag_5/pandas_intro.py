"""
Pandas Intro
"""

from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent / "active_volcanos.csv"

df = pd.read_csv(DATA)
print(df.head(5))  # die ersten 5 Zeilen
print(df.info())

# eine Spalte ausgeben
print(list(df.Country.unique()))  # df["Country"]

# Datensätze filtern
df_italy = df[df["Country"] == "Italy"]
df_italy.to_csv(Path(__file__).parent / "active_volcanos2.csv")

# Filter mit zwei Bedinungen. Country ist Italien und PEI soll >= 4 sein
print(df[(df["Country"] == "Italy") & (df["PEI"] >= 4)])

print("Wie viele Vulkane pro Land?", df["Country"].value_counts())

print(df.head(2))
