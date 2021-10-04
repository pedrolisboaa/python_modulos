"""
JavaScript Object Notation - JSON
JSON é um formato de troca de dados entre sistemas e programs muito leve e de fácil utilização
Muito utilizado por APIs
"""

from dados import *
import json
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista2 = (1,2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# dados_json = json.dumps(lista)
# dados2_json = json.dumps(lista2)
# dados3_jason = json.dumps(clientes_json, indent=4)
#
# print(dados_json)
# print(type(dados2_json))
#
# print(dados3_jason)
# print(type(dados3_jason))

#print(clientes_json)
#print(type(clientes_json))

# dicionario_json = json.loads(clientes_json)
# for chave, valor in dicionario_json.items():
#     print(chave)
#     print(valor)

with open('clietes.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)