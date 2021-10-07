"""
pip install openpyxl
"""

import openpyxl

pedidos = openpyxl.load_workbook('pedido.xlsx')

nome_planilha = pedidos.sheetnames
print(nome_planilha)

planilha1 = pedidos['Pedidos 07-10-21']
print(planilha1['b4'].value)

