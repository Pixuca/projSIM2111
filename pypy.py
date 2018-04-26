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
fpsClock = pygame.time.Clock()
fps = 120
ball_pos = (bola.x, bola.y)
done = False


x, y = 900/9, 600/6
distT = (x + y)/2
print("A cada %.2f pixels se tem 1 (um) metro. " % distT)
distancia = (robot.x - bola.x) + (robot.y - bola.y)
print("Distância (em pixels): %dp" % distancia)
if (robot.x < bola.x):
	if (robot.y > bola.y):
		distancia = (bola.x - robot.x) + (robot.y - bola.y)
		print("Distância (em pixels): %dp" % distancia)
		distanciaT = distancia/distT
		print("Distância (em metros): %.2fm" % distanciaT)
def sweepRight():
	if (robot.x > bola.x):
		if (robot.y > bola.y):
			distancia = (robot.x - bola.x) + (robot.y - bola.y)
			distanciaT = distancia/distT
			print("Distância: %.2fm" % distanciaT)
		elif (robot.y < bola.y):
			distancia = (robot.x - bola.x) + (bola.y - robot.y)
			distanciaTotal = distancia/distT
			print("Distância: %.2fm" % distanciaTotal)
	if(robot.x > bola.x + 5):
		robot.x -= 2

	if(robot.y > bola.y - 10):
		robot.y -= 2


	elif (robot.y < bola.y - 10):
		robot.y += 2


	if (robot.x - bola.x <= 15 and robot.x - bola.x > 0):
		if (bola.y > robot.y):
			robot.y += 2



		if (bola.y - robot.y <= 15 and bola.y - robot.y > 0):
			forca = random.randint(40, 100)
			chance = random.randint(0, 2)
			if (chance == 0):
				bola.x -= forca
				bola.y -= forca
				ball_pos = (bola.x, bola.y)
				pygame.display.flip()

			elif (chance == 1):
				bola.x -= forca
				bola.y -= forca
				ball_pos = (bola.x, bola.y)
				pygame.display.flip()

			elif (chance == 2):
				bola.x -= forca
				ball_pos = (bola.x, bola.y)
				pygame.display.flip()

		elif (bola.y - robot.y <= 0):
			robot.y -= 2

	if (robot.x <= 0):
		robot.x = 0

def sweepLeft():
	if (bola.x > robot.x):
		if (robot.y > bola.y):
			distancia = (bola.x - robot.x) + (robot.y - bola.y)
			distanciaT = distancia/distT
			print("Distância: %.2fm" % distanciaT)
		elif (robot.y < bola.y):
			distancia = (bola.x - robot.x) + (bola.y - robot.y)
			distanciaTotal = distancia/distT
			print("Distância: %.2fm" % distanciaTotal)


	#parte da movimentação do lado esqurdo do campo
	if (robot.x < bola.x - 20):
		robot.x += 1

	if (robot.y < bola.y - 10):
		robot.y += 1

	elif (robot.y > bola.y - 10):
		robot.y -= 1

	if (bola.x - robot.x <= 15):
		if(bola.y > robot.y):
			robot.y += 1


		if (kick.y - bola.y <= 15 and robot.y - bola.y > 0):
			forca = random.randint(40, 100)
			chance = random.randint (0, 2)
			if (chance == 0):
				bola.x += forca
				bola.y += forca
				ball_pos = (bola.x, bola.y)
				pygame.display.flip()
			elif (chance == 1):
				bola.x += forca
				bola.y -= forca
				ball_pos = (bola.x, bola.y)
				pygame.display.flip()
			elif (chance == 2):
				bola.x += forca
				ball_pos = (bola.x, bola.y)
				pygame.display.flip()
	if (robot.x >= 900):
		robot.x = 900

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			done = True
	if robot.x > bola.x:
		sweepRight()
		ball_pos = (bola.x, bola.y)
		pygame.display.flip()

	elif robot.x < bola.x:
		sweepLeft()
		ball_pos = (bola.x, bola.y)
		pygame.display.flip()

	screen.fill((0, 0, 0))
	robColor = (0, 0, 255)
	golColor = (255, 255, 255)
	areaColor = (0, 0, 0)
	screen.blit(background, (0,0))

	pygame.draw.circle(screen, bola.color, (ball_pos), bola.espessura)
	robot = pygame.draw.rect(screen, robColor, pygame.Rect(robot.x, robot.y, 20, 20))
	pygame.display.flip()
	fpsClock.tick(fps)
