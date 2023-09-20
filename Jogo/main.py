import pygame
import random

pygame.init()
largura, altura = 600, 400

#Player
x = largura // 2  # Inicializa x no centro da tela
y = altura // 2   # Inicializa y no centro da tela
velocidade = 10

#Zumbi 1
xz1 = 100
yz1 = 30
velocidade_z = 10
direcao_y = 1  # Inicializa a direção vertical para baixo

#Zumbi 2
xz2 = 100
yz2 = 30
velocidade_z = 10
direcao_x = 1  # Inicializa a direção vertical para baixo

#Coca café
xc = 50
yc = 100

#Define o título da janela
pygame.display.set_caption("O resgate de Marcelinho")

janela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

def colisao(xc1, yc1, xc2, yc2):
    return (xc1 == xc2) and (yc1 == yc2)

def rodar_jogo(x, y, xz1, yz1, direcao_y, xz2, yz2, direcao_x, xc, yc, velocidade):
    fim_jogo = False
    while not fim_jogo:
        pygame.time.delay(50)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True

        comandos = pygame.key.get_pressed() 
        if comandos[pygame.K_UP] and y > 0:
            y -= velocidade
        if comandos[pygame.K_DOWN] and y < altura - 20:
            y += velocidade
        if comandos[pygame.K_RIGHT] and x < largura - 20:
            x += velocidade
        if comandos[pygame.K_LEFT] and x > 0:
            x -= velocidade
        
        #Colisão entre player e coca-cafe
        if colisao(x, y, xc, yc):
            velocidade += 10
            xc = -1000 #uma tentativa de fazer a coca-café sumir após a colisão
            yc = -1000


        #Colisão entre player e zumbis
        if colisao(x, y, xz1, yz1) or colisao(x, y, xz2, yz2):
            x, y = largura // 2, altura // 2

        # Movimentação zumbi 1 (vertical)
        yz1 += velocidade_z * direcao_y
        if yz1 <= 0 or yz1 >= altura - 20:
            direcao_y *= -1

        # Movimentação zumbi 2 (horizontal)
        xz2 += velocidade_z * direcao_x
        if xz2 <= 0 or xz2 >= largura - 20:
            direcao_x *= -1


        janela.fill((0, 0, 0))
        player = pygame.draw.rect(janela, (0, 255, 0), (x, y, 20, 20))  #janela, cor, tamanho
        zumbi1 = pygame.draw.rect(janela, (255, 255, 255), (xz1, yz1, 20, 20)) #quadrado branco
        zumbi2 = pygame.draw.rect(janela, (255, 255, 255), (xz2, yz2, 20, 20)) #quadrado branco
        coca_cafe = pygame.draw.rect(janela, (139, 69, 19), (xc, yc, 10, 10)) #retangulo marrom
        pygame.draw.circle(janela, (255, 255, 0), (200, 200), 7) #circulo amarelo
        pygame.draw.circle(janela, (255, 255, 0), (400, 300), 7) #circulo amarelo
        pygame.display.update()

rodar_jogo(x, y, xz1, yz1, direcao_y, xz2, yz2, direcao_x, xc, yc, velocidade)
#atualizações
pygame.quit()
