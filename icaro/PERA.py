import pygame
import random



def fase1():
    pygame.init()

    x = 1280
    y = 720

    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption('Rick and fodase')

    # Carregar imagem de fundo e transformar o tamanho
    bg = pygame.image.load('jogo/images/bg.jpg').convert_alpha()
    bg = pygame.transform.scale(bg, (x, y))

    # Carregar imagem do inimigo e transformar o tamanho
    inimigo = pygame.image.load('jogo/images/velhote.png').convert_alpha()
    inimigo = pygame.transform.scale(inimigo, (90, 63))

    # Carregar imagem do player e transformar o tamanho
    player = pygame.image.load('jogo/images/navepixel.png').convert_alpha()
    player = pygame.transform.scale(player, (90, 50))

    # Carregar imagem do tiro e transformar o tamanho
    tiro = pygame.image.load('jogo/images/pickle.png').convert_alpha()
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


    # Funções
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
        nonlocal pontos
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

        screen.blit(bg, (bg_x, 0))
        
        if pontos <= 5:
            bg_x -= 1
        elif 5 < pontos <= 10:
            bg_x -= 1.3
        elif 10 < pontos <= 15:
            bg_x -= 1.5
        elif 15 < pontos <= 20:
            bg_x -= 1.7
        elif 20 < pontos <= 25:
            bg_x -= 1.9
        else:
            bg_x -= 2
            # Movimentação do inimigo
    pos_inimigo_x -= 2
    if pos_inimigo_x < 0:
        pos_inimigo_x = 1280
        pos_inimigo_y = random.randint(1, 680)

    # Movimentação do tiro
    if triggered:
        pos_x_tiro += vel_x_tiro

    if pos_x_tiro > 1280:
        pos_x_tiro = pos_player_x + 20
        pos_y_tiro = pos_player_y
        triggered = False

    # Atualizar retângulos de colisão
    player_rect.x = pos_player_x
    player_rect.y = pos_player_y
    inimigo_rect.x = pos_inimigo_x
    inimigo_rect.y = pos_inimigo_y
    tiro_rect.x = pos_x_tiro
    tiro_rect.y = pos_y_tiro

    # Colisões
    if colisoes():
        inimigo_rect.x, inimigo_rect.y = respawn()
        tiro_rect.x, tiro_rect.y, triggered, vel_x_tiro = respawn_tiro()

    # Desenhar elementos na tela
    screen.blit(player, (pos_player_x, pos_player_y))
    screen.blit(inimigo, (pos_inimigo_x, pos_inimigo_y))
    if triggered:
        screen.blit(tiro, (pos_x_tiro, pos_y_tiro))

    # Escrever os pontos na tela
    texto_pontos = font.render("Pontos: " + str(pontos), True, (255, 255, 255))
    screen.blit(texto_pontos, (20, 20))

    pygame.display.update()

    # Fim de jogo
    if pontos <= 0:
        rodando = False
        fase2()

def fase2():

    pygame.init()
    x = 1280
    y = 720

    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption('Rick and fodase 2')

    # Carregar imagem de fundo e transformar o tamanho
    bg = pygame.image.load('jogo/images/bg2.jpg').convert_alpha()
    bg = pygame.transform.scale(bg, (x, y))

    # Carregar imagem do inimigo e transformar o tamanho
    inimigo = pygame.image.load('jogo/images/velhote.png').convert_alpha()
    inimigo = pygame.transform.scale(inimigo, (90, 63))

    # Carregar imagem do player e transformar o tamanho
    player = pygame.image.load('jogo/images/navepixel.png').convert_alpha()
    player = pygame.transform.scale(player, (90, 50))

    # Carregar imagem do tiro e transformar o tamanho
    tiro = pygame.image.load('jogo/images/pickle.png').convert_alpha()
    tiro = pygame.transform.scale(tiro, (50, 50))

    # Posição inicial de cada elemento
    pos_inimigo_x = 680
    pos_inimigo_y = 225

    pos_player_x = 65
    pos_player_y = 200

    vel_x_tiro = 0
    pos_x_tiro = 85
    pos_y_tiro = 200

    pontos = 0

    triggered = False

    # Fazer com que as imagens sejam tratadas como retângulos para a colisão
    player_rect = player.get_rect()
    inimigo_rect = inimigo.get_rect()
    tiro_rect = tiro.get_rect()


    # Função que retorna True se ocorrer colisão entre os elementos
    def colisoes():
        if player_rect.colliderect(inimigo_rect):
            return True
        if tiro_rect.colliderect(inimigo_rect):
            return True
        return False

    # Função que define a nova posição do inimigo após a colisão
    def respawn():
        return 1280, random.randint(1, 680)

    # Função que define a nova posição do tiro após a colisão
    def respawn_tiro():
        return pos_player_x + 20, pos_player_y, False, 0

    rodando = True
    while rodando:
        # Configurar taxa de atualização da tela
        clock = pygame.time.Clock()
        clock.tick(60)

        # Capturar eventos do teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    triggered = True
                    vel_x_tiro = 5

        # Desenhar imagem de fundo
        screen.blit(bg, (0, 0))

        # Movimentação do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and pos_player_y > 0:
            pos_player_y -= 2
        if keys[pygame.K_DOWN] and pos_player_y < 720 - player_rect.height:
            pos_player_y += 2

        # Movimentação do inimigo
        pos_inimigo_x -= 2
        if pos_inimigo_x < 0:
            pos_inimigo_x = 1280
            pos_inimigo_y = random.randint(1, 680)

        # Movimentação do tiro
        if triggered:
            pos_x_tiro += vel_x_tiro

        if pos_x_tiro > 1280:
            pos_x_tiro = pos_player_x + 20
            pos_y_tiro = pos_player_y
            triggered = False

        # Atualizar retângulos de colisão
        player_rect.x = pos_player_x
        player_rect.y = pos_player_y
        inimigo_rect.x = pos_inimigo_x
        inimigo_rect.y = pos_inimigo_y
        tiro_rect.x = pos_x_tiro
        tiro_rect.y = pos_y_tiro

        # Colisões
        if colisoes():
            inimigo_rect.x, inimigo_rect.y = respawn()
            tiro_rect.x, tiro_rect.y, triggered, vel_x_tiro = respawn_tiro()

        # Desenhar elementos na tela
        screen.blit(player, (pos_player_x, pos_player_y))
        screen.blit(inimigo, (pos_inimigo_x, pos_inimigo_y))
        if triggered:
            screen.blit(tiro, (pos_x_tiro, pos_y_tiro))

        # Escrever os pontos na tela
        texto_pontos = font.render("Pontos: " + str(pontos), True, (255, 255, 255))
        screen.blit(texto_pontos, (20, 20))

        pygame.display.update()

        # Fim de jogo
        if pontos <= 0:
            rodando = False
            fase2()


fase1()