import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password=""
)

query = conexao.cursor()

query.execute("CREATE DATABASE IF NOT EXISTS testeIntuitiveCare")
query.execute("USE testeIntuitiveCare")

with open("Teste3/BD/demonstracoes.sql", "r") as script:
    script_sql = script.read()

query.execute(script_sql)

conexao.commit()
conexao.close()
