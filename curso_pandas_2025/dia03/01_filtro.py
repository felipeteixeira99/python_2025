# %% 
import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()
# %%

brinquedo  = pd.DataFrame(
    {
        "nome": ['teo', 'nah', 'mah'],
        "idade": [32,35,14],
        "uf": ['sp', 'pr', 'rj']
    }
)

brinquedo

# Serie                        # Scalar
filtro = brinquedo['idade'] >= 18
filtro  = filtro.to_list()
filtro

brinquedo[filtro]
# %%

# valores maiores que 50 e menor que 100
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] < 100)
df[filtro]
# %%

# Valore igual a 100 ou 1
filtro = (df['QtdePontos'] == 1) | (df['QtdePontos'] == 100)
df[filtro]
# %%

filtro = (df['QtdePontos'] > 0) & (df['QtdePontos'] <= 50) & (df["DtCriacao"] >= '2025-01-01')
df[filtro]
# %%
