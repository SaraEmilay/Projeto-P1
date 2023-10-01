import pygame
import random
from classes import*
from leveis import Levels, gera_mapas
from os import path


Levels = Levels
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (150, 150, 150)
VERDE=	(0,255,0)

pygame.init()
LARGURA, ALTURA = 640, 480
#criando botoes

botao_credito=Botao("Créditos", 150, 64, 155, 275)
botao_jogar=Botao("Jogar", 150, 64, 340, 275 )
botao_historia=Botao("Jogar", 150, 64, 255, 380)
botao_voltar_menu=Botao("Voltar Menu", 150, 64, 240, 390) #Volta para o Menu após os créditos  
botao_reiniciar=Botao("Jogar de novo", 150, 64, 115, 220) #Volta para tela inicial após o player perder todas as vidas
botao_fim=Botao("Encerrar jogo", 150, 64, 370, 220) #Opção de fechar a tela após o player perder todas as vidas    
botao_menu_ganhou=Botao("Voltar Menu", 150, 64, 145, 275) #Opção de jogar novamente após o player vencer o jogo
botao_encerrar_ganhou=Botao("Encerrar jogo", 150, 64, 330, 275)#Opção de fechar a tela após o player vencer o jogo

# Define o título da JANELA e estabelece a taxa de quadros por segundo.
pygame.display.set_caption("O resgate de Marcelinho")
JANELA = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()
FPS = 60

#marcelino
marcelino=Marcelinho(1*32,2*32, 'marcelinho.jpg')

#mudança de tela
configuracao = {
    "Menu_Inicial": True,
    "jogo_iniciado": False,
    "creditos":False,
    "Historia_1":False,
    "Fim do jogo":False,
    "Ganhou_jogo":False
}
som_jogo = pygame.mixer.Sound("musica_jogo.mp3")
som_jogo.play()
volume = 1 # ajuste conforme necessário
som_jogo.set_volume(volume)

# Inicia a reprodução da trilha sonora em loop
som_jogo.play(loops=-1)

def colisoes(jogador, zumbis, pizzas, cocas, cracha, pizzas_possuidas, vidas):
    # Colisão de zumbi e jogador. Se tem pizza, perde uma das pizzas. Se não, perde uma das vidas, desativa qualquer coca-café em efeito e volta para as coordenadas iniciais. Em qualquer um dos casos, fica invulnerável por 2000 milissegundos
    if vidas>0:
        for zumbi in zumbis:
            if jogador.rect.colliderect(zumbi.rect) and not jogador.invulnerabilidade:
                jogador.invulnerabilidade = True
                Jogador.cor = CINZA
                som_ganhou = pygame.mixer.Sound("colisao.mp3")
                som_ganhou.play()
                # pygame.USEREVENT + n, com n entre 0 e 8. Cria um evento. pygame.time.set_timer(evento, t, loops = 0) é uma função que coloca na fila de eventos o evento dado como argumento, que irá se repetir a cada t milissegundos um número de vezes igual ao número de loops(infinitas, se não der argumento ou for 0)
                PERDER_INVULNERABILIDADE = pygame.USEREVENT + 0
                pygame.time.set_timer(PERDER_INVULNERABILIDADE, 2000, 1)
                if pizzas_possuidas > 0:
                    pizzas_possuidas -= 1
                else:
                    vidas -= 1
                    for zumbi in zumbis:
                        zumbi.velocidade = zumbi.velocidade_base 
                    jogador.rect.x, jogador.rect.y = jogador.x_inicial, jogador.y_inicial # Retorna o jogador a posição predefinida.
        #Colisão entre pizza e jogador
        for pizza in pizzas:
            if jogador.rect.colliderect(pizza.rect) and not pizza.coletada:
                pizza.coletada = True  # Faz a Pizza desaparecer e não poder ser coletada mais vezes
                pizzas_possuidas += 1
                som_ganhou = pygame.mixer.Sound("pegar.mp3")
                som_ganhou.play()

        # Colisão entre coca café e jogador. Faz os zumbis se moverem com metade da velocidade pelos próximos 10 segundos.
        if len(cocas) != 0:
            for coca_cafe in cocas:
                if jogador.rect.colliderect(coca_cafe.rect) and not coca_cafe.coletada:
                    coca_cafe.coletada = True  # Faz a coca_cafe desaparecer e não poder ser coletada mais vezes
                    som_ganhou = pygame.mixer.Sound("pegar.mp3")
                    som_ganhou.play()
                    for zumbi in zumbis:
                        zumbi.velocidade *= 1/2
                    FIM_DO_BONUS = pygame.USEREVENT + 1
                    pygame.time.set_timer(FIM_DO_BONUS, 10000, 1)

    if jogador.rect.colliderect(cracha.rect) and not cracha.coletada:
            cracha.coletada = True  # Faz o crachá desaparecer e não poder ser coletada mais vezes
            jogador.tem_cracha = True
            som_ganhou = pygame.mixer.Sound("pegar.mp3")
            som_ganhou.play()
            
    return pizzas_possuidas, vidas


