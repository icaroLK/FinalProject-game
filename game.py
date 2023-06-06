import pygame

pygame.init()

l = 1280
h = 720
janela = pygame.display.set_mode((l, h))
clock = pygame.time.Clock()
pygame.display.set_caption("Joguinho")
running = True
pontos = 0

background = pygame.image.load("../icaro/images/bg.png")
back_pos = 0
back_vel = 1000

player = pygame.image.load("ary/imagens/nave.png")
player_pos = player.get_rect(center=(l / 2, h / 2))
player_vel = 500

while running:
    dt = clock.tick(60) / 1000 
    
    # fim do jogo 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    # TELA DE INICIO

    # PRIMEIRA FASE

    back_pos -= back_vel * dt
    if back_pos < -background.get_width():
        back_pos = 0

    superficie = pygame.Surface((l + background.get_width(), h))
    superficie.blit(background, (back_pos, 0)) 
    superficie.blit(background, (back_pos + background.get_width(), 0))

    # tela
    janela.fill((0, 0, 0))
    janela.blit(superficie, (0, 0))
    janela.blit(player, player_pos)
    
    # SEGUNDA FASE

    # FASE FINAL


    pygame.display.flip()

pygame.quit()