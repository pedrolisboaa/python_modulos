from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays

setlocale(LC_ALL, 'pt_BR.utf-8')
data = datetime.now()
mes_atual = int(data.strftime('%m'))
formatacao = data.strftime('%A, %d de %B de %Y')
formatacao2 = data.strftime('%a, %d/%m/%y ')
print(formatacao)
print(formatacao2)

print(mes_atual, mdays[mes_atual])