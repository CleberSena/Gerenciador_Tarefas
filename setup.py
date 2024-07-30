import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final
arquivos = ['Gerenciador de Tarefas.db']
# Saida de arquivos
configuracao = Executable(
    script='G_Tarefas.py',
    icon='icon.ico'
)
# Configurar o executável
setup(
    name='Gerenciador de Tarefas',
    version='1.0',
    description='Este programa gerencia uma rotina de tarefas diária',
    author='Cleber W. Sena',
    options={'build_exe':{ 
        'include_files' : arquivos,      
        'include_msvcr': True
    }},
    executables=[configuracao]
)