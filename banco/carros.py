from conexao import criar_conexao

conn = criar_conexao()
cursor = conn.cursor()

def criar_tabela():

    try:

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS carros (
                    id SERIAL PRIMARY KEY,
                    marca VARCHAR(30) NOT NULL,
                    modelo VARCHAR(30) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor VARCHAR(30) NOT NULL,
                    quilometragem REAL NOT NULL DEFAULT 0,
                    preco REAL NOT NULL,
                    vendido BOOLEAN NOT NULL DEFAULT FALSE
                    )
        """)

        conn.commit()
        print("Conectado com sucesso")

    except Exception as e:
        conn.rollback()
        print(f"Erro: {e}")

    finally:

        cursor.close()
        conn.close()