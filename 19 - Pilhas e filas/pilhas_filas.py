"""
Pilhas e filas
Pilha (stack) - LIFO last in, first out
    Exemplo: Pilha de livros são adicionadas uma sobre o outro
Fila (queue) - FIFO first in, first out
    Exemplo: Um fila de banco
"""
"""
# Pilha
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')
print(livros)

livros_removido = livros.pop()
print(livros)
print(livros_removido)
"""
from collections import deque


fila = deque()
fila.append('maria')
fila.append('joão')
fila.append('marcos')
fila.append('jose')
fila.append('pedro')

print(fila)

fila.popleft()
fila.popleft()

print(fila)

fila_max = deque(maxlen=4)
fila_max.append('marcia')
fila_max.append('maria')
fila_max.append('mariana')
fila_max.append('marcela')
print(fila_max
      )
fila_max.append('mario')
print(fila_max)