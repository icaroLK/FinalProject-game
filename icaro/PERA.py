import pygame
from pygame import mixer
from moviepy.editor import VideoFileClip
import numpy as np
import random




def atirar(tecla):
    global time, projetil, last_pickle
    
    if keys[tecla]:
        time = pygame.time.get_ticks() / 1000
        if time - last_pickle > pickle_dt:
            projetil = pygame.Rect(player_pos.right, player_pos.centery - 15, 5,10)
            p.append(projetil)
            last_pickle = time

def tiro():
    global score, running
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

def dano(dano):
    global game_over, life_count, progress

    for inimigo in enemies:
        if inimigo.colliderect(player_pos):
            life_count -= dano
            enemies.remove(inimigo)
            if life_count == 0:
                if progress < 1:
                    progress += 0.01
                game_over = True

def contador_de_tempo(dt):
    global sec, minutes, count, counter_text

    sec += dt
    minutes += 1
    count = int(sec)
    counter_text = counter_font.render('Tempo: ' + str(count), True, (255, 255, 255))
    janela.blit(counter_text, (25,25))
    return

def posicao_vida():
    global life_pos
    for c in range(life_count):
        life_pos = c*40+1130,25
        janela.blit(life, life_pos)

def posicao_pontos():
    global score_text
    score_text = score_font.render("Pontos: " + str(score), True, (255, 255, 255))
    janela.blit(score_text, (570, 25))

def spawnar_boss():
    global boss_text, boss_text_2

    boss_text = boss_font.render(f"BOSS! Desvie de notas ZERO e colete PYTHONS para vencer!", True, (255, 255, 255))
    boss_text_2 = boss_font.render(f"Colete 5 PYTHONS para dar um TIRO.", True, (255, 255, 255))
    janela.blit(boss_text, (25, 25))
    janela.blit(boss_text_2, (400, 80))
    if boss_pos.x > 900:
        boss_pos.x -= boss_vel * dt
        janela.blit(boss, boss_pos)

def atirar_zeros():
    global zero, last_pew, game_over, life2_count

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

def ALTxLARG(alt, larg):
    global l, h, janela

    l = larg
    h = alt
    janela = pygame.display.set_mode((l, h))

def nome_jogo(nome):
    pygame.display.set_caption(nome)

def clock():
    global clock
    clock = pygame.time.Clock()

def background(diretorio, velocidade):
    global background, back_pos, back_vel

    background = pygame.image.load(diretorio)
    back_pos = 0
    back_vel = velocidade

def player(diretorio, velocidade):
    global player, player_pos, player_vel

    player = pygame.image.load(diretorio)
    player_pos = player.get_rect(center=(l / 2, h / 2))
    player_vel = velocidade

def inimigo(diretorio, velocidade):
    global enemies, enemy, enemy_pos, enemy_vel, enemy_dt, last_enemy, enemy_hitbox

    enemies = []
    enemy = pygame.image.load(diretorio)
    enemy_pos = enemy.get_rect()
    enemy_vel = velocidade
    enemy_dt = 2
    last_enemy = 0 
    enemy_hitbox = enemy.get_rect()

def projeteis(diretorio):
    global p, pickle, pickle_dt, last_pickle

    p = []
    pickle = pygame.image.load(diretorio)
    pickle_dt = 0.5
    last_pickle = 0

def projeteis_inimigos(diretorio):
    global pe, pew, pew_dt, last_pew, pew_hitbox

    pe = []
    pew = pygame.image.load(diretorio)
    pew_dt = 1.5
    last_pew = 0
    pew_hitbox = pew.get_rect()

def imagem_gameover(diretorio):
    global game_over, tela_game_over, progress, go_pos, botao_go, fim, good_final

    game_over = False
    tela_game_over = pygame.image.load(diretorio)
    progress = 0
    botao_go = pygame.image.load("main/images/reiniciar.png")
    go_pos = ((l - botao_go.get_width()) / 2, 570)
    fim = False
    good_final = pygame.image.load("main/images/yw.jpg")

def boss(diretorio, velocidade):
    global boss_font, boss, boss_pos, boss_vel, last_pyt, pythons, zeros, boss_life_count, boss_life

    boss_font = pygame.font.Font("main/Minecraft.ttf", 30)
    boss = pygame.image.load(diretorio)
    boss_pos = boss.get_rect(center=(l+400, h / 2))
    boss_life = pygame.image.load("main/images/cor_boss.png")
    boss_life_count = 3
    boss_vel = velocidade
    last_pyt = 0
    pythons = []
    zeros = []

