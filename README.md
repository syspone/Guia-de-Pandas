# Pandas: Estudos e Análise de Dados

Repositório de estudos de **pandas** com Python: estruturas básicas (`Series`) e leitura/exibição de dados de pedidos a partir de um CSV.

## Autor

| | |
|---|---|
| **Nome** | Cristian Matias de Souza |
| **Cargo/Nível** | Analista de Dados (N3) |
| **E-mail** | [cmsouzaac@gmail.com](mailto:cmsouzaac@gmail.com) |
| **GitHub** | [github.com/cmsouzaac](https://github.com/cmsouzaac) |
| **LinkedIn** | [linkedin.com/in/cristiansouzaac](https://www.linkedin.com/in/cristiansouzaac/) |

## Estrutura do projeto

```
Pandas/
├── Dataset/
│   └── Pedidos.csv          # base de pedidos (2016–2017)
├── DataframePedidos.py      # leitura e exibição do Pedidos.csv
├── Series.py                # exemplos com pandas.Series
└── README.md
```

## Scripts

### `Series.py`

Exemplos introdutórios com `pd.Series`:

1. Criação de uma Series a partir de uma lista
2. Series com índice personalizado (vendas mensais de Jan a Dez)
3. Cálculo da média de vendas
4. Mês com maior venda (`idxmax`)
5. Filtro de meses com vendas acima da média

### `DataframePedidos.py`

Lê `Dataset/Pedidos.csv` com `pd.read_csv` e mostra quantas linhas e quais colunas o arquivo tem, além da tabela completa, sem truncar.
O caminho do arquivo é montado com `pathlib` a partir da pasta do próprio script, então ele funciona de qualquer diretório onde for executado.

## Dataset: `Pedidos.csv`

43 pedidos de eletrodomésticos entre jun/2016 e jun/2017.

| Coluna | Descrição | Exemplo |
|---|---|---|
| `DataPedido` | Data do pedido (`d-Mon-aaaa`) | `7-Jun-2016` |
| `Regiao` | Região do Brasil | `Nordeste` |
| `Estado` | Estado | `Pernambuco` |
| `Vendedor` | Nome do vendedor | `Tobias` |
| `Item` | Produto | `Geladeira` |
| `Unidades` | Quantidade vendida | `62` |
| `PrecoUnidade` | Preço unitário (R$) | `400.99` |

## Requisitos

- Python 3.14
- pandas 3.0

## Como executar

```bash
# criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# instalar dependências
pip install pandas

# executar os scripts
python Series.py
python DataframePedidos.py
```
