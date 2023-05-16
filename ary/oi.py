import pygame

pygame.init()

l = 1080
h = 640
janela = pygame.display.set_mode((l, h))
clock = pygame.time.Clock()
pygame.display.set_caption("Joguinho")
running = True

background = pygame.image.load("ary/imagens/espaco.png")
back_pos = 0
back_vel = 400

player = pygame.image.load("ary/imagens/nave.png")
pos = pygame.Vector2(l / 2, h / 2)

while running:
    dt = clock.tick(60) / 1000 

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos.y -= 250 * dt
    if keys[pygame.K_s]:
        pos.y += 250 * dt
    if keys[pygame.K_a]:
        pos.x -= 250 * dt
    if keys[pygame.K_d]:
        pos.x += 250 * dt

    back_pos -= back_vel * dt
    if back_pos < -background.get_width():
        back_pos = 0

    superficie = pygame.Surface((l + background.get_width(), h))
    superficie.blit(background, (back_pos, 0)) 
    superficie.blit(background, (back_pos + background.get_width(), 0))

    janela.fill((0, 0, 0))
    janela.blit(superficie, (0, 0))
    janela.blit(player, pos - pygame.Vector2(l / 2, h / 2))

    pygame.display.flip()

pygame.quit()