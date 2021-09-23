from datetime import datetime, timedelta

# criando uma data
# data = datetime(2021, 9, 15, 20, 1, 10)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))


# convertando uma data
# data = datetime.strptime('22/09/2021', '%d/%m/%Y')
# print(data.timestamp())

# data = datetime.strptime('15/09/1992 20:30:00', '%d/%m/%Y %H:%M:%S')
# data = data + timedelta(days=5)
# print(data.strftime('%d/%m/%Y %H:%M'))

d1 = datetime.strptime('15/09/1992 20:30', '%d/%m/%Y %H:%M')
d2 = datetime.strptime('22/08/1996 8:35', '%d/%m/%Y %H:%M')

print(d2 - d1)