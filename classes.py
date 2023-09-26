import pygame

#Classe do Jogador, com único método movimento e movimento linear.
class Jogador:
    cor = (255, 255, 255)
    def __init__(self, coordenadas, velocidade, vidas = 3):
        self.rect = pygame.Rect(coordenadas[0],coordenadas[1], 23, 23)    
        self.velocidade = velocidade
        self.vidas = vidas
        self.invulnerabilidade = False

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
        for parede in Parede.paredes:
            if self.rect.colliderect(parede.rect):
                if desloc_x > 0:  # Movendo para a direita
                    self.rect.right = parede.rect.left
                elif desloc_x < 0:  # Movendo para a esquerda
                    self.rect.left = parede.rect.right
                if desloc_y > 0:  # Movendo para baixo
                    self.rect.bottom = parede.rect.top
                elif desloc_y < 0:  # Movendo para cima
                    self.rect.top = parede.rect.bottom

#Classe dos Zumbis. Possui como método o movimento.
class Zumbi():
    cor = (1, 217, 65)
    #As variáveis x e y iniciais são usadas para criação do retângulo e como coordenadas padrão para onde os zumbis voltarão dps do fim de jogo. Os movimentos são booleanas que avaliam se deve se mover nessa direção(temporário) e as direção(sentido seria mais apropriado?) definem se se movem para um lado ou para o outro. 
    def __init__(self, x_inicial, y_inicial, velocidade, movimento_x = False, movimento_y = False, direcao_x = 1, direcao_y = 1):
        self._registro.append(self)
        self.rect = pygame.Rect(x_inicial, y_inicial, 32, 32)
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.mov_x = movimento_x
        self.mov_y = movimento_y
        self.direcao_x = direcao_x
        self.direcao_y = direcao_y
        self.velocidade_base = velocidade
        self.velocidade = velocidade

    #Antes de movimentar, checa se a instância possui movimento na determinada direção. No futuro será substituído por movimento em rotas.    
    def movimento(self, LARGURA, ALTURA):
        if self.mov_x:
            self.rect.x += self.direcao_x * self.velocidade
            if self.rect.x <= 32 or self.rect.x >= LARGURA - 64:
                self.direcao_x *= -1
            else:
                self.colisao(Parede.paredes)    
        if self.mov_y:
            self.rect.y += self.direcao_y * self.velocidade
            if self.rect.y <= 32 or self.rect.y >= ALTURA - 64:
                self.direcao_y *= -1
            else:
                self.colisao(Parede.paredes)        

    def colisao(self,paredes):
        for parede in paredes:
            if self.rect.colliderect(parede.rect):
                if self.mov_x:
                    self.direcao_x *= -1
                    
                if self.mov_y:
                    self.direcao_y *= -1


#Classe das Pizzas, self.coletada serve para garantir que os efeitos de coleta e a impressão só ocorram se a pizza não tiver sido coletada.
class Pizza():
    cor = (212, 155, 23)
    def __init__(self, x_inicial, y_inicial, coletada = False):
        self._registro.append(self)
        self.rect = pygame.Rect(x_inicial, y_inicial, 15, 15)
        self.coletada = coletada

#Classe das Coca_cafe, idêntica a pizza.
class Coca_cafe():
    cor = (111, 78, 55)
    def __init__(self, x_inicial, y_inicial, coletada = False):
        self._registro.append(self)
        self.rect = pygame.Rect(x_inicial, y_inicial, 10, 10)
        self.coletada = coletada

#Classe das paredes, cria quadrados de parede onde apropriado, seguindo a grid. Quando formos criar as fases, cada fase irá chamar essa classe e produzir sua própria lista [] iterável, fora do arquivo de classes.
class Parede(object):
    paredes=[]
    cor = (100, 217, 65)
    def __init__(self,posicao):
        Parede.paredes.append(self)
        self.rect=pygame.Rect(posicao[0],posicao[1],32,32)
mapa=[
    'PPPPPPPPPPPPPPPPPPPP',
    'P--P-P-------------P',
    'P-PP-PP-PPPP-PP-PP-P',
    'P------------PPPPP-P',
    'P---P-PPPPPP-------P',
    'P-PPP----P-P-PPP---P',
    'P---P-PPPP-P-P-PPP-P',
    'P-PPP--------P-PPP-P',
    'P---P-P-PPP--------P',
    'P-PPP-P---P-PPP-P-PP',
    'P---P-P-PPP-P-P-P-PP',
    'P-PPP-------P-PPP-PP',
    'P--P--P-P-P-P------P',
    'P--P-PP---P---P--P--',
    'PPPPPPPPPPPPPPPPPPPP'
     
]

x=y=0
for linha in mapa:
    for coluna in linha:
        if coluna =='P':
            Parede((x,y))
        x+=32
    y+=32
    x=0


    