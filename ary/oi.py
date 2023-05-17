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
back_vel = 600

player = pygame.image.load("ary/imagens/nave.png")
player_pos = player.get_rect(center=(l / 2, h / 2))

life = pygame.image.load("ary/imagens/coracao.png")

sec = 0
count = 0
font = pygame.font.Font(None, 42)

p = []
pew = pygame.image.load("ary/imagens/pew.png")

pew_dt = 0.5
final_pew = 0

while running:
    dt = clock.tick(60) / 1000 

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    if keys[pygame.K_SPACE]:
        time = pygame.time.get_ticks() / 1000
        if time - final_pew > pew_dt:
            projetil = pygame.Rect(player_pos.centerx, player_pos.top, 5,10)
            p.append(projetil)

            final_pew = time

    back_pos -= back_vel * dt
    if back_pos < -background.get_width():
        back_pos = 0

    superficie = pygame.Surface((l + background.get_width(), h))
    superficie.blit(background, (back_pos, 0)) 
    superficie.blit(background, (back_pos + background.get_width(), 0))

    janela.fill((0, 0, 0))
    janela.blit(superficie, (0, 0))
    janela.blit(player, player_pos)

    for tiro in p:
        tiro.x += 400 * dt
        janela.blit(pew, tiro)

    if player_pos.left < 0:
        player_pos.left = 0
    if player_pos.right > l:
        player_pos.right = l
    if player_pos.top < 0:
        player_pos.top = 0
    if player_pos.bottom > h:
        player_pos.bottom = h   

    sec += dt
    count = int(sec)
    text = font.render('' + str(count), True, (255, 255, 255))
    janela.blit(text, (20,20))


    for c in range(5):
        janela.blit(life, (c*40+870,20))

    pygame.display.flip()

pygame.quit()