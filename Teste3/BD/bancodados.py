import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
)

query = conexao.cursor()

query.execute("CREATE DATABASE IF NOT EXISTS testeIntuitiveCare")
query.execute("use testeIntuitiveCare")

with open("Teste3/BD/demonstracoes.sql", "r") as script:
    script_sql = script.read()
    print(script_sql)
    script_sql = script_sql.replace('\n', '').strip() 
query.execute(script_sql)

with open("Teste3/Relatorio_cadop.csv", "r", encoding="utf-8") as file:
    linhas = file.readlines()[1:] 
    dados = [linha.strip().split(';') for linha in linhas]
    for linha in dados:
        for i, dado in enumerate(linha):
            if dado == "":
                linha[i] = '" "'
    #dados = [[valor.replace(';;', ' ') for valor in linha] for linha in dados]
    #dados = [[valor.replace('"', ' ') for valor in linha] for linha in dados]


for linha in dados:
    print(linha)
    print(linha[2])
    print(f"INSERT INTO demonstracoes (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS) VALUES ({linha[0]}, {linha[1]}, {linha[2]}, {linha[3]}, {linha[4]}, {linha[5]}, {linha[6]}, {linha[7]}, {linha[8]}, {linha[9]}, {linha[10]}, {linha[11]}, {linha[12]}, {linha[13]}, {linha[14]}, {linha[15]}, {linha[16]}, {linha[17]}, {linha[18]}, {linha[19]})\n\n")
    query.execute(f"INSERT INTO demonstracoes (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS) VALUES ({linha[0]}, {linha[1]}, {linha[2]}, {linha[3]}, {linha[4]}, {linha[5]}, {linha[6]}, {linha[7]}, {linha[8]}, {linha[9]}, {linha[10]}, {linha[11]}, {linha[12]}, {linha[13]}, {linha[14]}, {linha[15]}, {linha[16]}, {linha[17]}, {linha[18]}, {linha[19]})")


conexao.commit()
query.close()
conexao.close()
