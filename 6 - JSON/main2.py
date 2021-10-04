import json

carros_json = '{"marca": "honda", "modelo": "HRV", "cor": "prata"}'
pessoa = {
        'nome': 'Pedro',
        'Sobrenome': 'Lisboa',
        'Idade': 28
        }

carros = json.loads(carros_json)
pessoa_json = json.dumps(pessoa)

# print(carros['marca'])
# print(carros['modelo'])

# for x, y in carros.items():
#     print(x, y)
#
# for chave, valor in pessoa.items():
#     print(chave, valor)

print(pessoa_json)
print(type(pessoa_json))