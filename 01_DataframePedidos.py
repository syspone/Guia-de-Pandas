# =============================================================================
# Autor.........: Cristian Matias de Souza
# Cargo/Nível...: Analista de Dados (N3)
# Criado em.....: 25/08/2026 22:44
# Versão........: 1.1
# -----------------------------------------------------------------------------
# Descrição.....: leitura do arquivo Dataset/Pedidos.csv com pandas, usando pathlib
#                 para montar o caminho relativo ao próprio script.
# Dependências..: Python 3.14, pandas
# =============================================================================
from pathlib import Path

import pandas as pd

# Exibição: mostra todas as linhas/colunas sem truncar com "..."
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

# Diretório onde este script está (independe de onde ele for executado)
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Dataset"
ARQUIVO = DATA_DIR / "Pedidos.csv"

if not ARQUIVO.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {ARQUIVO}")


df = pd.read_csv(ARQUIVO, sep=",", encoding="utf-8")

print(f"Arquivo: {ARQUIVO.name} ({ARQUIVO.stat().st_size} bytes)")
print(f"Linhas: {len(df)} | Colunas: {list(df.columns)}")
print(df.to_string(index=False))

