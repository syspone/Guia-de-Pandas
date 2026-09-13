# =============================================================================
# Autor.........: Cristian Matias de Souza
# Cargo/Nível...: Analista de Dados (N3)
# Criado em.....: 12/09/2026 21:20
# Versão........: 1.0
# -----------------------------------------------------------------------------
# Descrição.....: 
# Dependências..: Python 3.14
# =============================================================================
import pandas as pd

personagens_df = pd.DataFrame({
    'nome': ['Cristian', 'Jessica Fernanda', 'Bruna'],
    'idade' : [39, 36, 30],
    'peso': [96.5, 50.5, 60.6],
    'eh_jedi': [True, False, True]
})
print(personagens_df)