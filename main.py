import pygame
from leveis import Levels, gera_mapas
from Classes.Botão_classe import Botao
from Classes.Cracha_classe import Cracha
from Classes.Parede_classe import Parede
from Classes.Porta_classe import Porta
from Classes.Coca_cafe_classe import Coca_cafe
from Classes.Jogador_classe import Jogador
from Classes.Pizzas_classe import Pizza
from Classes.Marcelinho_classe import Marcelinho
from Classes.Zumbi_classe import Zumbi


Levels = Levels
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

pygame.init()
LARGURA, ALTURA = 640, 480

#Criando botoes
botao_credito=Botao("Créditos", 150, 64, 155, 275)
botao_jogar=Botao("Jogar", 150, 64, 340, 275 )
botao_historia=Botao("Jogar", 150, 64, 255, 380)
botao_voltar_menu=Botao("Voltar Menu", 150, 64, 240, 390) #Volta para o Menu após os créditos  
botao_reiniciar=Botao("Jogar de novo", 150, 64, 115, 220) #Volta para tela inicial após o player perder todas as vidas
botao_fim=Botao("Encerrar jogo", 150, 64, 370, 220) #Opção de fechar a tela após o player perder todas as vidas    
botao_menu_ganhou=Botao("Voltar Menu", 150, 64, 145, 275) #Opção de jogar novamente após o player vencer o jogo
botao_encerrar_ganhou=Botao("Encerrar jogo", 150, 64, 330, 275)#Opção de fechar a tela após o player vencer o jogo

#Define o título da JANELA e estabelece a taxa de quadros por segundo.
pygame.display.set_caption("O resgate de Marcelinho")
JANELA = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()
FPS = 60

#Marcelino
marcelino=Marcelinho(1*32,2*32, './imagens/marcelinho.jpg')

#Mudanças de tela
configuracao = {
    "Menu inicial": True,
    "Jogo iniciado": False,
    "Creditos":False,
    "Historia":False,
    "Fim do jogo":False,
    "Ganhou jogo":False
}
som_jogo = pygame.mixer.Sound("./sons/musica_jogo.mp3")
som_jogo.play()
volume = 0.5 # Ajuste conforme necessário
som_jogo.set_volume(volume)

#Inicia a reprodução da trilha sonora em loop
som_jogo.play(loops=-1)

def colisoes(jogador, zumbis, pizzas, cocas, cracha, pizzas_possuidas, vidas):
    #Colisão de zumbi e jogador:
    #Se tem pizza, perde uma das pizzas e fica invulnerável por 2000ms. Se não, perde uma das vidas, desativa qualquer coca-café em efeito e volta para as coordenadas iniciais.
    if vidas>0:
        
        for zumbi in zumbis:
            
            if jogador.rect.colliderect(zumbi.rect) and not jogador.invulnerabilidade:
                som_ganhou = pygame.mixer.Sound("./sons/colisao.mp3")
                som_ganhou.play()
                
                if pizzas_possuidas > 0:
                    jogador.invulnerabilidade = True
                    jogador.transparencia(150)
                    PERDER_INVULNERABILIDADE = pygame.USEREVENT + 0
                    pygame.time.set_timer(PERDER_INVULNERABILIDADE, 2000, 1)
                    pizzas_possuidas -= 1
                
                else:
                    vidas -= 1
                    for zumbi in zumbis:
                        zumbi.velocidade = zumbi.velocidade_base 
                    jogador.rect.x, jogador.rect.y = jogador.x_inicial, jogador.y_inicial # Retorna o jogador a posição predefinida.
        
        #Colisão entre pizza e jogador:
        for pizza in pizzas:
            
            #Faz a pizza desaparecer e não poder ser coletada mais vezes
            if jogador.rect.colliderect(pizza.rect) and not pizza.coletada:
                pizza.coletada = True 
                pizzas_possuidas += 1
                som_ganhou = pygame.mixer.Sound("./sons/pegar.mp3")
                som_ganhou.play()

        #Colisão entre coca-café e jogador. Faz os zumbis se moverem com metade da velocidade pelos próximos 10s.
        if len(cocas) != 0:

            for coca_cafe in cocas:

                # Faz a coca_cafe desaparecer e não poder ser coletada mais vezes
                if jogador.rect.colliderect(coca_cafe.rect) and not coca_cafe.coletada:
                    coca_cafe.coletada = True
                    som_ganhou = pygame.mixer.Sound("./sons/pegar.mp3")
                    som_ganhou.play()
                    
                    for zumbi in zumbis:
                        zumbi.velocidade *= 1/2
                    FIM_DO_BONUS = pygame.USEREVENT + 1
                    pygame.time.set_timer(FIM_DO_BONUS, 10000, 1)

    #Faz o crachá desaparecer e não poder ser coletada mais vezes
    if jogador.rect.colliderect(cracha.rect) and not cracha.coletada:
            cracha.coletada = True  
            jogador.tem_cracha = 1
            som_ganhou = pygame.mixer.Sound("./sons/pegar.mp3")
            som_ganhou.play()
            
    return pizzas_possuidas, vidas


