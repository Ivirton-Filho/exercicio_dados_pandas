#  Importações
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Configurações visuais
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

print("✅ Bibliotecas importadas com sucesso!")


# Criação do Dataset
np.random.seed(42)

produtos = {
    "Dom Casmurro":       ("Literatura", 35.90),
    "O Pequeno Príncipe": ("Infantil",   29.90),
    "Sapiens":             ("Ciências",   54.90),
    "Python para Dados":  ("Tecnologia", 89.90),
    "Clean Code":         ("Tecnologia", 95.00),
    "Harry Potter Vol.1": ("Fantasia",   49.90),
    "Atomic Habits":      ("Autoajuda",  44.90),
    "A Arte da Guerra":   ("Filosofia",  32.00),
    "Cosmos":             ("Ciências",   62.50),
    "Cem Anos de Solidão":("Literatura", 39.90),
}

vendedores = ["Ana Lima", "Carlos Mendes", "Bruno Costa", "Fernanda Rocha"]
regioes    = ["Sudeste", "Sul", "Nordeste", "Norte", "Centro-Oeste"]
datas      = pd.date_range("2024-01-01", "2024-06-30", periods=50)

nomes_prod = np.random.choice(list(produtos.keys()), 50)

dados = {
    "id_venda":   range(1, 51),
    "data":       datas.strftime("%Y-%m-%d"),
    "produto":    nomes_prod,
    "categoria":  [produtos[p][0] for p in nomes_prod],
    "quantidade": np.random.randint(1, 6, 50),
    "preco_unit": [produtos[p][1] for p in nomes_prod],
    "vendedor":   np.random.choice(vendedores, 50),
    "regiao":     np.random.choice(regioes, 50),
}

df = pd.DataFrame(dados)
df["total_venda"] = df["quantidade"] * df["preco_unit"]

# Salva como CSV
df.to_csv("vendas_livraria.csv", index=False)

print(f"✅ Dataset criado! Shape: {df.shape}")
print(f"   Colunas: {list(df.columns)}")
df.head()

#desafio 01 - calcule a evolução do faturamento mês a mês
df['data'] = pd.to_datetime(df['data'])

df['mes'] = df['data'].dt.month

faturamento_mes = df.groupby('mes')['total_venda'].sum().reset_index()
print(faturamento_mes)

#desafio 02 -Crie um gráfico de linha mostrando a tendência de vendas
plt.figure(figsize=(10, 6))
plt.plot(faturamento_mes['mes'], faturamento_mes['total_venda'], marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)

plt.title('Tendência de Faturamento Mensal (2024)', fontsize=16, fontweight='bold')
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Faturamento Total (R$)', fontsize=12)
plt.show()

# desafio 4 
# vendas que somam mais que 200 

vendas_altas = dataframe[dataframe['total_venda'] > 200]
print(f"Quantidade de vendas acima de R$200,00: {len(vendas_altas)}")

# analise quais categorias dominam as vendas de alto valor

categorias_altas = vendas_altas['categoria'].value_counts().reset_index()
categorias_altas.columns = ['categoria', 'quantidade']
print(categorias_altas)
