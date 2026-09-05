# Project Charter — Previsão de Vendas Mensais por Loja

*(Documento padrão da fase de Business Understanding do TDSP — Team Data Science Process, Microsoft)*

## Contexto de negócio

A rede de varejo (fictícia, dados sintéticos) opera múltiplas lojas físicas e quer melhorar o planejamento de compras e de equipe por loja. Hoje o planejamento é feito manualmente com base na média dos últimos 3 meses, o que gera erros grandes em lojas com sazonalidade forte.

## Objetivo do projeto

Construir um modelo que preveja a **receita mensal de cada loja** com 1 mês de antecedência, a partir de características da loja (tamanho, tipo, região) e de seu histórico recente de vendas e de campanhas promocionais.

## Métricas de sucesso

- **Métrica de modelo:** MAPE (erro percentual médio absoluto) abaixo de 12% no conjunto de teste.
- **Métrica de negócio:** redução do erro de planejamento de compras em relação ao método atual (média móvel simples de 3 meses), medida no mesmo período de teste.

## Papéis da equipe (estrutura padrão do TDSP)

| Papel | Responsabilidade neste projeto |
|---|---|
| Project Lead | Garante que o projeto entrega valor de negócio e está dentro do prazo |
| Solution Architect | Define a arquitetura de dados e a estrutura de pastas/pipeline (este repositório) |
| Data Scientist | Conduz exploração, engenharia de variáveis, modelagem e avaliação |
| Project Manager | Acompanha marcos e riscos do projeto |

*(Em um projeto de portfólio individual, uma mesma pessoa assume todos os papéis — mas a documentação segue o padrão de um projeto em equipe, que é o diferencial do TDSP frente a metodologias focadas em um único analista.)*

## Escopo e dados

- **Fonte de dados:** histórico sintético de vendas mensais por loja, características cadastrais das lojas e histórico de campanhas promocionais (todos os dados são sintéticos/gerados para este projeto de portfólio — nenhum dado real de empresa é utilizado).
- **Fora de escopo:** previsão em nível de produto/SKU (este projeto trabalha apenas em nível de loja/mês).

## Plano de marcos (milestones)

1. Aquisição e organização dos dados brutos (`code/data_acquisition`).
2. Exploração e limpeza dos dados (`code/data_exploration`).
3. Modelagem e avaliação (`code/modeling`).
4. Script de scoring para novas lojas/períodos (`code/deployment`).
5. Relatório final de encerramento (`docs/exit_report.md`).

## Riscos conhecidos

- Lojas muito novas (menos de 6 meses de histórico) têm poucos dados para gerar boas variáveis de lag — tratadas separadamente na fase de exploração.
- Mudanças estruturais no negócio (ex.: reforma de loja, mudança de bandeira) não são capturadas pelas variáveis disponíveis neste escopo.
