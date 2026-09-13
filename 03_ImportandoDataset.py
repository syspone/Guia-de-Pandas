# =============================================================================
# Autor.........: Cristian Matias de Souza
# Cargo/Nível...: Analista de Dados (N3)
# Criado em.....: 12/09/2026 20:18
# Versão........: 1.0
# -----------------------------------------------------------------------------
# Descrição.....: 
# Dependências..: Python 3.14
# =============================================================================
import pandas as pd

# As opções precisam vir ANTES do print, senão não têm efeito
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

df_gaz = pd.read_csv("Dataset/GazPrice.csv", sep=",")
# print(df_gaz.head(200))                                                     # retorna apenas as linhas do atributo

# df_gaz.info()

print(type(df_gaz))

# Atributo
print(df_gaz.shape)

print(f'O Dataframe possui {df_gaz.shape[0]} linhas/observações/registros e {df_gaz.shape[1]} colunas/atributos/variaveis.')
