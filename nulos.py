#importações
import pandas as pd
import numpy as np

df = pd.read_csv('vendas_livraria.csv')

novas_linhas = pd.DataFrame({
    "id_venda":   [None]*5,
    "data":       [None]*5,
    "produto":    [None]*5,
    "categoria":  [None]*5,
    "quantidade": [np.nan]*5,
    "preco_unit": [np.nan]*5,
    "vendedor":   [None]*5,
    "regiao":     [None]*5,
    "total_venda":[np.nan]*5
})

# Adicionando ao DataFrame original
df = pd.concat([df, novas_linhas], ignore_index=True)

# Exibindo as informações
print("✅ 5 linhas nulas adicionadas!")
print(df)

# Verificando a quantidade de valores nulos por coluna
print("\nQuantidade de valores nulos por coluna:")
print(df.isnull().sum())

#removendo os valores nulos
df_limpo = df.dropna()
print("✅ Valores nulos removidos!")
print(df_limpo.info())
print('\n🧹Resultado após limpeza:')
print(df_limpo)
