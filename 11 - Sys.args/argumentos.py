import sys
import os

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Faltando argumentos')
    print('-a', 'Para Listar todos os arquivos nesta pasta', sep="\t")
    print('-d', 'Para Listar todos os diretorios nesta pasta', sep="\t")
    sys.exit()

so_arquivos = False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

for so_arquivos in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        if os.path.isfile(arquivo):
            print(arquivo)