def vidas(diret1, diret2):
    global life, life2, life_count, life2_count

    life = pygame.image.load(diret1)
    life2 = pygame.image.load(diret2)
    life_count = 3
    life2_count = 5

def pontos(inicial):
    global score, score_2, score_font

    score = inicial
    score_2 = 0
    score_font = pygame.font.Font("main/Minecraft.ttf", 30)

def pagina_inicial():
    global button_color, button_rect, button_font, button_text, button_text_rect, button, font, text, shadow_text, shadow_text_rect, text_rect

    button_color = (255,255,255)
    button_rect = pygame.Rect(l/2 - 50, h/2 + 50, 100, 50)
    button_font = pygame.font.Font('main/Minecraft.ttf', 24)
    button_text = button_font.render("Iniciar", True, (0, 0, 0))
    button_text_rect = button_text.get_rect(center=button_rect.center)
    button = pygame.draw.rect(janela, button_color, button_rect)
    font = pygame.font.Font('main/Minecraft.ttf', 60)
    text = font.render("Bem-vindo ao jogo Rick and Foda-se", True, (255, 255,255))
    shadow_text = font.render("Bem-vindo ao jogo Rick and Foda-se", True, (0, 0, 0))
    shadow_text_rect = shadow_text.get_rect(center=(l/2 + 5, h/2 + 5))  
    text_rect = text.get_rect(center=(l/2, h/2))

def tempos(segundos, contador, minutos):
    global sec, count, minutes, counter_font

    sec = segundos
    count = contador
    minutes = minutos
    counter_font = pygame.font.Font("main/Minecraft.ttf", 30)

def cutscene(diretorio):
    global video, frames, fps, continua

    mixer.music.load("main/sounds/ricksoundtrack.mp3")
    mixer.music.play(-1)
    video = VideoFileClip(diretorio) 
    frames = video.iter_frames()
    fps = 30
    continua = False


def moviment_player():
    global keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= player_vel * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += player_vel * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= player_vel * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_pos.x += player_vel * dt

def limite_tela():
    if player_pos.left < 0:
        player_pos.left = 0
    if player_pos.right > l:
        player_pos.right = l
    if player_pos.top < 0:
        player_pos.top = 0
    if player_pos.bottom > h:
        player_pos.bottom = h


def atualizar_tela():
    global back_pos, superficie

    back_pos -= back_vel * dt
    if back_pos < -background.get_width():
        back_pos = 0

    superficie = pygame.Surface((l + background.get_width(), h))
    superficie.blit(background, (back_pos, 0)) 
    superficie.blit(background, (back_pos + background.get_width(), 0))

    janela.fill((0, 0, 0))
    janela.blit(superficie, (0, 0))
    janela.blit(player, player_pos)


def tiro_final(diretorio, pontos_necessarios):
    global boss_final_baw, baw, baw_dt, last_baw

    boss_final_baw = []
    baw = pygame.image.load(diretorio)
    baw_dt = pontos_necessarios
    last_baw = 0



def spaw_inimigo():
    global x, y, enemy_pos, last_enemy

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


def criar_rect(left, centery, width, height):
    return pygame.Rect(left, centery - 15, width, height)

def tiro_inimigo():
    global pe, last_pew, life_count, game_over

    if time - last_pew > pew_dt:
        tiro_inimigo = criar_rect(enemy_pos.left, enemy_pos.centery, 5, 10)
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





def fase1(pontuação_necessária):
    if score < pontuação_necessária:

        atirar(pygame.K_SPACE)
        tiro()
        spaw_inimigo()


def fase2(pontuação_min, pontuação_max):
    global transicao, background, enemy, pickle

    if score >= pontuação_max:
        return

    if score >= pontuação_min and score <= pontuação_max:
        transicao = True
        background = pygame.image.load('main/imagens/espaco.png')
        enemy = pygame.image.load('main/images/whatugot.png')
        pickle = pygame.image.load("main/imagens/pickle.png")
        tiro_inimigo()















pygame.init()
mixer.init()


running = True
rodando = False
transicao = False




ALTxLARG(720, 1280)

clock()

nome_jogo('Rick and fodase')

background('main/images/bg.jpg', 1000)

player("main/imagens/nave.png", 500)

