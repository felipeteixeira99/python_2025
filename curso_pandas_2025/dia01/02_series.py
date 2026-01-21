# %%
idades = [
    32,28,30,30,31,
    35,25,29,31,37,
    27,23,36,33,32
]

# %%
import pandas as pd

series_idades = pd.Series(idades)
series_idades

# %%

media_idades = series_idades.mean()
media_idades
var_idades = series_idades.var()
var_idades
sumary = series_idades.describe()
sumary

# %%
