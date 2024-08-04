import sqlite3
from sqlite3 import Error
from time import sleep as sl
import os

def cabeçalho(): 
    os.system('cls')   
    print('\033[31m~~'*23)
    print('\033[1;36m  Seja Bem Vindos Ao Gerenciador de Tarefas:\033[m')
    print('\033[31m~~'*23)

def menu(vcon):    
    opcao = 0
    while opcao != 6:
        os.system('cls')     
        cabeçalho()
        print('\033[35m O Que Desejas Fazer:')
        print('\033[31m~~'*15)        
        print('''\033[m
    1\033[34m=> \033[1;32mAdicionar Tarefas\033[m
    2\033[34m=> \033[1;32mVisualizar Tarefas\033[m
    3\033[34m=> \033[1;32mAtualizar Tarefas\033[m
    4\033[34m=> \033[1;32mTarefas Concluídas\033[m
    5\033[34m=> \033[1;32mRemover Tarefas\033[m
    6\033[34m=> \033[1;32mFechar Programa\033[m
    ''')
        opcao = int(input('\033[;36mDigite a opção Desejada\033[;32m  \033[m'))
        if opcao == 1:
            AdicionarTarefas()
        elif opcao == 2:
            VisualizarTarefas()
        elif opcao == 3:
            AtualizarTarefas()
        elif opcao == 4:
            TarefasConcluídas()
        elif opcao == 5:
            RemoverTarefas()
        elif opcao == 6:
            print('\033[;31mfechando Gerenciador de tarefas\033[;m')
            sl(2)
            print('\033[1;31mFim do programa!\033[1;32m Volte Sempre\033[;m')
            sl(3) 
            os.system('cls')
        else:
            print('\033[;31mOpção invalida digite somente números no intervalo de [\033[1;33m1/6\033[;31m] \033[;m')
            os.system('pause')
        os.system('cls')

def query(conexao, sql, tarefa):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print(f'\033[;35m{tarefa} \033[;32minserido no BBD com sussesso')
        conexao.close() 

def consultar(conexao, sql):
        c=conexao.cursor()
        c.execute(sql)
        resultado = c.fetchall()
        return resultado

def AdicionarTarefas():
    os.system('cls')
    vcon = ConexaoBanco()
    tarefa = input('\033[;34mDigite o nome da tarefa a ser criada\033[1;32m \033[;m').strip().title()
    res = tarefa_existe(vcon, tarefa)
    if res != True:        
        isql = "INSERT INTO tb_Gerenciador_de_Tarefas(T_TAREFAS)VALUES('"+ tarefa +"')"
        query(vcon, isql, tarefa)
        print(f'\033[;35m{tarefa} \033[;32minserido no BBD com sussesso\033[;m') 
        pergunta = input('\033[;34mDeseja Criar Mais Alguma Tarefa?\033[;m ').strip().upper()
        validacao(pergunta)

def validacao(pergunta): 
    while pergunta != 'N':
        if pergunta not in 'SN':                    
            pergunta = input('\033[;31m Opção inválida!\033[;33m Deseja Criar Mais Alguma Tarefa?\033[;m ').strip().upper()
        elif pergunta == 'S':
            vcon = ConexaoBanco()
            tarefa = input('\033[;34mDigite o nome da tarefa a ser criada\033[1;32m \033[;m').strip().title()
            res = tarefa_existe(vcon, tarefa)
            if res != True:        
                isql = "INSERT INTO tb_Gerenciador_de_Tarefas(T_TAREFAS)VALUES('"+ tarefa +"')"
                query(vcon, isql, tarefa)
                print(f'\033[;35m{tarefa} \033[;32minserido no BBD com sussesso\033[;m') 
                pergunta = input('\033[;34mDeseja Criar Mais Alguma Tarefa?\033[;m ').strip().upper()
            else:
                pergunta = input(f'\033[;33mA tarefa \033[1;36m{tarefa} \033[;33mjá existe em seu banco de dados. Deseja criar outra tarefa: \033[;m').strip().upper()

def tarefa_existe(vcon, tarefa):
    # Função para verificar se a tarefa já existe no banco de dados
    cursor = vcon.cursor()
    cursor.execute("SELECT 1 FROM tb_Gerenciador_de_Tarefas WHERE T_TAREFAS = ?", (tarefa,))
    return cursor.fetchone() is not None 

def VisualizarTarefas():
    vcon = ConexaoBanco()
    rsql = "SELECT * FROM tb_Gerenciador_de_Tarefas"
    res = consultar(vcon, rsql)
    if res:# Verifica se a lista de resultados não está vazia
        for r in res:
            print(f'\033[;35m{r}') 
        vcon.close()      
        os.system('pause')  
        sl(2)        
    else:
        print('\033[;33mAinda não existe lançamentos no seu banco de dados\033[;m')
        os.system('pause')
    vcon.close() 
    sl(2) 
    os.system('cls') 

def AtualizarTarefas():
    vcon = ConexaoBanco()
    rsql = "SELECT * FROM tb_Gerenciador_de_Tarefas"
    res = consultar(vcon, rsql)
    for r in res:
        print(f'\033[;37m{r}')
    id_escolhido = input('\033[;36mDigite o \033[1;31mID\033[;36m da tarefa que deseja atualizar?\033[;m ') 
    asql = "UPDATE tb_Gerenciador_de_Tarefas SET B_TAREFA_REALIZADA = ? WHERE N_IDTAREFAS= ?"
    parametros = ('True', id_escolhido)
    atualizarBanco(vcon, asql, parametros)
    pergunta = input('\033[36mDeseja atualizar mais alguma tarefas [S/N]').strip().upper()
    confirm_atualizar_tarefa(pergunta)
    vcon.close()

