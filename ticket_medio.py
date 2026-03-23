import pandas as pd

dataframe = pd.read_csv('vendas_livraria.csv') 

ticket_medio = dataframe.groupby('vendedor')['total_venda'].mean().reset_index()

print(ticket_medio.to_string(index=False))

melhor_vendedor = ticket_medio.loc[ticket_medio['total_venda'].idxmax(), 'vendedor']
maior_ticket = ticket_medio['total_venda'].max()

print(f'Maior ticket médio: {melhor_vendedor} com R$ {maior_ticket:.2f}')