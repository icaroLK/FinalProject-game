import pygame
from pygame import mixer
import random

pygame.init()
mixer.init()

l = 1280
h = 720
janela = pygame.display.set_mode((l, h))
clock = pygame.time.Clock()
pygame.display.set_caption("Rick and Foda-se")
running = True

# background
background = pygame.image.load("main/images/bg.jpg")
back_pos = 0
back_vel = 1000

# game over
game_over = False
tela_game_over = pygame.image.load("main/imagens/gameover.jpg")
progress = 0
botao_go = pygame.image.load("main/images/reiniciar.png")
go_pos = ((l - botao_go.get_width()) / 2, 570)

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

# projétieis inimigos
pe = []
pew = pygame.image.load("ary/imagens/pew.png")
pew_dt = 1.5
last_pew = 0
pew_hitbox = pew.get_rect()

# boss
boss_font = pygame.font.Font("main/Minecraft.ttf", 30)
boss = pygame.image.load("main/imagens/maicris.png")
boss_pos = boss.get_rect(center=(l+400, h / 2))
boss_vel = 100
last_pyt = 0
pythons = []
zeros = []

# tiro final
boss_final_baw = []
baw = pygame.image.load("main/images/baw.png")

# pontuação
score = 0
score_2 = 0
score_font = pygame.font.Font("main/Minecraft.ttf", 30)

# contador de vidas
life = pygame.image.load("main/imagens/coracao.png")
life2 = pygame.image.load("main/imagens/coracao.png")
life_count = 3
life2_count = 5

# contador de tempo
sec = 0
count = 0
minutes = 0
counter_font = pygame.font.Font("main/Minecraft.ttf", 30)

# loading 
mixer.music.load("main/sounds/ricksoundtrack.mp3")
mixer.music.play(-1)
portal = pygame.image.load("main/images/portal.png")
portal_pos = portal.get_rect()
state = 0


while running:
    dt = clock.tick(60) / 1000 

    # fim do jogo 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if go_pos[0] < mouse_pos[0] < go_pos[0] + botao_go.get_width() and go_pos[1] < mouse_pos[1] < go_pos[1] + botao_go.get_height():
                sec = 0
                life_count = 3
                score = 0
                background = pygame.image.load("main/images/bg.jpg")
                pickle = pygame.image.load("main/images/pickle.png")
                enemy = pygame.image.load("main/images/velhote.png")
                pew = pygame.image.load("ary/imagens/pew.png")
                game_over = False
                pygame.mixer.music.play()

    if game_over:
        janela.fill((0, 0, 0))
        janela.blit(tela_game_over, (0, 0)) 
        janela.blit(botao_go, go_pos)
        pygame.mixer.music.pause()

    if not game_over:
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

        # borda
        if player_pos.left < 0:
            player_pos.left = 0
        if player_pos.right > l:
            player_pos.right = l
        if player_pos.top < 0:
            player_pos.top = 0
        if player_pos.bottom > h:
            player_pos.bottom = h 

        time = pygame.time.get_ticks() / 1000

        # fase FINAL
        if score >= 3:
            # novas variáveis
            pew = pygame.image.load("main/imagens/zero.png")
            python = pygame.image.load("main/imagens/python.png")
            score_2_text =  score_font.render("= " + str(score_2), True, (255, 255, 255))
            player_vel = 650
            pew_dt = 1

            # boss
            boss_text = boss_font.render(f"BOSS! Desvie de notas ZERO e colete PYTHONS para vencer!", True, (255, 255, 255))
            janela.blit(boss_text, (25, 25))
            if boss_pos.x > 900:
                boss_pos.x -= boss_vel * dt
                janela.blit(boss, boss_pos)

            # zeros
            if time - last_pew > pew_dt:
                zero = pygame.Rect(boss_pos.left, random.randint(75, 625), 5, 10)
                zeros.append(zero)
                last_pew = time

            for z in zeros:
                z.x -= 1350 * dt
                janela.blit(pew, z)
                if z.colliderect(player_pos):
                    life2_count -= 1
                    zeros.remove(z)
                    if life2_count == 0:
                        game_over = True

            # pythons
            if time - last_pyt > pew_dt:
                pyt = pygame.Rect(boss_pos.left, random.randint(75, 625), 5, 10)
                pythons.append(pyt)
                last_pyt = time

            for p in pythons:
                p.x -= 1250 * dt
                janela.blit(python, p)
                if p.colliderect(player_pos):
                    score_2 += 1
                    pythons.remove(p)
                    if score_2 % 5 == 0:
                        # atirando os projéteis
                        if keys[pygame.K_SPACE]:
                            final_baw = pygame.Rect(player_pos.right, player_pos.centery - 15, 5,10)
                            b.append(final_baw)

                        for b in boss_final_baw:
                            b.x -= 1250 * dt
                            janela.blit(final_baw, b)
                            if b.colliderect(boss_pos):
                                life2_count -= 1
                                boss_final_baw.remove(b)
            
            # tela
            janela.blit(boss, boss_pos)
            janela.blit(python, (25, 80))
            janela.blit(score_2_text, (80, 90))

            # contador de vidas
            for c in range(life2_count):
                life_pos = c*40,680
                janela.blit(life, life_pos)

        # fase 1
        if score < 3:
            # atirando os projéteis
            if keys[pygame.K_SPACE]:
                time = pygame.time.get_ticks() / 1000
                if time - last_pickle > pickle_dt:
                    projetil = pygame.Rect(player_pos.right, player_pos.centery - 15, 5,10)
                    p.append(projetil)
                    last_pickle = time
            
            # tiro
            for tiritos in p:
                tiritos.x += 600 * dt
                janela.blit(pickle, tiritos)

                for enemy_pos in enemies:
                    if tiritos.colliderect(enemy_pos):
                        enemies.remove(enemy_pos)
                        p.remove(tiritos)
                        score += 1
                        if score == 40:
                            running = False

            # inimigo
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

            # fase 2
            if score >= 2:

                background = pygame.image.load("main/imagens/espaco.png")
                pickle = pygame.image.load("main/imagens/pickle.png")
                enemy = pygame.image.load("main/images/whatugot.png")

                # tiro inimigo
                if time - last_pew > pew_dt:
                    tiro_inimigo = pygame.Rect(enemy_pos.left, enemy_pos.centery - 15, 5, 10)
                    pe.append(tiro_inimigo)
                    last_pew = time

                for laser in pe:
                    laser.x -= 1200 * dt
                    janela.blit(pew, laser)
                    if laser.colliderect(player_pos):
                        life_count -= 1
                        pe.remove(laser)
                        if life_count == 0:
                            game_over = True
            
            # dano
            for inimigo in enemies:
                if inimigo.colliderect(player_pos):
                    life_count -= 1
                    enemies.remove(inimigo)
                    if life_count == 0:
                        if progress < 1:
                            progress += 0.01
                        game_over = True

            # vida
            for c in range(life_count):
                life_pos = c*40+1130,25
                janela.blit(life, life_pos)
    

            # contador de tempo
            sec += dt
            minutes += 1
            count = int(sec)
            counter_text = counter_font.render('Tempo: ' + str(count), True, (255, 255, 255))
            janela.blit(counter_text, (25,25))

            # contador de pontos
            score_text = score_font.render("Pontos: " + str(score), True, (255, 255, 255))
            janela.blit(score_text, (570, 25))


    pygame.display.flip()

pygame.quit()

