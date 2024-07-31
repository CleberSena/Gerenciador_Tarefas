import sqlite3
from sqlite3 import Error
from time import sleep as sl
import os

def cabeçalho():    
    print('\033[31m~~'*23)
    print('\033[1;36m  Seja Bem Vindos Ao Gerenciador de Tarefas:\033[m')
    print('\033[31m~~'*23)


def menu():    
    print('\033[35m O Que Desejas Fazer:')
    print('\033[31m~~'*15)

    opcao = 0
    while opcao != 6:
        print('''\033[m
    1\033[34m=> \033[1;32mAdicionar Tarefas\033[m
    2\033[34m=> \033[1;32mVisualizar Tarefas\033[m
    3\033[34m=> \033[1;32mAtualizar Tarefas\033[m
    4\033[34m=> \033[1;32mTarefas Concluídas\033[m
    5\033[34m=> \033[1;32mRemover Tarefas\033[m
    6\033[34m=> \033[1;32mFechar Programa\033[m
    ''')

        try:
            opcao = int(input('\033[;36mDigite a opção Desejada '))

            if opcao <= 0 or opcao > 6:
                print(f'\033[;31mERRO!\033[;33m Opção inválida por favor digite um número de 1 a 6\033[;m')
        except ValueError:
                print('\033[;31mERRO!\033[;33m Opção inválida, por favor digite um número de 1 a 6\033[;m')

        if opcao == 1:
            vcon = ConexaoBanco()
            nova_tarefa = input('\033[;32mDigite a Tarefa Desejada\033[;m ').strip().title()
            isql = "INSERT INTO tb_Gerenciador_de_Tarefas(T_TAREFAS)VALUES('"+ nova_tarefa +"')"
            inserir_dados_na_tabela(vcon, isql)
            print(f'\033[;35m{isql} \033[;32minserido no BBD com sussesso')
            res = input('\033[;34mDeseja Criar Mais Alguma Tarefa?\033[;m ').strip().title()

            while res not in 'N':
                if res not in 'SN':                    
                    res = input('\033[;31m Opção inválida!\033[;33m Deseja Criar Mais Alguma Tarefa?\033[;m ').strip().title()
                elif res in 'S':
                    vcon = ConexaoBanco()
                    nova_tarefa = input('\033[;32mDigite a Tarefa Desejada\033[;m ').strip().title()
                    isql = "INSERT INTO tb_Gerenciador_de_Tarefas(T_TAREFAS)VALUES('"+ nova_tarefa +"')"
                    inserir_dados_na_tabela(vcon, isql)
                    print(f'\033[;37m"{nova_tarefa}" \033[;33mcriado com sussesso')
                    res = input('\033[;34mDeseja Criar Mais Alguma Tarefa?\033[;m ').strip().title()

                vcon.close()

            os.system('cls')

        elif opcao == 2:
            vcon = ConexaoBanco()
            rsql = "SELECT * FROM tb_Gerenciador_de_Tarefas"
            res = consulta(vcon, rsql)
            if res:# Verifica se a lista de resultados não está vazia
                for r in res:
                        print(f'\033[;35m{r}')
            else:
                print('\033[;33mAinda não existe lançamentos no seu banco de dados') 

            vcon.close()
            os.system('pause')
            sl(2) 
            os.system('cls') 

        elif opcao == 3:
            vcon = ConexaoBanco()
            rsql = "SELECT * FROM tb_Gerenciador_de_Tarefas"
            res = consulta(vcon, rsql)
            for r in res:
                print(f'\033[;37m{r}')
            id_escolhido = input('\033[;36mDigite o \033[1;31mID\033[;36m da tarefa que deseja atualizar?\033[;m ') 
            asql = "UPDATE tb_Gerenciador_de_Tarefas SET B_TAREFA_REALIZADA = ? WHERE N_IDTAREFAS= ?"
            parametros = ('True', id_escolhido)
            atualizarBanco(vcon, asql, parametros)
            pergunta = input('\033[36mDeseja atualizar mais alguma tarefas [S/N]').strip().upper()

            while pergunta not in 'SN':
                pergunta = input('\033[;31mOpção Inválida Digite somente [S/N]\033[;m').strip().upper()
                while pergunta == 'S':
                    vcon = ConexaoBanco()
                    rsql = "SELECT * FROM tb_Gerenciador_de_Tarefas"
                    res = consulta(vcon, rsql)
                    for r in res:
                        print(f'\033[;37m{r}')
                    id_escolhido = input('\033[;36mDigite o \033[1;31mID\033[;36m da tarefa que deseja atualizar?\033[;m ') 
                    asql = "UPDATE tb_Gerenciador_de_Tarefas SET B_TAREFA_REALIZADA = ? WHERE N_IDTAREFAS= ?"
                    parametros = ('True', id_escolhido)
                    atualizarBanco(vcon, asql, parametros) 
                    pergunta = input('\033[;36mDeseja atualizar mais alguma tarefas [S/N]').strip().upper()                  
                if pergunta == 'N':
                    print('\033[;35mAtualizações finalizadas com sussesso\033[;m')

            vcon.close()

            os.system('pause')
            sl(2)
            os.system('cls')

        elif opcao == 4:
            vcon = ConexaoBanco()
            rsql = "SELECT * FROM tb_Gerenciador_de_Tarefas"
            res = consulta(vcon, rsql)
            for r in res:
                if r[2] == 'True':
                    print(f'\033[;33m{r}')

            os.system('pause')
            sl(2)
            os.system('cls')

        elif opcao == 5:
            vcon = ConexaoBanco()
            rsql = "SELECT * FROM tb_Gerenciador_de_Tarefas"
            res = consulta(vcon, rsql)
            for r in res:
                print(f'\033[35m{r}')
                pergunta = input('\033[;33mDigite o nome da tarefa Deseja Escluir:\n\033[;32mSe digitar a palavra \033[1;36mtodas\033[;32m o banco de dados será limpo\033[;m ').strip().title()
                
                if pergunta == 'Todas':                              
                    esql = "DELETE FROM tb_Gerenciador_de_Tarefas" 
                    excluir_tarefas(vcon, esql)
                    print('\033[;35mTodas tarefas excluídas com Sussesso\033[;m')

                    vcon.close()

                    os.system('pause')
                    sl(2)
                    os.system('cls')

                else:                              
                    esql = "DELETE FROM tb_Gerenciador_de_Tarefas WHERE T_TAREFAS='"+pergunta+"'" 
                    excluir_tarefas(vcon, esql)
                    print(f'\033[;31mA tarefa \033[1;33m{pergunta}\033[;31m foi excluída com sussesso\033[;m')

                    vcon.close()

                    os.system('pause')
                    sl(2)
                    os.system('cls')

                break
# Fechamento do programa:
        else:
            print('\033[;31mfechando Gerenciador de tarefas\033[;m')

    os.system('pause')
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

def inserir_dados_na_tabela(conexcao, sql):
    try:
        c = conexcao.cursor()
        c.execute(sql)
        conexcao.commit()
        print(f'{sql} foi inserido em seu Banco de Dados:')
    except Error as ex:
        print(ex)

def excluir_tarefas(conexcao, sql):
    try:
        c = conexcao.cursor()
        c.execute(sql)
        conexcao.commit()
        print(f'{sql} foi escuido em seu Banco de Dados:')
    except Error as ex:
        print(ex)

def atualizarBanco(conexcao, sql, parametro):
    try:
        c = conexcao.cursor()
        c.execute(sql, parametro)
        conexcao.commit()
        print('\033[35mO Banco de Dados foi atualizado com sussesso:')
    except Error as ex:
        print(ex)

def consulta(conexcao, sql):
    c = conexcao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado
