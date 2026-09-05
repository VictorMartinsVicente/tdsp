"""
Fase: Deployment (TDSP)

Script de scoring que carrega o modelo treinado (fase de Modeling) e gera previsões
de receita para o próximo mês, a partir de um conjunto de features de entrada.

Em um cenário real, este script rodaria em uma rotina agendada (ex.: no início de
cada mês), lendo as features mais recentes de cada loja diretamente do data warehouse
e publicando as previsões em uma tabela consumida pelo time de planejamento de compras
(ex.: um dashboard de Power BI).

Uso:
    python scoring.py --input novas_lojas.csv --output previsoes.csv

O arquivo de entrada deve ter as mesmas colunas de feature usadas no treinamento
(ver docs/data_dictionary.md e code/modeling/modelagem.ipynb):
    area_m2, meses_operacao, mes, teve_campanha, receita_lag_1, receita_lag_3,
    media_movel_3, receita_por_m2_lag1, regiao, tipo_loja
"""
import argparse
from pathlib import Path

import joblib
import pandas as pd

MODELO_PATH = Path(__file__).resolve().parent / "modelo_previsao_receita.joblib"

FEATURES = [
    "area_m2", "meses_operacao", "mes", "teve_campanha",
    "receita_lag_1", "receita_lag_3", "media_movel_3", "receita_por_m2_lag1",
    "regiao", "tipo_loja",
]


def gerar_exemplo_entrada(destino: Path) -> None:
    """Gera um CSV de exemplo com o formato esperado, a partir do dataset processado,
    para permitir testar o script sem depender de um sistema externo."""
    processed = Path(__file__).resolve().parents[2] / "data" / "processed" / "dataset_modelagem.parquet"
    df = pd.read_parquet(processed)
    exemplo = df.sample(5, random_state=42)[["loja_id"] + FEATURES]
    exemplo.to_csv(destino, index=False)
    print(f"Exemplo de entrada gerado em {destino}")


def prever(caminho_entrada: Path, caminho_saida: Path) -> None:
    modelo = joblib.load(MODELO_PATH)
    df = pd.read_csv(caminho_entrada)

    colunas_faltando = set(FEATURES) - set(df.columns)
    if colunas_faltando:
        raise ValueError(f"Colunas obrigatorias ausentes no arquivo de entrada: {colunas_faltando}")

    df["receita_prevista"] = modelo.predict(df[FEATURES])

    colunas_saida = [c for c in df.columns if c not in FEATURES]
    df[colunas_saida].to_csv(caminho_saida, index=False)
    print(f"Previsoes salvas em {caminho_saida}")
    print(df[colunas_saida].head())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scoring: previsao de receita mensal por loja")
    parser.add_argument("--input", type=str, help="CSV com as features de entrada")
    parser.add_argument("--output", type=str, default="previsoes.csv", help="CSV de saida com as previsoes")
    parser.add_argument("--gerar-exemplo", action="store_true",
                         help="Gera um CSV de exemplo (exemplo_entrada.csv) para teste do script")
    args = parser.parse_args()

    if args.gerar_exemplo:
        gerar_exemplo_entrada(Path("exemplo_entrada.csv"))
    elif args.input:
        prever(Path(args.input), Path(args.output))
    else:
        parser.print_help()
