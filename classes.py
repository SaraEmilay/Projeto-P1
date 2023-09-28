import pygame
from main import*
pygame.init()
#Classe do Jogador, com único método movimento e movimento linear.
class Jogador:
    cor = (255, 255, 255)
    def __init__(self, coordenadas, velocidade, saida, Paredes, vidas = 3):
        self.rect = pygame.Rect(coordenadas[0],coordenadas[1], 23, 23)   
        self.Paredes = Paredes
        self.x_inicial = coordenadas[0]
        self.y_inicial = coordenadas[1] 
        self.velocidade = velocidade
        self.vidas = vidas
        self.invulnerabilidade = False
        self.tem_cracha = False
        self.saida = saida
        self.passou_de_fase = False

    # Primeiramente, avalia qual a direção do movimento em x e em y. Então, chama um método que lida com o movimento unidirecional duas vezes: Uma apenas para x e uma apenas para y.    
    def movimento(self, comandos, LARGURA, ALTURA):        
        self.deslocamento_x = 0
        self.deslocamento_y = 0
        if comandos[pygame.K_UP] and self.rect.y > 32:
            self.deslocamento_y = -self.velocidade
        if comandos[pygame.K_DOWN] and self.rect.y < ALTURA - 32:
            self.deslocamento_y = self.velocidade
        if comandos[pygame.K_RIGHT] and self.rect.x < LARGURA - 32:
            self.deslocamento_x = self.velocidade
        if comandos[pygame.K_LEFT] and self.rect.x > 32:
            self.deslocamento_x = -self.velocidade
        
        if self.deslocamento_x != 0:
            self.movimento_linear(self.deslocamento_x, 0)
        if self.deslocamento_y != 0:
            self.movimento_linear(0, self.deslocamento_y)

    # Método que move em apenas uma direção enquanto checa colisão com as paredes do mapa. 
    def movimento_linear(self, desloc_x, desloc_y):
        self.rect.x += desloc_x
        self.rect.y += desloc_y
        for parede in self.Paredes:
            if self.rect.colliderect(parede.rect):
                if desloc_x > 0:  # Movendo para a direita
                    self.rect.right = parede.rect.left
                elif desloc_x < 0:  # Movendo para a esquerda
                    self.rect.left = parede.rect.right
                if desloc_y > 0:  # Movendo para baixo
                    self.rect.bottom = parede.rect.top
                elif desloc_y < 0:  # Movendo para cima
                    self.rect.top = parede.rect.bottom
        if self.rect.colliderect(self.saida.rect) and not self.tem_cracha:
                if desloc_x > 0:  # Movendo para a direita
                    self.rect.right = self.saida.rect.left
                elif desloc_x < 0:  # Movendo para a esquerda
                    self.rect.left = self.saida.rect.right
                if desloc_y > 0:  # Movendo para baixo
                    self.rect.bottom = self.saida.rect.top
                elif desloc_y < 0:  # Movendo para cima
                    self.rect.top = self.saida.rect.bottom
        elif self.rect.colliderect(self.saida.rect) and self.tem_cracha:
            self.passou_de_fase = True

#Classe dos Zumbis. Possui como método o movimento.
class Zumbi:
    cor = (70,109,67)
    #As variáveis x e y iniciais são usadas para criação do retângulo e como coordenadas padrão para onde os zumbis voltarão dps do fim de jogo. Os movimentos são booleanas que avaliam se deve se mover nessa direção(temporário) e as direção(sentido seria mais apropriado?) definem se se movem para um lado ou para o outro. 
    def __init__(self, x_inicial, y_inicial, movimento_x, movimento_y, direcao_x, direcao_y, Paredes):
        self.rect = pygame.Rect(x_inicial, y_inicial, 32, 32)
        self.Paredes = Paredes
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.mov_x = movimento_x
        self.mov_y = movimento_y
        self.direcao_x = direcao_x
        self.direcao_y = direcao_y
        self.velocidade_base = 10
        self.velocidade = 10

    #Antes de movimentar, checa se a instância possui movimento na determinada direção. No futuro será substituído por movimento em rotas.    
    def movimento(self, LARGURA, ALTURA):
        if self.mov_x:
            self.rect.x += self.direcao_x * self.velocidade
            if self.rect.x <= 32 or self.rect.x >= LARGURA - 64:
                self.direcao_x *= -1
            else:
                self.colisao(self.Paredes)    
        if self.mov_y:
            self.rect.y += self.direcao_y * self.velocidade
            if self.rect.y <= 32 or self.rect.y >= ALTURA - 64:
                self.direcao_y *= -1
            else:
                self.colisao(self.Paredes)        

    def colisao(self,paredes):
        for parede in paredes:
            if self.rect.colliderect(parede.rect):
                if self.mov_x:
                    self.direcao_x *= -1
                    
                if self.mov_y:
                    self.direcao_y *= -1


#Classe das Pizzas, self.coletada serve para garantir que os efeitos de coleta e a impressão só ocorram se a pizza não tiver sido coletada.
class Pizza:
    cor = (212, 155, 23)
    def __init__(self, x_inicial, y_inicial, coletada = False):
        self.rect = pygame.Rect(x_inicial, y_inicial, 15, 15)
        self.coletada = coletada

#Classe das Coca_cafe, idêntica a pizza.
class Coca_cafe:
    cor = (111, 78, 55)
    def __init__(self, x_inicial, y_inicial, coletada = False):
        self.rect = pygame.Rect(x_inicial, y_inicial, 10, 10)
        self.coletada = coletada

#Classe das paredes, cria quadrados de parede onde apropriado, seguindo a grid. Quando formos criar as fases, cada fase irá chamar essa classe e produzir sua própria lista [] iterável, fora do arquivo de classes.
class Parede(object):
    paredes=[]
    cor = (100, 217, 65)
    def __init__(self,posicao):
        Parede.paredes.append(self)
        self.rect=pygame.Rect(posicao[0],posicao[1],32,32)


#Classe do Crachá, igual a pizza.
class Cracha:
    cor = (0, 255, 0)
    def __init__(self, x_inicial, y_inicial, coletada = False):
        self.rect = pygame.Rect(x_inicial, y_inicial, 12, 12)
        self.coletada = coletada

#Classe da saida, ainda faltam informações quanto ao tamanho e tals
class Porta:

    cor = (255, 0, 0)
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        
LARGURA, ALTURA = 640, 480
JANELA = pygame.display.set_mode((LARGURA, ALTURA))
fonte_textos=pygame.font.SysFont('arial', 30)
#classe dos botões
class Botao:

    def __init__ (self, texto,altura,largura,x,y):
        self.rect=pygame.Rect(x,y,altura,largura)
        self.cor_botao=255,255,255

        self.pressionado=False

        self.texto_flutuante= fonte_textos.render(texto,True,(0,0,0))
        self.texto_rect=self.texto_flutuante.get_rect(center=self.rect.center)

    def draw(self):
        pygame.draw.rect(JANELA,(255,255,255),self.rect,border_radius=12)
        JANELA.blit(self.texto_flutuante,self.texto_rect)
        return self.click_verif()

    def click_verif(self):
        self.click=False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.cor_botao=0,8,9
            if pygame.mouse.get_pressed()[0]:
                self.pressionado=True
            else:
                if self.pressionado==True:
                    self.click=True

                    self.pressionado=False                   
        else:
            self.cor_botao=0,200,49
        return self.click
    
