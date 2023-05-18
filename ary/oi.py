import pygame
import random

pygame.init()

l = 1280
h = 720
janela = pygame.display.set_mode((l, h))
clock = pygame.time.Clock()
pygame.display.set_caption("Joguinho")
running = True

# fundo do jogo
background = pygame.image.load("ary/imagens/espaco.png")
back_pos = 0
back_vel = 900

# jogador
player = pygame.image.load("ary/imagens/nave.png")
player_pos = player.get_rect(center=(l / 2, h / 2))
player_vel = 400
player_hitbox = player_pos

# inimigos
enemies = []
enemy = pygame.image.load("ary/imagens/enemy.png")
enemy_pos = enemy.get_rect()
enemy_vel = 500
enemy_dt = 2
last_enemy = 0 
enemy_hitbox = enemy_pos

# contador de vidas
life = pygame.image.load("ary/imagens/coracao.png")
life_count = 3

# contador de tempo
sec = 0
count = 0
font = pygame.font.Font(None, 42)

# projéteis
p = []
pickle = pygame.image.load("ary/imagens/pickle.png")
pickle_dt = 0.5
last_pickle = 0

# projétieis inimigos
pe = []
pew = pygame.image.load("ary/imagens/pew.png")
pew_dt = 1.5
last_pew = 0

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
        if time - last_pickle > pickle_dt:
            projetil = pygame.Rect(player_pos.right, player_pos.centery - 15, 5,10)
            p.append(projetil)
            last_pickle = time

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
    pygame.draw.rect(janela, (255, 0, 0, 100), player_pos, width=1)
    
    # tiro
    for tiro in p:
        tiro.x += 600 * dt
        janela.blit(pickle, tiro)
    
    # inimigo
    time = pygame.time.get_ticks() / 1000
    for enemy_pos in enemies:
        enemy_pos.x -= enemy_vel * dt
        janela.blit(enemy, enemy_pos)
        pygame.draw.rect(janela, (255, 0, 0), enemy_pos, width=1)

    if time - last_enemy > enemy_dt:
        x = l
        y = random.randint(25, h - enemy.get_width())
        enemy_pos = enemy.get_rect(topleft=(x, y))
        enemies.append(enemy_pos)
        last_enemy = time

    # tiro inimigo
    if time - last_pew > pew_dt:
        tiro_inimigo = pygame.Rect(enemy_pos.left, enemy_pos.centery - 15, 5, 10)
        pe.append(tiro_inimigo)
        last_pew = time

    for laser in pe:
        laser.x -= 950 * dt
        janela.blit(pew, laser)
        

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
        janela.blit(life, (c*40+1130,25))

    pygame.display.flip()

pygame.quit()