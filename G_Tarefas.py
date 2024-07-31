from app import *

criarsql = """CREATE TABLE tb_Gerenciador_de_Tarefas(
            N_IDTAREFAS INTEGER PRIMARY KEY AUTOINCREMENT,
            T_TAREFAS VARCHAR(30),
            B_TAREFA_REALIZADA BOOLEAN
        )"""

vcon = ConexaoBanco()
tabela_existe = check_table_exists(vcon, 'tb_Gerenciador_de_Tarefas')

if tabela_existe:
    print('\033[;33mA tabela já foi criada anteriormente')
    sl(3)
else:
    CriarTabela(vcon, criarsql)
    print('\033[;32mA tabela foi criada com sucesso')
    sl(3)

# executar programa
os.system('cls')
cabeçalho()
menu()
os.system('cls')
