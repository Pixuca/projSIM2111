import pygame
import random
import time
import math


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

def sweepLeft(): #robô à esquerda fazendo varredura para a direita
	pygame.draw.line(screen, areaColor, (xDirection+30, yDirection+30), (xDirection+60, yDirection+60), 1)
def sweepRight(): #robô à direita fazendo varredura para a esquerda
	mirrorX1 = xDirection + math.cos(math.radians(180))*(xDirection/2)
	mirrorY1 = (yDirection+100) + math.sin(math.radians(180))*(yDirection/2)
	mirrorY2 = (yDirection-100) + math.sin(math.radians(180))*(yDirection/2)
	line1 = pygame.draw.line(screen, areaColor, (mirrorX1+99, mirrorY1), (xDirection, yDirection+10), 1)
	line2 = pygame.draw.line(screen, areaColor, (mirrorX1+99, mirrorY2), (xDirection, yDirection+10), 1)
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill((0, 0, 0))
	color = (255, 102, 0)
	robColor = (0, 0, 255)
	colisionColor = (255, 0, 0)
	golColor = (255, 255, 255)
	areaColor = (0, 0, 0)
	screen.blit(background, (0,0))
	ball = pygame.draw.circle(screen, color, (390, 245), 5)
	robot = pygame.draw.rect(screen, robColor, pygame.Rect(xDirection, yDirection, 20, 20))
	colisionRange = pygame.draw.circle(screen, colisionColor, (xDirection+10, yDirection+10), 20, 1)
	goal2 = pygame.draw.rect(screen, golColor, pygame.Rect(745, 223.5, 1, 50)) #gol da direita
	goal1 = pygame.draw.rect(screen, golColor, pygame.Rect(33, 223.5, 1, 50)) #gol da esquerda
	areaA = pygame.draw.rect(screen, golColor, pygame.Rect(389, 17, 1, 50)) #área da esquerda
	areaB = pygame.draw.rect(screen, golColor, pygame.Rect(389, 428, 1, 50)) #área da direita
	if(xDirection < 389):
		#significa que o robo está do lado esquerdo do campo, ou seja, seu objetivo é fazer gol do lado direito
		sweepLeft()
	elif (xDirection > 389):
		#significa que o robo está do lado direito do campo, ou seja, seu objetivo é fazer gol do lado esquerdo
		sweepRight()
	pygame.display.flip()
