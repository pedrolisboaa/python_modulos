"""
Faça um programa que leia 5 números e informe o maior número.
"""

lista = []
for i in range(5):
    numero = float(input('Digite um número '))
    lista.append(numero)


print(lista)
print(f'maior número {max(lista)}')