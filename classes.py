import random
from trajetoria import *
class robot:
    x = random.randint(20, 389)
    x2 = trajX[0]
    y = random.randint(30, 450)
    espessura = 20
    largura = 20

class colision:
    x = robot.x + 10
    y = robot.y + 10
    colisionColor = (255, 0, 0)
    diametro = 250
    espessura = 1

class kick:
    x = robot.x + 10
    y = robot.y + 10
    kickColor = (255, 255, 0)
    diametro = 20
    espessura = 1
class bola:
    x = 390
    y = 245
    espessura = 5
    color = (255, 102, 0)
