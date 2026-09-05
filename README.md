# TDSP na prática: previsão de vendas mensais por loja

Projeto de portfólio demonstrando a aplicação do **TDSP** (Team Data Science Process, da Microsoft) em um problema de varejo: prever a receita mensal de cada loja de uma rede, para apoiar o planejamento de compras e de equipe.

> **Sobre os dados:** todos os dados (lojas e histórico de vendas) são **sintéticos**, gerados com semente fixa por `code/data_acquisition/gerar_dados_brutos.py`. Nenhum dado real ou confidencial de empresa é utilizado.

## O que é o TDSP

O TDSP é a metodologia de ciência de dados da Microsoft, com um foco diferente das demais metodologias deste portfólio: em vez de descrever apenas o fluxo analítico, o TDSP define uma **estrutura padronizada de projeto, papéis de equipe e artefatos de documentação**, pensada para projetos conduzidos por múltiplas pessoas ao longo do tempo — não apenas um notebook isolado.

As 5 etapas do ciclo de vida do TDSP, refletidas neste repositório:

1. **Business Understanding** → [`docs/project_charter.md`](docs/project_charter.md)
2. **Data Acquisition and Understanding** → [`code/data_acquisition/`](code/data_acquisition/) e [`code/data_exploration/`](code/data_exploration/)
3. **Modeling** → [`code/modeling/`](code/modeling/)
4. **Deployment** → [`code/deployment/`](code/deployment/)
5. **Customer Acceptance** → [`docs/exit_report.md`](docs/exit_report.md)

## Estrutura do repositório (padrão oficial do TDSP)

```
tdsp/
├── docs/
│   ├── project_charter.md      # Objetivo de negócio, métricas de sucesso, papéis da equipe
│   ├── data_dictionary.md      # Descrição de cada tabela/coluna
│   └── exit_report.md          # Relatório final de encerramento
├── data/
│   ├── raw/                    # Dados brutos gerados (lojas.csv, vendas_mensais.csv)
│   ├── interim/                # Dados limpos/unidos, antes da engenharia de variáveis
│   └── processed/              # Dataset final pronto para modelagem
├── code/
│   ├── data_acquisition/       # Geração/ingestão dos dados brutos
│   ├── data_exploration/       # Notebook de exploração e limpeza
│   ├── modeling/                # Notebook de engenharia de variáveis, treino e avaliação
│   └── deployment/              # Script de scoring pronto para produção
├── requirements.txt
└── README.md
```

## Resultado principal

O modelo (`RandomForestRegressor`) treinado em `code/modeling/modelagem.ipynb` atingiu **MAPE ≈ 8,4%** no conjunto de teste, superando a baseline atual do negócio (média móvel de 3 meses, MAPE ≈ 14,8%) e o critério de sucesso definido no *project charter* (MAPE < 12%). Detalhes completos em [`docs/exit_report.md`](docs/exit_report.md).

## Como rodar o pipeline completo

```bash
pip install -r requirements.txt

# 1. Gerar os dados brutos sintéticos
python code/data_acquisition/gerar_dados_brutos.py

# 2. Rodar a exploração (gera data/interim/vendas_limpo.parquet)
jupyter nbconvert --to notebook --execute --inplace code/data_exploration/exploracao.ipynb

# 3. Rodar a modelagem (gera data/processed/ e o modelo treinado)
jupyter nbconvert --to notebook --execute --inplace code/modeling/modelagem.ipynb

# 4. Testar o script de scoring
cd code/deployment
python scoring.py --gerar-exemplo
python scoring.py --input exemplo_entrada.csv --output previsoes.csv
```

## Autor

Victor Martins Vicente — projeto de portfólio para demonstração prática da metodologia TDSP.