#Game over: o jogo inteiro é ressetado, todos os objetos e mapas voltam as suas posições iniciais
def reiniciar(jogador, zumbis, pizzas, cocas, cracha):
    
    jogador.invulnerabilidade = False
    jogador.transparencia(255)
    Jogador.cor = BRANCO
    vidas = 3
    jogador.velocidade = 10
    jogador.tem_cracha = 0
    cracha.coletada = False
    
    for zumbi in zumbis:
        zumbi.rect.x, zumbi.rect.y = zumbi.x_inicial, zumbi.y_inicial
    for pizza in pizzas:
        pizza.coletada = False
    for coca_cafe in cocas:
        coca_cafe.coletada = False
    return vidas 

#Parabéns: Tela de parabenização por vencer o jogo e opção de jogar novamente
def ganhou():
    
    global configuracao
    
    som_ganhou = pygame.mixer.Sound("./sons/ganhou.wav")
    som_ganhou.play()
    som_jogo.stop()
    background_ganhou = pygame.image.load("./imagens/tela_final jogo.jpg")
    tamanho_background_ganhou = pygame.transform.scale(background_ganhou,(640, 480))

    #Tela final do jogo incluindo funcionamento dos botões e sobreposição do design estática da tela
    menu_final_rodando = True
    
    while menu_final_rodando:
        
        JANELA.blit(tamanho_background_ganhou, (0, 0))
        pygame.time.delay(50)
        relogio.tick(FPS)

        if botao_menu_ganhou.draw():
            menu_final_rodando = False
            configuracao["Ganhou jogo"]=False
            configuracao["Menu inicial"]=True

        if botao_encerrar_ganhou.draw():
            menu_final_rodando = False
            configuracao["Ganhou jogo"]=False
            configuracao["Fim do jogo"]=True
            pygame.quit()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  
                menu_final_rodando = False

                pygame.quit()

        JANELA.blit(tamanho_background_ganhou, (0, 0))
        pygame.display.update()

#Tela inicial: botões de créditos e início do jogo
def menu_inicial():

    global configuracao
    background_menu_inicial = pygame.image.load("./imagens/tela_inicial jogo.jpg")
    tamanho_background_menu_incial = pygame.transform.scale(background_menu_inicial,(640, 480))

    menu_final_rodando = True
    
    while menu_final_rodando:

        pygame.time.delay(50)
        relogio.tick(FPS)
        
        if botao_jogar.draw():
            menu_final_rodando = False
            configuracao["Historia"]=True
            configuracao["Menu inicial"]=False
        
        if botao_credito.draw():
            menu_final_rodando = False
            configuracao["Menu inicial"]=False
            configuracao["Creditos"]=True

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  
                menu_final_rodando = False

                pygame.quit()
        
        JANELA.blit(tamanho_background_menu_incial, (0, 0))
        pygame.display.update()

#Tela de créditos: Informações acerca dos desenvolvedores do projeto
def creditos():

    global configuracao
    background_creditos = pygame.image.load("./imagens/tela_creditos jogo.jpg")
    tamanho_background_creditos = pygame.transform.scale(background_creditos, (640, 480))
    menu_final_rodando = True
    
    while menu_final_rodando:

        pygame.time.delay(50)
        relogio.tick(FPS)
        
        if botao_voltar_menu.draw():
            menu_final_rodando = False
            configuracao["Creditos"]=False
            configuracao["Menu inicial"]= True

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  
                menu_final_rodando = False

                pygame.quit()

        JANELA.blit(tamanho_background_creditos, (0, 0))
        pygame.display.update()

#Tela contando a história do jogo
def historia():
    
    global configuracao
    background_historia = pygame.image.load("./imagens/tela_historia jogo.jpg")
    tamanho_background_historia = pygame.transform.scale(background_historia,(640, 480))
    menu_final_rodando = True
    
    while menu_final_rodando:
        
        JANELA.blit(tamanho_background_historia, (0, 0))
        pygame.time.delay(50)
        relogio.tick(FPS)
        
        if botao_historia.draw():
            menu_final_rodando = False
            configuracao["Historia"]=False
            configuracao["Jogo iniciado"]= True

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  
                menu_final_rodando = False

                pygame.quit()

        JANELA.blit(tamanho_background_historia, (0, 0))
        pygame.display.update()

