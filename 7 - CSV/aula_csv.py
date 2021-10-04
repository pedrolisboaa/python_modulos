"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usados em tabelas (Excel, Google Sheets), base de dados
Clientes de e-mail etc
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
