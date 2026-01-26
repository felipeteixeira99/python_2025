# %% 
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.shape
# %%

df.shape

# %%
df.info(memory_usage='deep')


# %%
df = df.rename(columns={"QtdePontos": "qtdpontos"})
df
# %%

df['IdCliente']

# %%
df[['IdCliente']]

# %%
df[['IdCliente', 'IdTransacao']]
# %%
