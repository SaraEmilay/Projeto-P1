import pygame
import random
from classes import*


PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

pygame.init()
LARGURA, ALTURA = 640, 480

# Player
jogador = Jogador(64, 416, 10)  # x_inicial, y_inicial, velocidade

# Zumbis
zumbi_1_1 = Zumbi(32, 64, 10,
               movimento_y=True)  # x_inicial, y_inicial, velocidade, movimento_x = False, movimento_y, direcao_x = 1, direcao_y = 1
zumbi_1_3 = Zumbi(200, 32, 10,
               movimento_x=True)  # x_inicial, y_inicial, velocidade, movimento_x, movimento_y = False, direcao_x = 1, direcao_y = 1
zumbi_1_2 = Zumbi(32, 400, 10,
               movimento_y=True,direcao_y = -1)
zumbi_1_6 = Zumbi(224, 352, 10,
               movimento_x=True)
zumbi_1_5 = Zumbi(384, 224, 10,
               movimento_y=True)
zumbi_1_4 = Zumbi(160, 224, 10,
               movimento_y=True)
zumbi_1_8 = Zumbi(512, 256, 10,
               movimento_x=True)
zumbi_1_7 = Zumbi(512, 384, 10,
               movimento_x=True)
zumbi_1_9 = Zumbi(544, 128, 10,
               movimento_x=True)
# Pizzas e Coca café
pizza1 = Pizza(480+8, 64+8)  # x_inicial, y_inicial, coletada = False
pizza2 = Pizza(320+8, 160+8)  # x_inicial, y_inicial, coletada = False
pizza3 = Pizza(128+8, 416+8)  # x_inicial, y_inicial, coletada = False
coca = Coca_cafe(288+8, 288+8)  # x_inicial, y_inicial, coletada = False

# Define o título da JANELA e estabelece a taxa de quadros por segundo.
pygame.display.set_caption("O resgate de Marcelinho")
JANELA = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()
FPS = 60


def colisoes(placar):
    # Colisão de zumbi e jogador
    for zumbi in Zumbi:
        if jogador.rect.colliderect(zumbi.rect):
            jogador.vidas -= 1
            jogador.velocidade = 10
            jogador.rect.x, jogador.rect.y = 64, 416  # Retorna o jogador a posição predefinida.
    # Colisão entre pizza e jogador
    for pizza in Pizza:
        if jogador.rect.colliderect(pizza.rect) and not pizza.coletada:
            pizza.coletada = True  # Faz a Pizza desaparecer e não poder ser coletada mais vezes
            if jogador.vidas<=2:
                jogador.vidas += 1
            placar += 1
    # Colisão entre coca café e jogador
    for coca_cafe in Coca_cafe:
        if jogador.rect.colliderect(coca_cafe.rect) and not coca_cafe.coletada:
            coca_cafe.coletada = True  # Faz a coca_cafe desaparecer e não poder ser coletada mais vezes
            jogador.velocidade += 10
    return placar


# Quando o jogador perde as 3 vidas(a ser debatido), ele regressa a posição inicial(consequência da colisão com zumbi), volta a ter 3 vidas e velocidade 10, os zumbis e coletáveis voltam a seus estados inicais.
def reiniciar():
    jogador.vidas = 3
    jogador.velocidade = 10
    for zumbi in Zumbi:
        zumbi.rect.x, zumbi.rect.y = zumbi.x_inicial, zumbi.y_inicial
    for pizza in Pizza:
        pizza.coletada = False
    for coca_cafe in Coca_cafe:
        coca_cafe.coletada = False
    return 0


def rodar_jogo():
    fim_jogo = False
    placar = 0
    while not fim_jogo:
        fonte_contador = pygame.font.Font(None, 20)
        texto_contador = fonte_contador.render("Pizza:" + str(placar) + "       Vidas:" + str(jogador.vidas), True,
                                               BRANCO)
        pygame.time.delay(50)
        relogio.tick(FPS)
        # Condição de interromper código
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
        # Controla o movimento do jogador, dos Zumbis, testa colisões e avalia se o jogo terminou. Então, redesenha a janela de acordo.
        comandos = pygame.key.get_pressed()
        jogador.movimento(comandos, LARGURA, ALTURA)
        for zumbi in Zumbi:
            zumbi.movimento(LARGURA, ALTURA)
        placar = colisoes(placar)
        if jogador.vidas == 0:
            placar = reiniciar()

        JANELA.fill(PRETO)
        for parede in Parede.paredes:
            pygame.draw.rect(JANELA,(80,9,200), parede.rect)

        pygame.draw.rect(JANELA, (Jogador.cor), jogador.rect)  # JANELA, cor, tamanho
        for zumbi in Zumbi:
            pygame.draw.rect(JANELA, Zumbi.cor, zumbi.rect)  # quadrado verde-zumbi
        for coca_cafe in Coca_cafe:
            if not coca_cafe.coletada:
                pygame.draw.rect(JANELA, Coca_cafe.cor, coca_cafe.rect)  # retangulo marrom
        for pizza in Pizza:
            if not pizza.coletada:
                pygame.draw.rect(JANELA, Pizza.cor, pizza.rect)  # retângulo pizza
        JANELA.blit(texto_contador, [32, 32])   
        pygame.display.update()


rodar_jogo()

pygame.quit()
