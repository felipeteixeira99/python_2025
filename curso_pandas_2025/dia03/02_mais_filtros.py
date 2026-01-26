# %% 
import pandas as pd

df = pd.read_csv('../data/transacao_produto.csv', sep=';')
df
# %%

filtro = (df['IdProduto'] == 5) | (df['IdProduto'] == 11)
df[filtro]
# %%

df['IdProduto']

# %%
df['IdProduto'].isin([5,11])
# %%
