"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
e a quantidade de números impares.
"""
from gerar_numero_aleatorio import gerar_aleatorio

lista = []

for i in range(10):
    numero = gerar_aleatorio()
    lista.append(numero)

lista_par = []
lista_impar = []

for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(lista)
print('Lista de pares ',lista_par)
print('Lista de impares, ',lista_impar)