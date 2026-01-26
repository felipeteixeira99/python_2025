# %%
import pandas as pd

df_clientes = pd.read_csv('../data/clientes.csv', sep=";")

df_clientes
# %%
df_clientes.head(10) # Primeiras linhas
# %%
df_clientes.tail(10) # Ultimas Linhas
# %%
df_clientes.sample(10) # Aleatorios
# %%

df_clientes
# %%
df_clientes.shape
# %%
df_clientes.columns
# %%
df_clientes.index
# %%
df_clientes.info()
# %%
df_clientes.info(memory_usage='deep')

# %%
type(df_clientes.dtypes)
# %%
df_clientes.dtypes["idCliente"]
# %%
