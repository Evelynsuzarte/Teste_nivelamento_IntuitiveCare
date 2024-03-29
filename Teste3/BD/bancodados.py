import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    connect_timeout=30
)

query = conexao.cursor()

query.execute("CREATE DATABASE IF NOT EXISTS testeIntuitiveCare")
query.execute("use testeIntuitiveCare")


# def estruturar_tabelas():
#     with open("Teste3/BD/demonstracoes.sql", "r") as script:
#         script_sql = script.read()
#         print(script_sql)
#         script_sql = script_sql.replace('\n', '').strip() 
#     query.execute(script_sql)

#     with open("Teste3/Relatorio_cadop.csv", "r", encoding="utf-8") as file:
#         linhas = file.readlines()[1:] 
#         dados = [linha.strip().split(';') for linha in linhas]
#         for linha in dados:
#             for i, dado in enumerate(linha):
#                 if dado == "":
#                     linha[i] = '" "'
#         #dados = [[valor.replace(';;', ' ') for valor in linha] for linha in dados]
#         #dados = [[valor.replace('"', ' ') for valor in linha] for linha in dados]

#     query_demonstracoes = "INSERT INTO demonstracoes (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     query.executemany(query_demonstracoes, dados)
#     # for linha in dados:
#     #     query.execute(f"INSERT INTO demonstracoes (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS) VALUES ({linha[0]}, {linha[1]}, {linha[2]}, {linha[3]}, {linha[4]}, {linha[5]}, {linha[6]}, {linha[7]}, {linha[8]}, {linha[9]}, {linha[10]}, {linha[11]}, {linha[12]}, {linha[13]}, {linha[14]}, {linha[15]}, {linha[16]}, {linha[17]}, {linha[18]}, {linha[19]})")


with open("Teste3/BD/operadoras_ativas.sql", "r") as script:
    script_sql = script.read()
    print(script_sql)
    #script_sql = script_sql.replace('\n', '').strip() 
query.execute(script_sql)

arquivos = ["1T2022", "2T2022", "3T2022", "4T2022", "1T2023", "2T2023", "3T2023"]
for nome in arquivos:
    with open(f"Teste3/{nome}.csv", "r", encoding="latin-1") as file:
        linhas = file.readlines()[1:] 
        dados = [linha.strip().split(';') for linha in linhas]
        dados = [[valor.replace('"', '') for valor in linha] for linha in dados]
        
    #print(f"INSERT INTO operacoes_ativas (DATA_OP, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL) VALUES ({linha[0]}, {linha[1]}, {linha[2]}, {linha[3]}, {linha[4]}, {linha[5]})")
  
    # for linha in dados:
    #     print(f"INSERT INTO demonstracoes (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS) VALUES ({linha[0]}, {linha[1]}, {linha[2]}, {linha[3]}, {linha[4]}, {linha[5]}, {linha[6]}, {linha[7]}, {linha[8]}, {linha[9]}, {linha[10]}, {linha[11]}, {linha[12]}, {linha[13]}, {linha[14]}, {linha[15]}, {linha[16]}, {linha[17]}, {linha[18]}, {linha[19]})\n\n")
    #     query.execute(f"INSERT INTO operacoes_ativas (DATA_OP, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL) VALUES ({linha[0]}, {linha[1]}, {linha[2]}, {linha[3]}, {linha[4]}, {linha[5]})")

    # Converter a lista de listas em uma lista de tuplas
        dados_tuplas = [tuple(linha) for linha in dados]

        # Executar a consulta usando executemany
        query.executemany("""
            INSERT INTO operacoes_ativas (
                DATA_OP, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, dados_tuplas)



conexao.commit()
query.close()
conexao.close()



