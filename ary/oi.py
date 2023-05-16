import pygame

pygame.init()

janela = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Joguinho")
running = True
dt = 0


background = pygame.image.load("ary/imagens/espaco.png")

pos = pygame.Vector2(janela.get_width() / 2, janela.get_height() / 2)

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    janela.blit(background, (0,0))    

    pygame.draw.circle(janela, "red", pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pos.y -= 300 * dt
    if keys[pygame.K_s]:
        pos.y += 300 * dt
    if keys[pygame.K_a]:
        pos.x -= 300 * dt
    if keys[pygame.K_d]:
        pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()