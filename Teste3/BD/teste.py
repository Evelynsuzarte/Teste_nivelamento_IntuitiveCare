arquivos = ["1T2022", "2T2022", "3T2022", "4T2022", "1T2023", "2T2023", "3T2023"]
for nome in arquivos:
    with open(f"Teste3/{nome}.csv", "r", encoding="latin-1") as file:
        linhas = file.readlines()[1:] 
        dados = [linha.strip().split(';') for linha in linhas]
        dados = [[valor.replace('"', '') for valor in linha] for linha in dados]

print(dados[1])
