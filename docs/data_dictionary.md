# Dicionário de Dados

*(Documento padrão da fase de Data Understanding do TDSP)*

## `data/raw/lojas.csv`

| Coluna | Tipo | Descrição |
|---|---|---|
| `loja_id` | int | Identificador único da loja |
| `regiao` | string | Região geográfica da loja (Sudeste, Sul, Nordeste, Centro-Oeste, Norte) |
| `tipo_loja` | string | Porte/formato da loja (Shopping, Rua, Outlet) |
| `area_m2` | float | Área de vendas em metros quadrados |
| `meses_operacao` | int | Meses desde a inauguração da loja até o fim do período observado |

## `data/raw/vendas_mensais.csv`

| Coluna | Tipo | Descrição |
|---|---|---|
| `loja_id` | int | Identificador da loja (chave estrangeira para `lojas.csv`) |
| `ano_mes` | string (YYYY-MM) | Mês de referência da venda |
| `receita` | float | Receita total da loja no mês (variável-alvo) |
| `teve_campanha` | int (0/1) | Se houve campanha promocional ativa na loja naquele mês |

## `data/interim/vendas_limpo.parquet`

Resultado da fase de exploração: junção de `lojas.csv` + `vendas_mensais.csv`, com tratamento de valores ausentes e remoção de lojas com histórico insuficiente (< 6 meses).

## `data/processed/dataset_modelagem.parquet`

Resultado da fase de engenharia de variáveis: dataset final usado para treinar o modelo, incluindo variáveis derivadas (`receita_lag_1`, `receita_lag_3`, `media_movel_3`, `receita_por_m2`, etc.).
