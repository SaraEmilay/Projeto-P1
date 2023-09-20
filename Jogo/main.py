import pygame
import random
from classes import Iterador, Jogador, Zumbi, Pizza, Coca_cafe

PRETO = (0,0,0)

pygame.init()
LARGURA, ALTURA = 600, 400

#Player
jogador = Jogador(LARGURA // 2, ALTURA // 2, 10) #x_inicial, y_inicial, velocidade

#Zumbis
zumbi1 = Zumbi(100, 30, 10, movimento_y= True) #x_inicial, y_inicial, velocidade, movimento_x = False, movimento_y, direcao_x = 1, direcao_y = 1
zumbi2 = Zumbi(200, 30, 10, movimento_x = True) #x_inicial, y_inicial, velocidade, movimento_x, movimento_y = False, direcao_x = 1, direcao_y = 1


#Pizzas e Coca café
pizza1 = Pizza(200, 200) #x_inicial, y_inicial, coletada = False
pizza2 = Pizza(400, 300) #x_inicial, y_inicial, coletada = False
coca = Coca_cafe(50, 100) #x_inicial, y_inicial, coletada = False


#Define o título da JANELA e estabelece a taxa de quadros por segundo.
pygame.display.set_caption("O resgate de Marcelinho")
JANELA = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()
FPS = 60

def colisoes():
    # Colisão de zumbi e jogador
    for zumbi in Zumbi:
        if jogador.rect.colliderect(zumbi.rect):
            jogador.vidas -= 1 
            jogador.rect.x, jogador.rect.y = LARGURA // 2, ALTURA // 2 #Retorna o jogador a posição predefinida.
    # Colisão entre pizza e jogador
    for pizza in Pizza:
        if jogador.rect.colliderect(pizza.rect) and not pizza.coletada:
            pizza.coletada = True #Faz a Pizza desaparecer e não poder ser coletada mais vezes

    # Colisão entre coca café e jogador
    for coca_cafe in Coca_cafe:
        if jogador.rect.colliderect(coca_cafe.rect) and not coca_cafe.coletada:
            coca_cafe.coletada = True #Faz a coca_cafe desaparecer e não poder ser coletada mais vezes
            jogador.velocidade += 10
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


def rodar_jogo():
    fim_jogo = False
    while not fim_jogo:
        pygame.time.delay(50)
        relogio.tick(FPS)
        #Condição de interromper código
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
        # Controla o movimento do jogador, dos Zumbis, testa colisões e avalia se o jogo terminou. Então, redesenha a janela de acordo.
        comandos = pygame.key.get_pressed() 
        jogador.movimento(comandos, LARGURA, ALTURA)
        for zumbi in Zumbi:
            zumbi.movimento(LARGURA, ALTURA)
        colisoes()
        if jogador.vidas == 0:
            reiniciar()
        
        JANELA.fill(PRETO)
        pygame.draw.rect(JANELA, Jogador.cor, jogador.rect)  #JANELA, cor, tamanho
        for zumbi in Zumbi:
            pygame.draw.rect(JANELA, Zumbi.cor, zumbi.rect) #quadrado verde-zumbi
        for coca_cafe in Coca_cafe:
            if not coca_cafe.coletada:
                pygame.draw.rect(JANELA, Coca_cafe.cor, coca_cafe.rect) #retangulo marrom
        for pizza in Pizza:
            if not pizza.coletada:
                pygame.draw.rect(JANELA, Pizza.cor, pizza.rect) #retângulo pizza
        pygame.display.update()

rodar_jogo()

pygame.quit()
