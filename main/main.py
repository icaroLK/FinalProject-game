import pygame
import random
from time import sleep

pygame.init()

l = 1280
h = 720
janela = pygame.display.set_mode((l, h))
clock = pygame.time.Clock()
pygame.display.set_caption("Joguinho")
running = True

# background
background = pygame.image.load("main/images/bg.jpg")
back_pos = 0
back_vel = 1000

# game over
game_over = False
tela_game_over = pygame.image.load("main/imagens/gameover.jpg")
progress = 0

# player
player = pygame.image.load("main/imagens/nave.png")
player_pos = player.get_rect(center=(l / 2, h / 2))
player_vel = 500

# inimigos
enemies = []
enemy = pygame.image.load("main/images/velhote.png")
enemy_pos = enemy.get_rect()
enemy_vel = 600
enemy_dt = 2
last_enemy = 0 
enemy_hitbox = enemy.get_rect()

# projeteis
p = []
pickle = pygame.image.load("main/images/pickle.png")
pickle_dt = 0.5
last_pickle = 0

# pontuação
score = 0
score_font = pygame.font.Font("main/Minecraft.ttf", 30)

# contador de vidas
life = pygame.image.load("main/imagens/coracao.png")
life_count = 3

# contador de tempo
sec = 0
count = 0
minutes = 0
counter_font = pygame.font.Font("main/Minecraft.ttf", 30)

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
    

    # tela
    back_pos -= back_vel * dt
    if back_pos < -background.get_width():
        back_pos = 0

    superficie = pygame.Surface((l + background.get_width(), h))
    superficie.blit(background, (back_pos, 0)) 
    superficie.blit(background, (back_pos + background.get_width(), 0))

    janela.fill((0, 0, 0))
    janela.blit(superficie, (0, 0))
    janela.blit(player, player_pos)

    # tiro
    for tiro in p:
        tiro.x += 600 * dt
        janela.blit(pickle, tiro)

        for enemy_pos in enemies:
            if tiro.colliderect(enemy_pos):
                enemies.remove(enemy_pos)
                p.remove(tiro)
                score += 1
                if score == 30:
                    running = False

    # inimigo
    time = pygame.time.get_ticks() / 1000
    for enemy_pos in enemies:
        enemy_pos.x -= enemy_vel * dt
        janela.blit(enemy, enemy_pos)
    
    enemy_hitbox.x = enemy_pos.x
    enemy_hitbox.y = enemy_pos.y

    if time - last_enemy > enemy_dt:
        x = l
        y = random.randint(25, h - enemy.get_width())
        enemy_pos = enemy.get_rect(topleft=(x, y))
        enemies.append(enemy_pos)
        last_enemy = time

    # dano
    for inimigo in enemies:
        if inimigo.colliderect(player_pos):
            life_count -= 1
            enemies.remove(inimigo)
            if life_count == 0:
                if progress < 1:
                    progress += 0.01

                running = False

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
    minutes += 1
    count = int(sec)
    counter_text = counter_font.render('Tempo: ' + str(count), True, (255, 255, 255))
    janela.blit(counter_text, (25,25))

    # contador de pontos
    score_text = score_font.render("Pontos: " + str(score), True, (255, 255, 255))
    janela.blit(score_text, (570, 25))

    # vida
    for c in range(life_count):
        janela.blit(life, (c*40+1130,25))

    pygame.display.flip()

pygame.quit()