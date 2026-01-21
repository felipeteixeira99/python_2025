# %%
import pandas as pd

idades = [
    32,28,30,30,31,
    35,25,29,31,37,
    27,23,36,33,33
]

# %%

series_idades = pd.Series(idades)
series_idades

# %%

# Pegar o primeiro elemento de uma lista

idades[-1]
# %%

series_idades[0]
# %%
series_idades[-1]
# %%

series_idades = series_idades.sort_values()
series_idades

# %%
# Acesso ao elemento
series_idades.iloc[:5]

# %%

idades = [
    32,28,30,30,31,
    35,25,29,31,37,
    27,23,36,33,33
]

indexs = [
    "Teo", "Maria", "Jose", "Luiz", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda", 
    "Naty", "Nih", "Pedro", "Kozato", "Kozato"
]

series_idades = pd.Series(idades, index=indexs)
series_idades

# %%
series_idades["Teo"]
# %%
series_idades.iloc[0]
# %%

series_idades['Kozato']
series_idades.iloc[-1]
# %%

