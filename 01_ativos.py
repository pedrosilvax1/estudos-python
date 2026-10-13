# Exercício 01 - lista de ativos e idade das máquinas
ano_atual = 2026

ativos = [
    {"maquina": "NB-001", "usuario": "ana", "ano_compra": 2019},
    {"maquina": "NB-002", "usuario": "bruno", "ano_compra": 2023},
    {"maquina": "DT-003", "usuario": "carla", "ano_compra": 2020},
]

for ativo in ativos:
    idade = ano_atual - ativo["ano_compra"]
    if idade >= 5:
        status = "TROCAR"
    else:
        status = "ok"
    print(f'{ativo["maquina"]} ({ativo["usuario"]}): {idade} anos - {status}')