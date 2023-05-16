import pygame
from pygame.locals import *
from sys import exit

roxo = (255,131,250)
rosa = (255,62,150)
preto = (0,0,0)
branco = (255,255,255)

largura = 640
altura = 480

pygame.display.set_mode((largura,altura))
pygame.display.set_caption('ICARYANOLINE')
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()