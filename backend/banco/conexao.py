import psycopg2

def criar_conexao():

    conexao = psycopg2.connect(
        database = "postgres",
        user = "postgres",
        password = "26a09b2003F#",
        host = "localhost",
        port = "5432",
    )
    
    return conexao
    