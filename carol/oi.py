import pygame
from pygame.locals import *
from sys import exit

largura = 1280
altura = 720

pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Ricks')
 

pygame.font.init()
font = pygame.font.Font(None, 36)
text = font.render("Bem-vindo ao jogo Ricks", True, (255, 255, 255))
background_image = pygame.image.load('carol/bg.jpg')
screen = pygame.display.set_mode((largura, altura))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.blit(background_image, [0, 0])
    pygame.display.update()
