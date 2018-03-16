import pygame
import math
import random





def runGame():
    bg = "field.png"
    screen = pygame.display.set_mode((780, 496))
    background = pygame.image.load(bg).convert()
    done = False
    screen.blit(background, (0, 0))
    class robot():
        robColor = (0, 0, 255)
        colisionColor = (255, 0, 0)
        xDirection, yDirection = random.randint(0, 389), random.randint(30, 450)
    robo = pygame.draw.rect(screen, robot.robColor, pygame.Rect(robot.xDirection, robot.yDirection, 20, 20))
    if (robot.xDirection < 389):
        mod = 389 - robot.xDirection
        mod += robot.xDirection
        rob2 = pygame.draw.rect(screen, robot.robColor, pygame.Rect(robot.xDirection, robot.yDirection, 20, 20))
        screen.blit(background, (0, 0))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                done = True


            pygame.display.flip()


runGame()
