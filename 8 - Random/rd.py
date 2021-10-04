import random
import string

inteiro = random.randint(10, 20)
inteiro_range = random.randrange(900, 1000, 10)
flutuante = random.uniform(10, 20)

lista = ['pedro', 'Juliana', 'marcela', 'Alice', 'Daniel', 'Marcos']
sorteio = random.choice(lista)
sorteio_duplo = random.choices(lista, k=2)
sorteio_duplo_sem_repetir = random.sample(lista, 2)


print(inteiro)
print(flutuante)
print(inteiro_range)
print(sorteio)
print(sorteio_duplo)
print(sorteio_duplo_sem_repetir)

# Embaralhar a lista
print(lista)
random.shuffle(lista)
print(lista)

# Gerar senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = "!@#$%¨&*()_+"
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)