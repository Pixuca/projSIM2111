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
done = False


x, y = 900/9, 600/6
distT = (x + y)/2
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
vmax = 2.4
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

def sweepLeft(i, vi):
	if (xi[i] > robot.x):
		if (robot.y > yi[i]):
			distancia = (xi[i] - robot.x) + (robot.y - yi[i])
			distanciaT = distancia/distT
			print("Distância: %.2fm" % distanciaT)
		elif (robot.y < yi[i]):
			distancia = (xi[i] - robot.x) + (yi[i] - robot.y)
			distanciaTotal = distancia/distT
			print("Distância: %.2fm" % distanciaTotal)


	#parte da movimentação do lado esqurdo do campo
	if (robot.x < xi[i] - 20):
		for vi in range (vmax):
			vi += acel2
			if (vi > vmax):
				vi = vmax
		robot.x += vmax

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
		screen.blit(background, (0, 0))
		xk = xi[i]
		yk = yi[i]



	for i in range(len(xi)):
		screen.blit(background, (0, 0))
		bola.x = xi[i]
		bola.y = yi[i]
		pygame.draw.rect(screen, robColor, pygame.Rect(robot.x, robot.y, 20, 20))
		ball = pygame.draw.rect(screen, bola.color, pygame.Rect(bola.x, bola.y, bola.espessura, bola.espessura))
		if (robot.x < bola.x):
			if (robot.y > bola.y):
				distancia = (bola.x - robot.x) + (robot.y - bola.y)
				distanciaT = distancia/distT
				print("Distância: %.2fm" % distanciaT)
			elif (robot.y < bola.y):
				distancia = (bola.x - robot.x) + (bola.y - robot.y)
				distanciaTotal = distancia/distT
				print("Distância: %.2fm" % distanciaTotal)
			vi += acel2
			if (vi > vmax):
				vi = vmax
				acel2 = acel1
				print(vi)
			robot.x += vi
			if (robot.x > 880):
				robot.x = 880
			pygame.display.flip()
		if (robot.x > bola.x):
			vi += acel2
			if (vi > vmax):
				acel2 = acel1
				print(vi)
			robot.x -= vi
			pygame.display.flip()

		if (robot.y > bola.y):
			vi += acel2
			if (vi > vmax):
				vi = vmax
				acel2 = acel1
				print(vi)
			robot.y -= vi
			pygame.display.flip()
		if (robot.y < bola.y):
			vi += acel2
			if (vi > vmax):
				vi = vmax
				acel2 = acel1
				print(vi)
			robot.y += vi
			pygame.display.flip()
		print(robot.x, bola.x)
