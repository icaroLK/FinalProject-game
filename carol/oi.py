import pygame
from pygame.locals import *
from sys import exit

def iniciar_jogo():

    largura = 1280
    altura = 720

    pygame.init()

    screen = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption('Ricks')
    

    pygame.font.init()
    font = pygame.font.Font('carol/Minecraft.ttf', 60)
    text = font.render("Bem-vindo ao jogo Ricks", True, (255, 255,255))
    shadow_text = font.render("Bem-vindo ao jogo Ricks", True, (0, 0, 0))

    text_rect = text.get_rect()
    text_rect.center = (largura/2, altura/2)

    shadow_text_rect = shadow_text.get_rect()  
    shadow_text_rect.center = (largura/2 + 5, altura/2 + 5)

    background_image = pygame.image.load('carol/bg.jpg')

    button_color = (255,255,255)  
    button_rect = pygame.Rect(largura/2 - 50, altura/2 + 50, 100, 50)
    button_font = pygame.font.Font('carol/Minecraft.ttf', 24)
    button_text = button_font.render("Iniciar", True, (0, 0, 0))
    button_text_rect = button_text.get_rect(center=button_rect.center)

    def iniciar_jogo():
        print("O jogo começou!")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        if event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    iniciar_jogo()

        screen.blit(background_image, [0, 0])
        screen.blit(shadow_text, shadow_text_rect)
        screen.blit(text, text_rect)

        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(button_text, button_text_rect)

        pygame.display.update()

