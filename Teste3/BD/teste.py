with open("Teste3/Relatorio_cadop.csv", "r", encoding="utf-8") as file:
    linhas = file.readlines()[1:] 
    dados = [linha.strip().split(';') for linha in linhas]
    dados = [[valor.replace('"', '') for valor in linha] for linha in dados]


print(dados[1][0])