#Função mestre: Constrói os mapas e os objetos dentro dele
def rodar_jogo(Levels):

    continuar = True
    level_atual = 4
    vidas = 3
    pizzas_possuidas = 0

    while continuar: 

        #Constróis de instâncias dos objetos
        nivel = gera_mapas(*Levels[level_atual])
        paredes = nivel[0]
        porta = nivel[1]
        jogador = nivel[2]
        zumbis = nivel[3]
        pizzas = nivel[4]
        cocas = nivel[5]
        cracha = nivel[6]
        fim_de_nivel = False

        while not fim_de_nivel:

            fonte_contador = pygame.font.Font(None, 20)
            texto_contador = fonte_contador.render("Pizza:" + str(pizzas_possuidas) + "       Vidas:" + str(vidas) + '         Crachá:' + str(jogador.tem_cracha), True, BRANCO)
            pygame.time.delay(50)
            relogio.tick(FPS)

            #Condição de interromper código
            for evento in pygame.event.get():
                
                #Ao clicar no "X", o jogo fecha
                if evento.type == pygame.QUIT:
                    fim_de_nivel = True
                    continuar = False
                    configuracao["Jogo iniciado"]=False
                    configuracao["Fim do jogo"]=True
                    pygame.quit()
                
                #Tira o efeito invulnerabilidade do jogar após o tempo limite
                if evento.type == pygame.USEREVENT + 0:
                    jogador.invulnerabilidade = False
                    jogador.transparencia(255)
                    Jogador.cor = BRANCO
                
                #Acaba o efeito da coca-café: zumbis voltam a velocidade inicial
                if evento.type == pygame.USEREVENT + 1:
                    for zumbi in zumbis:
                        zumbi.velocidade = zumbi.velocidade_base 
            
            #Controla o movimento do jogador e dos zumbis, testa colisões e avalia se o jogo terminou. Então, redesenha a janela de acordo.
            comandos = pygame.key.get_pressed()
            jogador.movimento(comandos, LARGURA, ALTURA)
            
            for zumbi in zumbis:
                zumbi.movimento()
            pizzas_possuidas, vidas = colisoes(jogador, zumbis, pizzas, cocas, cracha, pizzas_possuidas, vidas)
                               
            if jogador.passou_de_fase and level_atual < 4:
                level_atual += 1
                som_porta = pygame.mixer.Sound("./sons/som_porta.mp3")
                som_porta.play()
                fim_de_nivel = True 

            #Desenhando itens dos mapas
            ## Comentários indicam a versão antiga, quando os mapas eram construídos por quadrados.
            JANELA.fill(PRETO)

            for parede in paredes:
                #pygame.draw.rect(JANELA,(80,9,200), parede.rect)
                parede.desenhar(JANELA)

            for zumbi in zumbis:
                #pygame.draw.rect(JANELA, Zumbi.cor, zumbi.rect)
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
                    configuracao["Ganhou jogo"]=True
                    configuracao["Jogo iniciado"]=False
            
            if vidas == 0:
                
                if botao_reiniciar.draw():
                    pizzas_possuidas = 0
                    vidas = reiniciar(jogador, zumbis, pizzas, cocas, cracha)
                    level_atual = 0
                    fim_de_nivel = True
                   
                if botao_fim.draw():

                    configuracao["Jogo iniciado"]=False
                    configuracao["Fim do jogo"]=True
                    pygame.quit()

                botao_menu = pygame.transform.scale(pygame.image.load("./imagens/menu_inicial_botao.png"), (180, 160))
                JANELA.blit(botao_menu, (100, 180))   

                botao_encerrar = pygame.transform.scale(pygame.image.load("./imagens/fecar_jogo_botao.png"), (180, 160))
                JANELA.blit(botao_encerrar, (360, 180)) 

            JANELA.blit(texto_contador, [32, 32])
            pygame.display.update()

jogo_rodando = True

while jogo_rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    JANELA.fill(PRETO)  # Limpa a tela
    if configuracao["Menu inicial"]==True:
        menu_inicial()
    elif configuracao["Creditos"]==True:
        creditos()
    elif configuracao["Historia"]==True:
        historia()
    elif configuracao["Jogo iniciado"]==True:
        rodar_jogo(Levels)
    elif configuracao["Fim do jogo"]==True:
        jogo_rodando = False
    elif configuracao["Ganhou jogo"]==True:
        ganhou()

    pygame.display.update()

pygame.quit()