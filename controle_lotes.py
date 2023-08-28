import pandas as pd

linhas_validas = []


with open(r'C:\Users\Usuario\Documents\csv_teste\sicoob_2022_04_10_12_06_13-_1_.csv', 'r') as arquivo:

    for _ in range(9):
        next(arquivo)


    for linha in arquivo:
        campos = linha.strip().split()
        if len(campos) == 3:
            linhas_validas.append(campos)


df = pd.DataFrame(linhas_validas, columns=['DATA', 'HISTORICO', 'VALOR'])