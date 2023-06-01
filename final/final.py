import pygame
from um import first_phase

pygame.init()

l = 1280
h = 720
janela = pygame.display.set_mode((l, h))
clock = pygame.time.Clock()
pygame.display.set_caption("Joguinho")
running = True
count = 0

while running:
    dt = clock.tick(60) / 1000 
    
    # fim do jogo 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    
    if count < 20:
        first_phase()