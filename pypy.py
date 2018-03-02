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

	***Valores da variável 'xDirection'***

	389, 750 para o robô sempre aparecer à direita
	30, 389 para o robô sempre aparecer à esquerda
	30, 750 para o robô ter possibilidade de aparecer nos dois lados do campo

------------------------------------------------'''

#direção de spawn do robô em X e Y
xDirection = random.randint(30, 389) #30, 750 ----  #240 (centro)
yDirection = random.randint(30, 450) #30, 450 ---- #240 (centro)
print("Direção em X: %d" % xDirection)
print("Direção em Y: %d" % yDirection)

def sweepLeft(): #robô à esquerda fazendo varredura para a direita
	''' *****campo de visão razoavelmente grande*****
			line1 - xDirection (end) += 400 == xSize_line_1
					yDirection (end) -=150  == xMod_dir_l1

			line2 - xDirection (end) += 400 == xMod_dir_l2
			      - yDirection (end) += 150 == ySize_line_2
		*****---------------------------------******
	'''
	#valores abaixo para campo de visão extra grande
	xSize_line_1 = 400 #500
	ySize_line_2 = 150 #250

	yMod_dir_l1 = 150
	xMod_dir_l2 = 400

	final_l1_x = xDirection + xSize_line_1
	final_l1_y  = yDirection - yMod_dir_l1

	final_l2_x = xDirection + xMod_dir_l2
	final_l2_y = yDirection + ySize_line_2

	if (final_l1_y < 0):
		while (final_l1_y < 0):
			count = 1
			final_l1_y += count

	middle_l1_y = ((yDirection+10) + final_l1_y)/2
	middle_l2_y = ((yDirection+10) + final_l2_y)/2

	cordaLinha = (255, 0, 0)
	line1 = pygame.draw.line(screen, areaColor, (xDirection+20, yDirection+10), (final_l1_x, final_l1_y), 1)
	line2 = pygame.draw.line(screen, areaColor, (xDirection+20, yDirection+10), (final_l2_x, final_l2_y), 1)
'''	linhaTeste1 = pygame.draw.line(screen, cordaLinha, (0, yDirection), (0, final_l1_x), 1)
	linhaTeste2 = pygame.draw.line(screen, cordaLinha, (0, yDirection), (0, final_l2_x), 1) '''

	if(middle_l1_y < yBall and middle_l2_y > yBall):
		print("Bola avistada")

def sweepRight(): #robô à direita fazendo varredura para a esquerda
	mirrorX1 = xDirection + math.cos(math.radians(180))*(xDirection/2)
	mirrorY1 = (yDirection+100) + math.sin(math.radians(180))*(yDirection/2)
	mirrorY2 = (yDirection-100) + math.sin(math.radians(180))*(yDirection/2)
	line1 = pygame.draw.line(screen, areaColor, (mirrorX1-200, mirrorY1+150), (xDirection, yDirection+10), 1)
	line2 = pygame.draw.line(screen, areaColor, (mirrorX1-200, mirrorY2-150), (xDirection, yDirection+10), 1)

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
	xBall = 390
	yBall = 245
	ball = pygame.draw.circle(screen, color, (xBall, yBall), 5)
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
