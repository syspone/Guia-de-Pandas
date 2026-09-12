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

# 3 - Indentificando o mes com maior vendas
mes_maior_vendas = vendas_mensais.idxmax()
print('=== Mes com Maior Vendas==')
print(mes_maior_vendas)

# 4 - Exibir as vendas acima da media
vendas_acima_media = vendas_mensais[vendas_mensais > media_vendas]
print('=== Media de Vendas acima de Maior Vendas==')
print(vendas_acima_media)





