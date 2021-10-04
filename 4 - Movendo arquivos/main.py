import os
import shutil

caminho_original = r'E:\Arquivos Usuário\Desktop\atualizacao_prouni'
caminho_novo= r'E:\Arquivos Usuário\Desktop\atualizacao_prouni2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if 'GAS' in file:
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} movido com sucesso.')

            if 'GAS' in file:
                os.remove(new_file_path)
