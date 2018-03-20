import random
import time
class robo:
    x = random.uniform(0, 10)
    y = random.uniform(0, 10)
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
    def pos(self):
        print ("%d agora está em %d" % (self.x, self.y))
s1 = robo('kkk', 10, 20)
s1.x
s1.pos()
print(s1.nome)