# Quando o jogador perde as 3 vidas(a ser debatido), ele regressa a posição inicial(consequência da colisão com zumbi), volta a ter 3 vidas e velocidade 10, os zumbis e coletáveis voltam a seus estados inicais.
def reiniciar(jogador, zumbis, pizzas, cocas, cracha):
    jogador.invulnerabilidade = False
    Jogador.cor = BRANCO
    vidas = 3
    jogador.velocidade = 10
    jogador.tem_cracha = False
    cracha.coletada = False
    for zumbi in zumbis:
        zumbi.rect.x, zumbi.rect.y = zumbi.x_inicial, zumbi.y_inicial
    for pizza in pizzas:
        pizza.coletada = False
    for coca_cafe in cocas:
        coca_cafe.coletada = False
    return vidas 

def ganhou():
    global configuracao
    
    som_ganhou = pygame.mixer.Sound("ganhou.wav")
    som_ganhou.play()
    som_jogo.stop()
    background_ganhou = pygame.image.load("tela_final jogo.jpg")
    tamanho_background_ganhou = pygame.transform.scale(background_ganhou,(640, 480))


    
    
    m_rodando = True
    
    while m_rodando:
        JANELA.blit(tamanho_background_ganhou, (0, 0))
        pygame.time.delay(50)
        relogio.tick(FPS)
        if botao_menu_ganhou.draw():
            m_rodando = False
            configuracao["Ganhou_jogo"]=False
            configuracao["Menu_Inicial"]=True
        if botao_encerrar_ganhou.draw():
            m_rodando = False
            configuracao["Ganhou_jogo"]=False
            configuracao["Fim do jogo"]=True
            pygame.quit()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  
                m_rodando = False

                pygame.quit()
        JANELA.blit(tamanho_background_ganhou, (0, 0))
        pygame.display.update()



def menu_inicial():

    global configuracao
    background_menu_inicial = pygame.image.load("tela_inicial jogo.jpg")
    tamanho_background_menu_incial = pygame.transform.scale(background_menu_inicial,(640, 480))

    m_rodando = True
    
    while m_rodando:

        pygame.time.delay(50)
        relogio.tick(FPS)
        if botao_jogar.draw():
            m_rodando = False
            configuracao["Historia_1"]=True
            configuracao["Menu_Inicial"]=False
        if botao_credito.draw():
            m_rodando = False
            configuracao["Menu_Inicial"]=False
            configuracao["creditos"]=True

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  
                m_rodando = False

                pygame.quit()
        JANELA.blit(tamanho_background_menu_incial, (0, 0))
        pygame.display.update()

def creditos():
    global configuracao
    background_creditos = pygame.image.load("tela_creditos jogo.jpg")
    tamanho_background_creditos = pygame.transform.scale(background_creditos, (640, 480))
    m_rodando = True
    
    while m_rodando:

        pygame.time.delay(50)
        relogio.tick(FPS)
        if botao_voltar_menu.draw():
            m_rodando = False
            configuracao["creditos"]=False
            configuracao["Menu_Inicial"]= True


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  
                m_rodando = False

                pygame.quit()
        JANELA.blit(tamanho_background_creditos, (0, 0))
        pygame.display.update()

def historia_1():
    global configuracao
    background_historia = pygame.image.load("tela_historia jogo.jpg")
    tamanho_background_historia = pygame.transform.scale(background_historia,(640, 480))
    m_rodando = True
    
    while m_rodando:
        JANELA.blit(tamanho_background_historia, (0, 0))
        pygame.time.delay(50)
        relogio.tick(FPS)
        if botao_historia.draw():
            m_rodando = False
            configuracao["Historia_1"]=False
            configuracao["jogo_iniciado"]= True


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  
                m_rodando = False

                pygame.quit()

        JANELA.blit(tamanho_background_historia, (0, 0))
        pygame.display.update()

