import pygame
import random

def jogo_1():
    pygame.init()

    x = 1280
    y = 720

    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption('Rick and fodase')

    # Carregar imagem de fundo e transformar o tamanho
    bg = pygame.image.load('icaro/tentarjogo/images/bg.jpg').convert_alpha()
    bg = pygame.transform.scale(bg, (x, y))

    # Carregar imagem do inimigo e transformar o tamanho
    inimigo = pygame.image.load('icaro/tentarjogo/images/velhote.png').convert_alpha()
    inimigo = pygame.transform.scale(inimigo, (90, 63))

    # Carregar imagem do player e transformar o tamanho
    player = pygame.image.load('icaro/tentarjogo/images/navepixel.png').convert_alpha()
    player = pygame.transform.scale(player, (90, 50))

    # Carregar imagem do tiro e transformar o tamanho
    tiro = pygame.image.load('icaro/tentarjogo/images/pickle.png').convert_alpha()
    tiro = pygame.transform.scale(tiro, (50, 50))

    # Posição inicial de cada elemento
    pos_inimigo_x = 680
    pos_inimigo_y = 225

    pos_player_x = 65
    pos_player_y = 200

    vel_x_tiro = 0
    pos_x_tiro = 85
    pos_y_tiro = 200

    pontos = 4

    triggered = False

    # Fazer com que o jogo fique aberto e só feche quando clicar no X
    rodando = True

    # Escrever os pontos na tela
    font = pygame.font.SysFont('icaro/tentarjogo/fonts/Minecraft.ttf', 50)


    #escrever os pontos na tela
    font = pygame.font.SysFont('icaro/tentarjogo/fonts/Minecraft.ttf', 50)



    # funcoes
    def respawn():
        x = 1217
        y = random.randint(1, 680)
        return [x, y]

    def respawn_tiro():
        triggered = False
        respawn_tiro_x = pos_player_x + 20
        respawn_tiro_y = pos_player_y
        vel_x_tiro = 0
        return [respawn_tiro_x, respawn_tiro_y, triggered, vel_x_tiro]

    def colisoes():
        global pontos
        if player_rect.colliderect(inimigo_rect) or inimigo_rect.x < 0:
            pontos -= 1
            return True
        elif tiro_rect.colliderect(inimigo_rect):
            pontos += 1
            return True
        else:
            return False

    player_rect = player.get_rect()
    inimigo_rect = inimigo.get_rect()
    tiro_rect = tiro.get_rect()



    bg_x = 0
    bg_width = bg.get_rect().width

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
        
        screen.blit(bg, (bg_x, 0))  # Isso cria um fundo na posição (bg_x, 0)


        if pontos <= 5:
            bg_x -= 1
        elif 5 < pontos <= 10:
            bg_x -= 1.3
        elif 10 < pontos <= 15:
            bg_x -= 1.5
        elif 15 < pontos <= 20:
            bg_x -= 1.7
        else:
            bg_x -= 2




        if bg_x <= -bg_width:
            bg_x = 0

        screen.blit(bg, (bg_x + bg_width, 0))


        vel_nave = 0.7

        #teclas
        tecla = pygame.key.get_pressed()
        if pos_player_y > 1:
            if tecla[pygame.K_w] or tecla[pygame.K_UP]:
                pos_player_y -= vel_nave
                if not triggered:
                    pos_y_tiro -= vel_nave

        if pos_player_y < 670:
            if tecla[pygame.K_s] or tecla[pygame.K_DOWN]:
                pos_player_y += vel_nave
                if not triggered:
                    pos_y_tiro += vel_nave

        if pos_player_x > 0:
            if tecla[pygame.K_a] or tecla[pygame.K_LEFT]:
                pos_player_x -= vel_nave
                if not triggered:
                    pos_x_tiro -= vel_nave

        if pos_player_x < 1200:
            if tecla[pygame.K_d] or tecla[pygame.K_RIGHT]:
                pos_player_x += vel_nave
                if not triggered:
                    pos_x_tiro += vel_nave

        if tecla[pygame.K_SPACE]:
            triggered = True
            vel_x_tiro = 2


        if pontos == -1:
            rodando = False
        


        # respawn
        if pos_inimigo_x < -70 or colisoes():
            pos_inimigo_x = respawn()[0]
            # print(respawn()[0])
            pos_inimigo_y = respawn()[1]
            # print(respawn()[1])

        if pos_x_tiro > 1280:
            pos_x_tiro, pos_y_tiro, triggered, vel_x_tiro = respawn_tiro()


        #posição rects (caixas de colisao)
        player_rect.y = pos_player_y
        player_rect.x = pos_player_x

        tiro_rect.x = pos_x_tiro
        tiro_rect.y = pos_y_tiro

        inimigo_rect.x = pos_inimigo_x
        inimigo_rect.y = pos_inimigo_y









        # movimento / controle do fundo
        
        if pontos <= 5:
            x -= 1
            pos_inimigo_x -= 0.5
        elif 5 < pontos <= 10:
            x -= 1.3
            pos_inimigo_x -= 0.6
        elif 10 < pontos <= 15:
            x -= 1.5
            pos_inimigo_x -= 0.7
        elif 15 < pontos <= 20:
            x -= 1.7
            pos_inimigo_x -= 0.8
        else:
            x -= 2
            pos_inimigo_x -= 1
        



        pos_inimigo_x -= 0.7
        pos_x_tiro += vel_x_tiro


        ####caixa de colisão ative para ver
        # pygame.draw.rect(screen, (225, 0, 0), player_rect, 4)
        # pygame.draw.rect(screen, (225, 0, 0), tiro_rect, 4)
        # pygame.draw.rect(screen, (225, 0, 0), inimigo_rect, 4)

        score = font.render(f'Pontos: {int(pontos)} ', True, (0,0,0))
        screen.blit(score, (50,50))



        #criar imagens
        screen.blit(inimigo, (pos_inimigo_x, pos_inimigo_y))
        screen.blit(tiro, (pos_x_tiro, pos_y_tiro))
        screen.blit(player, (pos_player_x, pos_player_y))
        
        # print(pontos)

        
        pygame.display.update() # isso vai ficar atualizando a tela o tempo todo

