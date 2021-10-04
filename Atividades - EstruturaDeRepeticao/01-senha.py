"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""


print('Cadastre seu login e senha: ')
novo_login = input('Digite seu novo login: ')
nova_senha = input('Digite sua nova senha: ')

while nova_senha == novo_login:
    print(f'Erro login tem que ser diferente da senha: ')
    novo_login = input('Digite seu novo login: ')
    nova_senha = input('Digite sua nova senha: ')

print('Sucesso!')