def rodar_jogo(Levels):

    continuar = True
    level_atual = 0
    vidas = 3
    pizzas_possuidas = 0
    while continuar: 
        nivel = gera_mapas(*Levels[level_atual])
        paredes = nivel[0]
        porta = nivel[1]
        jogador = nivel[2]
        zumbis = nivel[3]
        pizzas = nivel[4]
        cocas = nivel[5]
        cracha = nivel[6]
        print(level_atual)
        print(jogador.passou_de_fase)
        fim_de_nivel = False
        while not fim_de_nivel:
            fonte_contador = pygame.font.Font(None, 20)
            texto_contador = fonte_contador.render("Pizza:" + str(pizzas_possuidas) + "       Vidas:" + str(vidas) + '         Crachá:' + str(jogador.tem_cracha), True, BRANCO)
            pygame.time.delay(50)
            relogio.tick(FPS)
            # Condição de interromper código
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_de_nivel = True
                    continuar = False
                    configuracao["jogo_iniciado"]=False
                    configuracao["Fim do jogo"]=True
                    pygame.quit()
                if evento.type == pygame.USEREVENT + 0:
                    jogador.invulnerabilidade = False
                    Jogador.cor = BRANCO
                if evento.type == pygame.USEREVENT + 1:
                    for zumbi in zumbis:
                        zumbi.velocidade = zumbi.velocidade_base 
            # Controla o movimento do jogador, dos zumbis, testa colisões e avalia se o jogo terminou. Então, redesenha a janela de acordo.
            comandos = pygame.key.get_pressed()
            jogador.movimento(comandos, LARGURA, ALTURA)
            for zumbi in zumbis:
                zumbi.movimento()
            pizzas_possuidas, vidas = colisoes(jogador, zumbis, pizzas, cocas, cracha, pizzas_possuidas, vidas)
            #colide marcelino
            
                       
            if jogador.passou_de_fase and level_atual < 4:
                level_atual += 1
                som_porta = pygame.mixer.Sound("som_porta.mp3")
                som_porta.play()
                fim_de_nivel = True

            JANELA.fill(PRETO)
            for parede in paredes:
                #pygame.draw.rect(JANELA,(80,9,200), parede.rect)
                parede.desenhar(JANELA)
            for zumbi in zumbis:
                #pygame.draw.rect(JANELA, Zumbi.cor, zumbi.rect)  # quadrado verde-zumbi
                zumbi.desenhar(JANELA)

            if level_atual <4 :
                #pygame.draw.rect(JANELA, porta.cor, porta.rect)
                porta.desenhar(JANELA)
            elif level_atual==4 and not cracha.coletada:
                #pygame.draw.rect(JANELA, porta.cor, porta.rect)
                porta.desenhar(JANELA)
                    
            if len(cocas) != 0:
                for coca_cafe in cocas:
                    if not coca_cafe.coletada:
                        #pygame.draw.coca_cafe()
                        coca_cafe.desenhar(JANELA)
            for pizza in pizzas:
                if not pizza.coletada:
                    #pygame.draw.rect(JANELA, Pizza.cor, pizza.rect)  # retângulo pizza
                    pizza.desenhar(JANELA)
            if not cracha.coletada:
                #pygame.draw.rect(JANELA,Cracha.cor, cracha.rect)
                cracha.desenhar(JANELA)

            #pygame.draw.rect(JANELA, (Jogador.cor), jogador.rect)  # JANELA, cor, tamanho
            jogador.desenhar(JANELA)

            if level_atual==4:
                #pygame.draw.rect(JANELA, (Marcelinho.cor), marcelino.rect)
                marcelino.desenhar(JANELA)
                if jogador.rect.colliderect(marcelino.rect):
                    continuar = False
                    fim_de_nivel = True
                    configuracao["Ganhou_jogo"]=True
                    configuracao["jogo_iniciado"]=False
                    
            if vidas == 0:
                
                if botao_reiniciar.draw():
                    pizzas_possuidas = 0
                    vidas = reiniciar(jogador, zumbis, pizzas, cocas, cracha)
                    level_atual = 0
                    fim_de_nivel = True
                    
                    
                    
                if botao_fim.draw():

                    configuracao["jogo_iniciado"]=False
                    configuracao["Fim do jogo"]=True
                    pygame.quit()
                botao_menu =pygame.image.load("menu_inicial_botao.png")
                botao_imagem_1 = pygame.transform.scale(botao_menu, (180, 160))
                JANELA.blit(botao_imagem_1, (100, 180))   

                botao_encerrar =pygame.image.load("fecar_jogo_botao.png")
                botao_imagem_2 = pygame.transform.scale(botao_encerrar, (180, 160))
                JANELA.blit(botao_imagem_2, (360, 180))  

            JANELA.blit(texto_contador, [32, 32])
            pygame.display.update()

rodando=True

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    JANELA.fill(PRETO)  # Limpa a tela
    if configuracao["Menu_Inicial"]==True:
        menu_inicial()
    elif configuracao["creditos"]==True:
        creditos()
    elif configuracao["Historia_1"]==True:
        historia_1()
    elif configuracao["jogo_iniciado"]==True:
        rodar_jogo(Levels)
    elif configuracao["Fim do jogo"]==True:
        rodando=False
    elif configuracao["Ganhou_jogo"]==True:
        ganhou()

        
    pygame.display.update()


pygame.quit()