inimigo("main/images/velhote.png", 600)

projeteis("main/images/pickle.png")

projeteis_inimigos("main/imagens/pew.png")

imagem_gameover("main/imagens/gameover.jpg")

boss("main/imagens/maicris.png", 100)

vidas("main/imagens/coracao.png", "main/imagens/coracao.png")

pontos(0)

pagina_inicial()

tempos(0,0,0)

cutscene("main/video/transition.mp4")

tiro_final("main/images/baw.png", 5)



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
                boss_pos = boss.get_rect(center=(l+400, h / 2))
                boss_vel = 100
                score_2 = 0
                life2_count = 5
                background = pygame.image.load("main/images/bg.jpg")
                pickle = pygame.image.load("main/images/pickle.png")
                enemy = pygame.image.load("main/images/velhote.png")
                pew = pygame.image.load("main/imagens/pew.png")
                p.clear()
                pe.clear()
                enemies.clear()
                boss_final_baw.clear()
                pythons.clear()
                zeros.clear()
                game_over = False
                pygame.mixer.music.play()
            if button_rect[0] < mouse_pos[0] < button_rect[0] + 100 and button_rect[1] < mouse_pos[1] < button_rect[1] + 50:
                rodando = True
                continua = True

    if transicao:
        pygame.mixer.music.pause()
        continua = False
        try:
            frame = next(frames)
            frame = np.rot90(frame)
            frame_surface = pygame.surfarray.make_surface(frame)
            frame_surface = pygame.transform.flip(frame_surface, True, False)
            janela.blit(frame_surface, (0, 0))
            pygame.display.update()
            clock.tick(fps)
        except StopIteration:
            pygame.mixer.music.play()
            transicao = False
            rodando = True
            continua = True
            
    if not rodando:
        janela.blit(background, [0, 0])
        janela.blit(shadow_text, shadow_text_rect)
        janela.blit(text, text_rect)

        pygame.draw.rect(janela, button_color, button_rect)
        janela.blit(button_text, button_text_rect)

    if continua:
        if rodando:
            if fim:
                janela.fill((0, 0, 0))
                janela.blit(good_final, (0, 0)) 

            if game_over:
                janela.fill((0, 0, 0))
                janela.blit(tela_game_over, (0, 0)) 
                janela.blit(botao_go, go_pos)
                pygame.mixer.music.pause()

            elif not game_over and not fim:


                moviment_player()
                atualizar_tela()
                limite_tela()
                time = pygame.time.get_ticks() / 1000

                




                fase1(30)


                fase2(2, 5)





                # fase FINAL
                if score >= 5:
                    # novas variáveis
                    pew = pygame.image.load("main/imagens/zero.png")
                    python = pygame.image.load("main/imagens/python.png")
                    score_2_text =  score_font.render("= " + str(score_2), True, (255, 255, 255))
                    player_vel = 650
                    pew_dt = 0.5

                    # boss
                    spawnar_boss()

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

                    for pitons in pythons:
                        pitons.x -= 1250 * dt
                        janela.blit(python, pitons)
                        if pitons.colliderect(player_pos):
                            score_2 += 1
                            pythons.remove(pitons)

                    if score_2 % 5 == 0:
                        # atirando os projéteis
                        if keys[pygame.K_SPACE]:
                            if time - last_baw > baw_dt:
                                final_baw = pygame.Rect(player_pos.right, player_pos.centery - 15, 5, 10)
                                boss_final_baw.append(final_baw)
                                last_baw = time

                        for b in boss_final_baw:
                            b.x += 600 * dt
                            janela.blit(baw, b)
                            if b.colliderect(boss_pos):
                                boss_life_count -= 1
                                boss_final_baw.remove(b)
                                score_2 = 0
                                if boss_life_count == 0:
                                    fim = True
                    

                    # contador de vidas do boss
                    for c in range(boss_life_count):
                        life_pos = c*40+800, 680
                        janela.blit(boss_life, life_pos)


                    # tela
                    janela.blit(boss, boss_pos)
                    janela.blit(python, (25, 80))
                    janela.blit(score_2_text, (80, 90))

                    # contador de vidas
                    for c in range(life2_count):
                        life_pos = c*40,680
                        janela.blit(life, life_pos)


                        

                dano(1)

                contador_de_tempo(dt)

                posicao_vida()

                posicao_pontos()

    pygame.display.flip()

pygame.quit()

