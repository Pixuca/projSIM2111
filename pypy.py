import pygame
import random
import time
import math
from classes import *

pygame.init()
bg = "field.png"
screen = pygame.display.set_mode((780, 496))
background = pygame.image.load(bg).convert()
done = False

'''-----------------------------------------------

	389, 750 para o robô sempre aparecer à direita
	30, 389 para o robô sempre aparecer à esquerda
	30, 750 para o robô ter possibilidade de aparecer nos dois lados do campo

------------------------------------------------'''

#direção de spawn do robô em X e Y
xDirection = random.randint(389, 750) #30, 750
yDirection = random.randint(30, 450)



def sweepRight():
	if(robot.x > bola.x + 5):
		robot.x -= 1
		colision.x -= 1
		kick.x -= 1

	if(robot.y > bola.y - 10):
		robot.y -= 1
		colision.y -= 1
		kick.y -= 1
	elif (robot.y < bola.y - 10):
		robot.y += 1
		colision.y += 1
		kick.y += 1

	if (colision.x - bola.x <= 15 and colision.y - bola.y <= 15):
		forca = random.randint(40, 100)
		vel = forca
		chance = random.randint(0, 2)
		print(chance)
		if (chance == 0):
			bola.x -= forca
			bola.y += forca
		elif (chance == 1):
			bola.x -= forca
			bola.y -= forca
		elif (chance == 2):
			bola.x -= forca
		while vel >= 0:
			vel -= 1
def sweepLeft():
	if ((colision.x + bola.x) <= colision.diametro):
		print("Estou vendo a bola! Minha distância até ela é de X = %d" % ((colision.x + bola.x)))
	if (robot.x < bola.x+5):
		robot.x += 1
		colision.x += 1
		kick.x += 1

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			done = True
		if robot.x > bola.x:
			sweepRight()
		elif robot.x < bola.x:
			sweepLeft()
	screen.fill((0, 0, 0))
	color = (255, 102, 0)
	robColor = (0, 0, 255)
	golColor = (255, 255, 255)
	areaColor = (0, 0, 0)
	screen.blit(background, (0,0))

	colisionRange = pygame.draw.circle(screen, colision.colisionColor, (colision.x, colision.y), colision.diametro, colision.espessura)
	kickRange = pygame.draw.circle(screen, kick.kickColor, (kick.x, kick.y), kick.diametro, kick.espessura)
	ball = pygame.draw.circle(screen, color, (bola.x, bola.y), bola.espessura)
	robot = pygame.draw.rect(screen, robColor, pygame.Rect(robot.x, robot.y, 20, 20))
	goal2 = pygame.draw.rect(screen, golColor, pygame.Rect(745, 223.5, 1, 50)) #gol da direita
	goal1 = pygame.draw.rect(screen, golColor, pygame.Rect(33, 223.5, 1, 50)) #gol da esquerda
	areaA = pygame.draw.rect(screen, golColor, pygame.Rect(389, 17, 1, 50)) #área da esquerda
	areaB = pygame.draw.rect(screen, golColor, pygame.Rect(389, 428, 1, 50)) #área da direita
	pygame.display.flip()
