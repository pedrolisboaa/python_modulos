from time import sleep
from threading import Thread

# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo
#
#         super().__init__()
#
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)
#
#
# t = MeuThread('Thread 1', 5)
# t.start()
#
# t2 = MeuThread('Thread 2', 8)
# t2.start()
#
# t3 = MeuThread('Thread 2', 2)
# t3.start()
#
# for i in range(20):
#     print(i)
#     sleep(1)


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=vai_demorar, args=('Olá Pedro', 5))
t.start()

for i in range(20):
    print(i)
    sleep(.8)
