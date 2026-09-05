"""
Fase: Data Acquisition (TDSP)

Gera os dados brutos sinteticos deste projeto de portfolio, simulando o histórico
de vendas mensais de uma rede de lojas de varejo. Em um projeto real, este script
seria substituído pela extração de um data warehouse / ERP da empresa.

Saídas:
    data/raw/lojas.csv
    data/raw/vendas_mensais.csv
"""
import numpy as np
import pandas as pd
from pathlib import Path

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def gerar_lojas(n_lojas: int = 60) -> pd.DataFrame:
    regioes = np.random.choice(
        ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"],
        size=n_lojas, p=[0.40, 0.20, 0.20, 0.12, 0.08],
    )
    tipos = np.random.choice(["Shopping", "Rua", "Outlet"], size=n_lojas, p=[0.5, 0.35, 0.15])
    area_m2 = np.clip(np.random.normal(250, 90, size=n_lojas), 60, 900).round(1)
    meses_operacao = np.random.randint(3, 60, size=n_lojas)

    return pd.DataFrame({
        "loja_id": np.arange(1, n_lojas + 1),
        "regiao": regioes,
        "tipo_loja": tipos,
        "area_m2": area_m2,
        "meses_operacao": meses_operacao,
    })


def gerar_vendas_mensais(lojas: pd.DataFrame, n_meses: int = 36) -> pd.DataFrame:
    meses = pd.period_range("2023-01", periods=n_meses, freq="M")
    registros = []

    peso_regiao = {"Sudeste": 1.15, "Sul": 1.05, "Nordeste": 0.95, "Centro-Oeste": 0.90, "Norte": 0.85}
    peso_tipo = {"Shopping": 1.20, "Rua": 0.95, "Outlet": 0.85}

    for _, loja in lojas.iterrows():
        base = loja["area_m2"] * 45 * peso_regiao[loja["regiao"]] * peso_tipo[loja["tipo_loja"]]
        idade_loja = 0

        for i, mes in enumerate(meses):
            if idade_loja > loja["meses_operacao"]:
                continue  # loja ainda nao existia neste periodo (calculo aproximado)

            sazonalidade = 1 + 0.18 * np.sin(2 * np.pi * (mes.month / 12) + 1.4)
            tendencia = 1 + 0.004 * i
            campanha = np.random.choice([0, 1], p=[0.75, 0.25])
            efeito_campanha = 1.12 if campanha else 1.0
            ruido = np.random.normal(1.0, 0.08)

            receita = base * sazonalidade * tendencia * efeito_campanha * ruido
            registros.append({
                "loja_id": loja["loja_id"],
                "ano_mes": str(mes),
                "receita": round(max(receita, 1000), 2),
                "teve_campanha": campanha,
            })
            idade_loja += 1

    return pd.DataFrame(registros)


if __name__ == "__main__":
    lojas = gerar_lojas()
    vendas = gerar_vendas_mensais(lojas)

    lojas.to_csv(RAW_DIR / "lojas.csv", index=False)
    vendas.to_csv(RAW_DIR / "vendas_mensais.csv", index=False)

    print(f"lojas.csv gerado com {len(lojas)} lojas.")
    print(f"vendas_mensais.csv gerado com {len(vendas)} registros loja-mes.")
