from app import *

criarsql = """CREATE TABLE tb_Gerenciador_de_Tarefas(
            N_IDTAREFAS INTEGER PRIMARY KEY AUTOINCREMENT,
            T_TAREFAS VARCHAR(30),
            B_TAREFA_REALIZADA BOOLEAN
        )"""

vcon = ConexaoBanco()
CriarTabela(vcon, criarsql)
vcon.close()
sl(1)
start = cabeçalho()
section = menu()
os.system('cls')