def atualizarBanco(conexcao, sql, parametro):
    try:
        c = conexcao.cursor()
        c.execute(sql, parametro)
        conexcao.commit()
        print('\033[35mO Banco de Dados foi atualizado com sussesso:')
    except Error as ex:
        print(ex)

def confirm_atualizar_tarefa(pergunta):
    while pergunta not in 'SN':
        pergunta = input('\033[;31mOpção Inválida Digite somente [S/N]\033[;m').strip().upper()
    while pergunta == 'S':
        vcon = ConexaoBanco()
        rsql = "SELECT * FROM tb_Gerenciador_de_Tarefas"
        res = consultar(vcon, rsql)
        for r in res:
            print(f'\033[;37m{r}')
        id_escolhido = input('\033[;36mDigite o \033[1;31mID\033[;36m da tarefa que deseja atualizar?\033[;m ') 
        asql = "UPDATE tb_Gerenciador_de_Tarefas SET B_TAREFA_REALIZADA = ? WHERE N_IDTAREFAS= ?"
        parametros = ('True', id_escolhido)
        atualizarBanco(vcon, asql, parametros) 
        pergunta = input('\033[;36mDeseja atualizar mais alguma tarefas [S/N]').strip().upper() 
        vcon.close()                 
    if pergunta == 'N':
        print('\033[;35mAtualizações finalizadas com sussesso\033[;m')    
    os.system('pause')
    sl(2)
    os.system('cls')

def TarefasConcluídas():
    vcon = ConexaoBanco()
    rsql = "SELECT * FROM tb_Gerenciador_de_Tarefas"
    res = consultar(vcon, rsql)
    for r in res:
        if r[2] == 'True':
            print(f'\033[;33m{r}')

    os.system('pause')
    sl(2)
    os.system('cls')

def RemoverTarefas():
    pergunta = input('\033[;33mDigite o nome da tarefa que Deseja Escluir:\n\033[;32mSe digitar a palavra \033[1;36mtodas\033[;32m o banco de dados será limpo\033[;m ').strip().title()
    condicao_para_exclusao(pergunta)

def condicao_para_exclusao(pergunta):
    vcon = ConexaoBanco()
    if pergunta == 'Todas':
        res = input('\033[;35mO banco de dados será todo deletado! Tem certeza que quer fazer isso? [\033[;31mS/N\033[;35m]\033[1;37m \033[;m').strip().upper()
        while res not in 'SN':
            res = input('\033[;34mOpcão invalida! Digite [\033[;31mS/N\033[;34m]\033[1;37m \033[;m').strip().upper()
        if res == 'S':
            esql = "DELETE FROM tb_Gerenciador_de_Tarefas" 
            query(vcon, esql, pergunta)
            print('\033[;35mTodas tarefas excluídas com Sussesso\033[;m')
        elif res == 'N':
            print('\033[;32mCancelado a exclusão das tarefas\033[;m')
        sl(3)
        vcon.close()

    else:
        res = tarefa_existe(vcon, pergunta)
        if res == True:
            esql = "DELETE FROM tb_Gerenciador_de_Tarefas WHERE T_TAREFAS='"+pergunta+"'" 
            query(vcon, esql, pergunta)
            resp = input(f'\033[;31mA tarefa \033[1;33m{pergunta}\033[;31m foi excluída com sussesso: Deseja excluir outra tarefa?\033[;35m \033[;m').strip().upper()
            confirmar_exclusao(resp)
        else:
            resp = input(f'\033[;36mA tarefa \033[;37m{pergunta}\033[;36m não existe no banco de dados. Deseja excluir outra tarefa?\033[;35m \033[;m').strip().upper()
            confirmar_exclusao(resp)
    vcon.close()                    
    sl(2)
    os.system('cls')

def confirmar_exclusao(resp):
    while resp not in 'SN':
        resp = input('\033[;34mOpcão invalida! Digite [\033[;31mS/N\033[;34m]\033[1;37m \033[;m').strip().upper()
    if resp != 'N':
        pergunta = input('\033[;33mDigite o nome da tarefa que Deseja Escluir:\n\033[;32mSe digitar a palavra \033[1;36mtodas\033[;32m o banco de dados será limpo\033[;m ').strip().title()
        condicao_para_exclusao(pergunta)

def FecharPrograma():
    print('\033[;31mfechando Gerenciador de tarefas\033[;m')
    sl(1.5)
    print('\033[1;31mFim do programa!\033[1;32m Volte Sempre\033[;m')
    sl(3)
    os.system('cls')

def ConexaoBanco():
    caminho = 'F:\\area de trabalho\\destava-dev\\gerenciador de tarefas\\Gerenciador de Tarefas.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

def ConexaoBanco():
    caminho = 'F:\\area de trabalho\\destava-dev\\gerenciador de tarefas\\Gerenciador de Tarefas.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
# Verificar se a tabela existe
def check_table_exists(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    return cursor.fetchone() is not None

def CriarTabela(conexcao, sql):
    try:
        c = conexcao.cursor()
        c.execute(sql)
        print('\033[;33mtabela criada')
    except Error as ex:
        print(ex)
