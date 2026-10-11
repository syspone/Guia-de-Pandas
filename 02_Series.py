# =============================================================================
# Autor.........: Cristian Matias de Souza
# Cargo/Nível...: Analista de Dados (N3)
# Criado em.....: 27/08/2026 06:25
# Versão........: 1.0
# -----------------------------------------------------------------------------
# Descrição.....: Estrutura de uma Series
# Dependências..: Python 3.14
# =============================================================================
import pandas as pd
from pip._internal.commands import index

# 1 - Criando estrutura Series
dados = [10, 20, 30, 40, 50]
series = pd.Series(dados)
print(series)

type(series)
print(type(series))


vendas_mensais = pd.Series(
    [2000, 2500, 3000, 2800, 3500, 4000, 4500, 5000, 4800, 5200, 6000, 7000],
    index=['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
)

print(vendas_mensais)

# 2 - Calculando media de vendas
media_vendas = vendas_mensais.mean()
print('=== Media de Vendas==')
print(media_vendas)

# 3 - Indentificando o mes com maior vendasd
mes_maior_vendas = vendas_mensais.idxmax()
print('=== Mes com Maior Vendas==')
print(mes_maior_vendas)

# 4 - Exibir as vendas acima da media
vendas_acima_media = vendas_mensais[vendas_mensais > media_vendas]
print('=== Media de Vendas acima de Maior Vendas==')
print(vendas_acima_media)

# 5 - Acessando Dados
print('==== Acessando Dados via Indice ====')
print(dados[0])
print(dados[1])
print(dados[2])

# 6 - Fatiamento (slicing): posicoes 1 ate 2 (o 3 nao entra)
print('==== Fatiamento dos Dados ====')
print(dados[1:3])

# 7 - Series com arrays Generalizados
print('==== Arrays Generalizados ====')
ex1 = pd.Series([0.25, 0.75, 1.0],
    index=['a', 'b', 'c'])
print(ex1)
print(ex1['a'])
print(ex1['b'])
print(ex1['c'])





