from zipfile import ZipFile
import os

caminho = r'E:\Arquivos Usuário\Desktop\atualizacao_prouni'
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompacatado')