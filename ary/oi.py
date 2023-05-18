import pygame
import random

pygame.init()

l = 1280
h = 640
janela = pygame.display.set_mode((l, h))
clock = pygame.time.Clock()
pygame.display.set_caption("Joguinho")
running = True

# fundo do jogo
background = pygame.image.load("ary/imagens/espaco.png")
back_pos = 0
back_vel = 700

# jogador
player = pygame.image.load("ary/imagens/nave.png")
player_pos = player.get_rect(center=(l / 2, h / 2))
player_vel = 350

# inimigos
enemies = []
enemy = pygame.image.load("ary/imagens/enemy.png")
enemy_vel = 500
enemy_dt = 2
last_enemy = 0 
# contador de vidas
life = pygame.image.load("ary/imagens/coracao.png")
life_count = 5

# contador de tempo
sec = 0
count = 0
font = pygame.font.Font(None, 42)

# projéteis
p = []
picle = pygame.image.load("ary/imagens/pew.png")
picle_dt = 0.5
last_picle = 0

# looping principal
while running:
    dt = clock.tick(60) / 1000 
    
    # fim do jogo 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    # movimentando o personagem
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= player_vel * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += player_vel * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= player_vel * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += player_vel * dt

    # atirando os projéteis
    if keys[pygame.K_SPACE]:
        time = pygame.time.get_ticks() / 1000
        if time - last_picle > picle_dt:
            projetil = pygame.Rect(player_pos.centerx, player_pos.centery, 5,10)
            p.append(projetil)
            last_picle = time

    # movimento do fundo
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
    
    # tiro
    for tiro in p:
        tiro.x += 400 * dt
        janela.blit(picle, tiro)
    
    # inimigo
    time = pygame.time.get_ticks() / 1000
    for enemy_pos in enemies:
        enemy_pos.x -= enemy_vel * dt
        janela.blit(enemy, enemy_pos)

    if time - last_enemy > enemy_dt:
        x = l
        y = random.randint(25, h - enemy.get_width())
        enemy_pos = enemy.get_rect(topleft=(x, y))
        enemies.append(enemy_pos)
        last_enemy = time

    # borda
    if player_pos.left < 0:
        player_pos.left = 0
    if player_pos.right > l:
        player_pos.right = l
    if player_pos.top < 0:
        player_pos.top = 0
    if player_pos.bottom > h:
        player_pos.bottom = h   

    # contador de tempo
    sec += dt
    count = int(sec)
    text = font.render('' + str(count), True, (255, 255, 255))
    janela.blit(text, (25,25))

    # vida
    for c in range(life_count):
        janela.blit(life, (c*40+1050,25))

    pygame.display.flip()

pygame.quit()