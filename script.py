# 1. Criar e Conectar ao Banco de Dados
import sqlite3

# Conectar ao banco (ou criar, caso não exista)
conexao = sqlite3.connect("meu_banco.db")

# Criar um cursor para executar comando SQL
cursor = conexao.cursor()

# 2. Criar uma Tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGAR,
        turma TEXT
    )
""")

# Salvar as alterações
conexao.commit()

# 3. Inserir Dados
cursor.execute("""
    INSERT INTO alunos (nome, idade, turma)
               VALUES (?, ?, ?)
""", ("Carlos Silva", 12, "Sub-13"))

# Salvar as alterações
conexao.commit()

# 4. Buscar Dados
cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall() # Retorna todos os registros

for aluno in alunos:
    print(aluno)

# 5. Atualizar Dados
cursor.execute("""
    UPDATE alunos
    SET idade = ?
    WHERE nome = ?               
""", (13, "Carlos Silva"))

conexao.commit()

# 6. Excluir Dados
cursor.execute(""" 
    DELETE FROM alunos
    WHERE nome = ?
""", ("Carlos Silva",))

# 7. Fechar a Conexão
conexao.close()