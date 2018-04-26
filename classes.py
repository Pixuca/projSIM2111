import random
from trajetoria import *

class robot:
    x = random.randint(450, 900)
    y = random.randint(0, 600)
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
    espessura = 5
    x = random.randint(0, 900)
    y = random.randint(0, 600)
    color = (255, 102, 0)
