# Exercício 01 - lista de ativos e idade das máquinas
ano_atual = 2026

ativos = [
    {"maquina": "NB-001", "usuario": "ana", "ano_compra": 2019},
    {"maquina": "NB-002", "usuario": "bruno", "ano_compra": 2023},
    {"maquina": "DT-003", "usuario": "carla", "ano_compra": 2020},
    {"maquina": "DT-004", "usuario": "pedro", "ano_compra": 2020},
]

qtd_trocar = 0

for ativo in ativos:
    idade = ano_atual - ativo["ano_compra"]
    if idade >= 5:
        status = "TROCAR"
        qtd_trocar += 1   
    else:
        status = "ok"
    print(f'{ativo["maquina"]} ({ativo["usuario"]}): {idade} anos - {status}')      

print(f"Total para trocar: {qtd_trocar}")   