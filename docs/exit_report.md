# Exit Report — Previsão de Vendas Mensais por Loja

*(Documento padrão da fase de Customer Acceptance do TDSP)*

## Resumo executivo

O projeto entregou um modelo de previsão de receita mensal por loja que **supera a baseline atual de negócio** (média móvel de 3 meses) e **atinge o critério de sucesso definido no Project Charter** (MAPE abaixo de 12%).

| Métrica | Baseline (média móvel 3m) | Modelo (RandomForest) |
|---|---|---|
| MAPE (conjunto de teste) | ~14,8% | ~8,4% |
| Critério de sucesso (MAPE < 12%) | Não atingia | **Atingido** |

*(Os valores exatos variam levemente a cada execução por aleatoriedade do split de dados sintéticos; a ordem de grandeza e a conclusão — modelo supera a baseline — são estáveis.)*

## O que foi entregue

1. **Documentação de projeto** (`docs/`): charter de negócio, dicionário de dados e este relatório de encerramento.
2. **Pipeline de dados reproduzível** (`code/data_acquisition/`, `code/data_exploration/`): da geração/ingestão dos dados brutos até um dataset limpo e documentado.
3. **Modelo treinado e avaliado** (`code/modeling/`): com engenharia de variáveis de série temporal por loja, comparação explícita contra a baseline de negócio, e análise de importância de variáveis.
4. **Script de scoring pronto para produção** (`code/deployment/scoring.py`): recebe um CSV de features e devolve as previsões, no formato que alimentaria uma rotina agendada mensal.

## Variáveis mais relevantes para a previsão

O histórico recente da própria loja (receita do mês anterior e média móvel de 3 meses) e a área de vendas foram os fatores mais importantes — resultado consistente com a expectativa de negócio e que dá confiança adicional ao modelo além da métrica agregada.

## Limitações conhecidas

- Lojas com menos de 6 meses de histórico foram excluídas da modelagem por falta de dados suficientes para gerar variáveis de lag confiáveis — precisam de uma estratégia específica (ex.: modelo baseado apenas em características cadastrais, sem histórico).
- O modelo não captura eventos estruturais fora dos dados disponíveis (reformas, mudança de bandeira, fechamento temporário).

## Recomendação de próximos passos

- Reavaliar o modelo periodicamente (retreinamento trimestral) à medida que novos meses de dados ficam disponíveis.
- Investigar uma abordagem específica para lojas novas (cold start).
- Integrar o script de `scoring.py` a uma rotina agendada, alimentando um dashboard de planejamento de compras.

## Aceite

Este relatório encerra formalmente o ciclo do TDSP para este projeto de portfólio, demonstrando a estrutura de documentação e entregáveis esperada de um projeto de ciência de dados conduzido em equipe segundo o Team Data Science Process da Microsoft.
