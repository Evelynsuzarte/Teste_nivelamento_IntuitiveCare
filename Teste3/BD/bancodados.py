import mysql.connector

def tabela_demonstracoes_script(config):
    conexao = mysql.connector.connect(**config)
    query = conexao.cursor()
    query.execute("use testeIntuitiveCare")
    with open("Teste3/BD/demonstracoes.sql", "r") as script:
        script_sql = script.read()
        print(script_sql)
        script_sql = script_sql.replace('\n', '').strip() 
    query.execute(script_sql)
    conexao.commit()
    query.close()
    conexao.close()

def tabela_demonstracoes_csv(config):
    conexao = mysql.connector.connect(**config)
    query = conexao.cursor()
    query.execute("use testeIntuitiveCare")
    with open("Teste3/Relatorio_cadop.csv", "r", encoding="utf-8") as file:
        linhas = file.readlines()[1:] 
        dados = [linha.strip().split(';') for linha in linhas]
        for linha in dados:
            for i, dado in enumerate(linha):
                if dado == "":
                    linha[i] = '" "'

    query_demonstracoes = "INSERT IGNORE INTO demonstracoes (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    query.executemany(query_demonstracoes, dados)
    conexao.commit()
    query.close()
    conexao.close()

#---------------------------------------------------------------------------------
    
def tabela_operadorasAtivas_script(config):
    conexao = mysql.connector.connect(**config)
    query = conexao.cursor()
    query.execute("use testeIntuitiveCare")

    with open("Teste3/BD/operadoras_ativas.sql", "r") as script:
        script_sql = script.read()
        print(script_sql)
        
    query.execute(script_sql)
    conexao.commit()
    query.close()
    conexao.close()

def tabela_operadorasAtivas_csv(arquivos, config, batch_size=10000):
    conexao = mysql.connector.connect(**config)
    query = conexao.cursor()
    query.execute("use testeIntuitiveCare")

    for nome in arquivos:
        with open(f"Teste3/{nome}.csv", "r", encoding="utf-8") as file:
            linhas = file.readlines()[1:]
            for i in range(0, len(linhas), batch_size):
                batch = linhas[i:i + batch_size]
                dados = [linha.strip().split(';') for linha in batch]
                dados = [[valor.replace('"', '') for valor in linha] for linha in dados]
                dados_tuplas = [tuple(linha) for linha in dados]

                query.executemany("""
                    INSERT INTO operacoes_ativas (
                        DATA_OP, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL
                    ) VALUES (%s, %s, %s, %s, %s, %s)
                """, dados_tuplas)

                conexao.commit()

    query.close()
    conexao.close()  

#----------------------------------------------------    

def querys_analiticas(config):
    conexao = mysql.connector.connect(**config)
    query = conexao.cursor()
    query.execute("use testeIntuitiveCare")
    with open("Teste3/BD/querys_analiticas.sql", "r", encoding="utf-8") as script:
        script_sql = script.read()
        script_result = script_sql.strip().split(';')
    for comando in script_result:
            print(comando)
            query.execute(comando)
            conexao.commit()

            resultados = query.fetchall()

            for resultado in resultados:
                print(resultado)

    #conexao.commit()
    query.close()
    conexao.close()

#----------------------------------------------------            
try:
    arquivos = ["3T2022", "4T2022","2T2023", "3T2023"]
    config = {"host": "127.0.0.1","user": "root","password": "","connect_timeout": 5000}
    conexao = mysql.connector.connect(**config)

    query = conexao.cursor()
    query.execute("CREATE DATABASE IF NOT EXISTS testeIntuitiveCare")
    
    tabela_demonstracoes_script(config)
    tabela_demonstracoes_csv(config)
    tabela_operadorasAtivas_script(config)
    tabela_operadorasAtivas_csv(arquivos,config)
    querys_analiticas(config)
    
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao MySQL: {err}")
finally:
    if 'conexao' in locals() and conexao.is_connected():
        query.close()
        conexao.close()



