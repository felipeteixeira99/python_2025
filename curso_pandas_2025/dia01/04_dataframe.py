# %%
import pandas as pd

idades = [
    32,28,30,30,31,
    35,25,29,31,37,
    27,23,36,33,35
]

nomes = [
    "Teo", "Maria", "Jose", "Luiz", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda", 
    "Naty", "Nih", "Pedro", "Kozato", "Kozato"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
# %%

df = pd.DataFrame()
# %%
df["idades"] = series_idades
df["nomes"] = series_nomes
df
# %%
df["nomes"]

# %%
df["idades"]
# %%
df["idades"]
df["nomes"]
# %%
df.iloc[0]
# %%
df.iloc[0]["nomes"]

# %%
df.iloc[-1]["nomes"]
# %%
