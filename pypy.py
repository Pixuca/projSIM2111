import pygame
import random
import time
import math
from trajetoria import *
from classes import *


pygame.init()
bg = "field2.jpeg"
screen = pygame.display.set_mode((900, 600))
background = pygame.image.load(bg).convert()

ball_pos = (xi[0], yi[0])
done = False


x, y = 900/9, 600/6
distT = (x + y)/2
print("A cada %.2f pixels se tem 1 (um) metro. " % distT)
distancia = (robot.x - xi[0]) + (robot.y - yi[0])
print("Distância (em pixels): %dp" % distancia)
if (robot.x < xi[0]):
	if (robot.y > yi[0]):
		distancia = (xi[0] - robot.x) + (robot.y - yi[0])
		print("Distância (em pixels): %dp" % distancia)
		distanciaT = distancia/distT
		print("Distância (em metros): %.2fm" % distanciaT)

#dados do robo
acel1 = 0
acel2 = 0.1
vmax = 2.3
vi = 0
#---------


def sweepRight():
	if (robot.x > xi[0]):
		if (robot.y > yi[0]):
			distancia = (robot.x - xi[0]) + (robot.y - yi[0])
			distanciaT = distancia/distT
			print("Distância: %.2fm" % distanciaT)
		elif (robot.y < yi[0]):
			distancia = (robot.x - xi[0]) + (yi[0] - robot.y)
			distanciaTotal = distancia/distT
			print("Distância: %.2fm" % distanciaTotal)
	if(robot.x > xi[0] + 5):
		robot.x -= 2

	if(robot.y > yi[0] - 10):
		robot.y -= 2


	elif (robot.y < yi[0] - 10):
		robot.y += 2


	if (robot.x - xi[0] <= 15 and robot.x - xi[0] > 0):
		if (yi[0] > robot.y):
			robot.y += 2



		if (yi[0] - robot.y <= 15 and yi[0] - robot.y > 0):
			forca = random.randint(40, 100)
			chance = random.randint(0, 2)
			if (chance == 0):
				xi[0] -= forca
				yi[0] += forca
				return ball_pos
				pygame.display.update()

			elif (chance == 1):
				xi[0] -= forca
				yi[0] -= forca
				return ball_pos
				pygame.display.update()

			elif (chance == 2):
				xi[0] -= forca
				return ball_pos
				pygame.display.update()

		elif (yi[0] - robot.y <= 0):
			robot.y -= 2

	if (robot.x <= 0):
		robot.x = 0

def sweepLeft():
	if (xi[0] > robot.x):
		if (robot.y > yi[0]):
			distancia = (xi[0] - robot.x) + (robot.y - yi[0])
			distanciaT = distancia/distT
			print("Distância: %.2fm" % distanciaT)
		elif (robot.y < yi[0]):
			distancia = (xi[0] - robot.x) + (yi[0] - robot.y)
			distanciaTotal = distancia/distT
			print("Distância: %.2fm" % distanciaTotal)


	#parte da movimentação do lado esqurdo do campo
	if (robot.x < xi[0] - 20):
		robot.x += 2

	if (robot.y < yi[0] - 10):
		robot.y += 2

	elif (robot.y > yi[0] - 10):
		robot.y -= 2

	if (robot.x == xi[0] -20 and robot.y > yi[0]):
		robot.y -= 2

	elif (robot.x == xi[0]-20 and robot.y < yi[0]):
		robot.y += 2

	if (xi[0] - robot.x <= 20):
		if(yi[0] > robot.y or yi[0] - robot.y < 0):
			robot.y += 2
		if (yi[0] - robot.y <= 15 and yi[0] - robot.y >= 0):
			forca = random.randint(40, 100)
			chance = random.randint (0, 2)
			if (chance == 0):
				xi[0] += forca
				yi[0] += forca
				ball_pos = (xi[0], yi[0])
				animationTimer.tick(100)
				pygame.display.update()
			elif (chance == 1):
				xi[0] += forca
				yi[0] -= forca
				ball_pos = (xi[0], yi[0])
				animationTimer.tick(100)
				pygame.display.update()
			elif (chance == 2):
				xi[0] += forca
				ball_pos = (xi[0], yi[0])
				animationTimer.tick(100)
				pygame.display.update()


	if (robot.x >= 900):
		robot.x = 900

while not done:
	robColor = (0, 0, 255)
	animationTimer = pygame.time.Clock()
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			done = True

	screen.fill((0, 0, 0))
	for i in range(1001):
		xk = xi[i]
		yk = yi[i]

	print(yk)
	time.sleep(2)

	for i in range(1001):
		screen.blit(background, (0, 0))
		xk2 = xi[i]
		yk2 = yi[i]
		pygame.draw.rect(screen, bola.color, pygame.Rect(xk2, yk2, bola.espessura, bola.espessura))
		pygame.draw.rect(screen, robColor, pygame.Rect(robot.x, robot.y, 20, 20))
		if robot.x < xk:
			vi += acel2
			robot.x += vi
			if (robot.x > 760):
				robot.x = 760
			if (vi > vmax):
				vi = vmax
		if robot.y > yk:
			robot.y -= vmax
		if robot.y < yk2:
			robot.y += vmax
		if xk2 == robot.x - 5:
			xk2 = robot.x - 5
		pygame.display.flip()
