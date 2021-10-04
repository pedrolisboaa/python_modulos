"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120
"""

from math import factorial
from gerar_numero_aleatorio import gerar_aleatorio

n = gerar_aleatorio()
print(f'Número gerado {n}')
print(f'Seu fatorial {factorial(n)}')