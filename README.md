## Guia de Pandas

Este material apresenta os códigos dos meus estudos de **[pandas](https://pandas.pydata.org/)**, a biblioteca de análise de dados do Python, [disponível no GitHub](https://github.com/syspone/Guia-de-Pandas).

**Autor:** [Cristian Matias de Souza](https://www.linkedin.com/in/cristiansouzaac/) - [@syspone](https://github.com/syspone)

### Estrutura do projeto

```
Guia-de-Pandas/
├── Dataset/              # bases de dados usadas nos exemplos
│   ├── GazPrice.csv
│   └── Pedidos.csv
├── notebooks/            # aulas do curso, uma por notebook
│   ├── 01_DataframePedidos.ipynb
│   ├── 02_Series.ipynb
│   └── 03_ImportandoDataset.ipynb
├── requirements.txt
└── README.md
```

### Aulas

| Notebook | Conteúdo |
|---|---|
| [01 · DataFrame de Pedidos](notebooks/01_DataframePedidos.ipynb) | Leitura de um CSV com `read_csv`, caminhos com `pathlib` e exibição de um `DataFrame` |
| [02 · Series](notebooks/02_Series.ipynb) | Criação, índice personalizado, `mean`, `idxmax`, filtros, `loc`/`iloc` e fatiamento |
| [03 · Importando um Dataset](notebooks/03_ImportandoDataset.ipynb) | Datas com `parse_dates` e primeira inspeção: `type`, `shape`, `info()` e `head()` |

### Bases de dados

- [Pedidos.csv](Dataset/Pedidos.csv): 43 pedidos de eletrodomésticos entre jun/2016 e jun/2017.
- [GazPrice.csv](Dataset/GazPrice.csv): preços semanais de combustíveis da ANP por região, estado e produto (103 mil registros, desde 2004).

### Como executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Depois, abra os notebooks no PyCharm (selecionando o interpretador `.venv`) ou no VS Code. Para usar no navegador, instale também o JupyterLab (`pip install jupyterlab`) e rode `jupyter lab`.

<br>

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
