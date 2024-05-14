"""
Programinha para fazer backups datados de pastas
versão 2
Doug Funnie Bressar
14/05/2024
"""

# window to select the computer's folder
import os
from tkinter.filedialog import askdirectory
import shutil  # biblioteca para colar, copiar, manipular aquivos e etc.
import datetime

nome_pasta_selecionada = askdirectory()

lista_arquivos = os.listdir(nome_pasta_selecionada)
# print(lista_arquivos)
# for i in lista_arquivos: print(i)# for debug

# Make the backup of select folder
# a pasta de bkp será criada dentro da pasta original
nome_pasta_backup = 'backup'
nome_completo_pasta_backup = f'{nome_pasta_selecionada}/{nome_pasta_backup}'
if not os.path.exists(nome_completo_pasta_backup):
    os.mkdir(nome_completo_pasta_backup)

data_atual = datetime.datetime.today().strftime("%Y_%m_%d%H%M%S")

for arquivo in lista_arquivos:
    nome_completo_arquivo = os.path.join(nome_pasta_selecionada, arquivo)
    nome_final_arquivo = os.path.join(nome_completo_pasta_backup, data_atual, arquivo)

    if not os.path.exists(os.path.join(nome_completo_pasta_backup, data_atual)):
        os.makedirs(os.path.join(nome_completo_pasta_backup, data_atual))

    if "." in arquivo:
        shutil.copy2(nome_completo_arquivo, os.path.join(nome_completo_pasta_backup, data_atual))
    elif "backup" != arquivo: # para não fazer bkp do bkp... :(
        shutil.copytree(nome_completo_arquivo, nome_final_arquivo)

    """
    os.path.join() para construir os caminhos dos arquivos e pastas,
    mais robusto se o código precisar ser executado em diferentes
    sistemas operacionais."""


