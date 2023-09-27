import pygame
import random
from classes import*
from leveis import Levels


PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (150, 150, 150)

pygame.init()
LARGURA, ALTURA = 640, 480
porta = Porta(608,416)
# Player
jogador_coord_init = [64, 416]  #x_inicial, y_inicial,
jogador = Jogador(jogador_coord_init, 10, porta)  # coordenadas e velocidade

# Zumbis
Zumbis = [Zumbi(32, 64, 10,movimento_y=True),Zumbi(200, 32, 10,movimento_x=True),Zumbi(32, 400, 10,movimento_y=True,direcao_y = -1),Zumbi(224, 352, 10,movimento_x=True),Zumbi(384, 224, 10,movimento_y=True),Zumbi(160, 224, 10,movimento_y=True),Zumbi(512, 256, 10,movimento_x=True),Zumbi(512, 384, 10,movimento_x=True),Zumbi(544, 128, 10,movimento_x=True)]

# Pizzas, Coca café e Crachá
Pizzas = [Pizza(480+8, 64+8),Pizza(320+8, 160+8),Pizza(128+8, 416+8)]
Cocas = [Coca_cafe(288+8, 288+8)]
cracha = Cracha(192+8, 32+8)


# Define o título da JANELA e estabelece a taxa de quadros por segundo.
pygame.display.set_caption("O resgate de Marcelinho")
JANELA = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()
FPS = 60


def colisoes(pizzas_possuidas):
    # Colisão de zumbi e jogador. Se tem pizza, perde uma das pizzas. Se não, perde uma das vidas, desativa qualquer coca-café em efeito e volta para as coordenadas iniciais. Em qualquer um dos casos, fica invulnerável por 2000 milissegundos
    for zumbi in Zumbis:
        if jogador.rect.colliderect(zumbi.rect) and not jogador.invulnerabilidade:
            jogador.invulnerabilidade = True
            Jogador.cor = CINZA
            # pygame.USEREVENT + n, com n entre 0 e 8. Cria um evento. pygame.time.set_timer(evento, t, loops = 0) é uma função que coloca na fila de eventos o evento dado como argumento, que irá se repetir a cada t milissegundos um número de vezes igual ao número de loops(infinitas, se não der argumento ou for 0)
            PERDER_INVULNERABILIDADE = pygame.USEREVENT + 0
            pygame.time.set_timer(PERDER_INVULNERABILIDADE, 2000, 1)
            if pizzas_possuidas > 0:
                pizzas_possuidas -= 1
            else:
                jogador.vidas -= 1
                for zumbi in Zumbis:
                    zumbi.velocidade = zumbi.velocidade_base
                jogador.rect.x, jogador.rect.y = jogador.x_inicial, jogador.y_inicial # Retorna o jogador a posição predefinida.
    #Colisão entre pizza e jogador
    for pizza in Pizzas:
        if jogador.rect.colliderect(pizza.rect) and not pizza.coletada:
            pizza.coletada = True  # Faz a Pizza desaparecer e não poder ser coletada mais vezes
            pizzas_possuidas += 1
    # Colisão entre coca café e jogador. Faz os zumbis se moverem com metade da velocidade pelos próximos 10 segundos.
    if len(Cocas) != 0:
        for coca_cafe in Cocas:
            if jogador.rect.colliderect(coca_cafe.rect) and not coca_cafe.coletada:
                coca_cafe.coletada = True  # Faz a coca_cafe desaparecer e não poder ser coletada mais vezes
                for zumbi in Zumbis:
                    zumbi.velocidade *= 1/2
                FIM_DO_BONUS = pygame.USEREVENT + 1
                pygame.time.set_timer(FIM_DO_BONUS, 10000, 1)
    if jogador.rect.colliderect(cracha.rect) and not cracha.coletada:
            cracha.coletada = True  # Faz o crachá desaparecer e não poder ser coletada mais vezes
            jogador.tem_cracha = True
    return pizzas_possuidas


# Quando o jogador perde as 3 vidas(a ser debatido), ele regressa a posição inicial(consequência da colisão com zumbi), volta a ter 3 vidas e velocidade 10, os zumbis e coletáveis voltam a seus estados inicais.
def reiniciar():
    jogador.invulnerabilidade = False
    Jogador.cor = BRANCO
    jogador.vidas = 3
    jogador.velocidade = 10
    jogador.tem_cracha = False
    cracha.coletada = False
    for zumbi in Zumbis:
        zumbi.rect.x, zumbi.rect.y = zumbi.x_inicial, zumbi.y_inicial
    for pizza in Pizzas:
        pizza.coletada = False
    for coca_cafe in Cocas:
        coca_cafe.coletada = False
    return 0


def rodar_jogo():
    continuar = True
    level_atual = 0
    while continuar:
        Paredes = Levels[level_atual][0]
        porta = Levels[level_atual][1]
        jogador = Levels[level_atual][2]
        Zumbis = Levels[level_atual][3]
        Pizzas = Levels[level_atual][4]
        Cocas = Levels[level_atual][5]


    fim_de_nivel = False
    pizzas_possuidas = 0
    while not fim_de_nivel:
        fonte_contador = pygame.font.Font(None, 20)
        texto_contador = fonte_contador.render("Pizza:" + str(pizzas_possuidas) + "       Vidas:" + str(jogador.vidas) + '         Crachá:' + str(jogador.tem_cracha), True, BRANCO)
        pygame.time.delay(50)
        relogio.tick(FPS)
        # Condição de interromper código
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_nivel = True
            if evento.type == pygame.USEREVENT + 0:
                jogador.invulnerabilidade = False
                Jogador.cor = BRANCO
            if evento.type == pygame.USEREVENT + 1:
                for zumbi in Zumbis:
                    zumbi.velocidade = zumbi.velocidade_base
        # Controla o movimento do jogador, dos Zumbis, testa colisões e avalia se o jogo terminou. Então, redesenha a janela de acordo.
        comandos = pygame.key.get_pressed()
        jogador.movimento(comandos, LARGURA, ALTURA)
        for zumbi in Zumbis:
            zumbi.movimento(LARGURA, ALTURA)
        pizzas_possuidas = colisoes(pizzas_possuidas)
        if jogador.vidas == 0:
            pizzas_possuidas = reiniciar()
        if jogador.passou_de_fase:
            level_atual += 1

        JANELA.fill(PRETO)
        for parede in Paredes:
            pygame.draw.rect(JANELA,(80,9,200), parede.rect)

        pygame.draw.rect(JANELA, (Jogador.cor), jogador.rect)  # JANELA, cor, tamanho
        for zumbi in Zumbis:
            pygame.draw.rect(JANELA, Zumbi.cor, zumbi.rect)  # quadrado verde-zumbi
        if len(Cocas) != 0:
            for coca_cafe in Cocas:
                if not coca_cafe.coletada:
                    pygame.draw.rect(JANELA, Coca_cafe.cor, coca_cafe.rect)  # retangulo marrom
        for pizza in Pizzas:
            if not pizza.coletada:
                pygame.draw.rect(JANELA, Pizza.cor, pizza.rect)  # retângulo pizza
        if not cracha.coletada:
            pygame.draw.rect(JANELA,Cracha.cor, cracha.rect)
        pygame.draw.rect(JANELA, Porta.cor, porta.rect)
        JANELA.blit(texto_contador, [32, 32])
        pygame.display.update()


rodar_jogo()

pygame.quit()
