import pygame

#Metaclasse que irá pertmitir iterações sobre as outras classes(Zumbi, Pizza e Coca_cafe)
class Iterador(type):
    def __iter__(cls):
        return iter(cls._registro)

#Classe do Jogador, com único método movimento.
class Jogador:
    cor = (255, 255, 255)
    def __init__(self, x_inicial, y_inicial, velocidade, vidas = 3):
        self.rect = pygame.Rect(x_inicial,y_inicial, 32, 32)    
        self.velocidade = velocidade
        self.vidas = vidas

    def movimento(self, comandos, LARGURA, ALTURA):        
        self.dx = 0
        self.dy = 0
        if comandos[pygame.K_UP] and self.rect.y > 32:
            self.dy = -self.velocidade
        if comandos[pygame.K_DOWN] and self.rect.y < ALTURA - 32:
            self.dy = self.velocidade
        if comandos[pygame.K_RIGHT] and self.rect.x < LARGURA - 32:
            self.dx = self.velocidade
        if comandos[pygame.K_LEFT] and self.rect.x > 32:
            self.dx = -self.velocidade
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.colisao(Parede.paredes)

    def colisao(self,paredes):
        for parede in paredes:
            if self.rect.colliderect(parede.rect):
                if self.dx > 0:  # Movendo para a direita
                    self.rect.right = parede.rect.left
                elif self.dx < 0:  # Movendo para a esquerda
                    self.rect.left = parede.rect.right
                if self.dy > 0:  # Movendo para baixo
                    self.rect.bottom = parede.rect.top
                elif self.dy < 0:  # Movendo para cima
                    self.rect.top = parede.rect.bottom
#Classe dos Zumbis. É iterável, e possui como método o movimento.
class Zumbi(metaclass = Iterador):
    _registro = []
    cor = (105, 131, 98)

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
        self.velocidade = velocidade

    #Antes de movimentar, checa se a instância possui movimento na determinada direção. No futuro será substituído por movimento em rotas.    
    def movimento(self, LARGURA, ALTURA):
        if self.mov_x:
            self.rect.x += self.direcao_x * self.velocidade
            if self.rect.x <= 32 or self.rect.x >= LARGURA - 64:
                self.direcao_x *= -1
        if self.mov_y:
            self.rect.y += self.direcao_y * self.velocidade
            if self.rect.y <= 32 or self.rect.y >= ALTURA - 64:
                self.direcao_y *= -1
#Classe das Pizzas, Iterável. self.coletada serve para garantir que os efeitos de coleta e a impressão só ocorram se a pizza não tiver sido coletada.
class Pizza(metaclass = Iterador):
    _registro = []
    cor = (212, 155, 23)
    def __init__(self, x_inicial, y_inicial, coletada = False):
        self._registro.append(self)
        self.rect = pygame.Rect(x_inicial, y_inicial, 15, 15)
        self.coletada = coletada

#Classe das Coca_cafe, idêntica a pizza.
class Coca_cafe(metaclass = Iterador):
    _registro = []
    cor = (111, 78, 55)
    def __init__(self, x_inicial, y_inicial, coletada = False):
        self._registro.append(self)
        self.rect = pygame.Rect(x_inicial, y_inicial, 10, 10)
        self.coletada = coletada

class Parede(object):
    paredes=[]
    def __init__(self,posicao):
        Parede.paredes.append(self)
        self.rect=pygame.Rect(posicao[0],posicao[1],32,32)
mapa=[
    'PPPPPPPPPPPPPPPPPPPP',
    'P------------------P',
    'P-----PPPP---------P',
    'P--------P---------P',
    'P------------------P',
    'P------------------P',
    'P-----------PP-----P',
    'P------------P-----P',
    'P------------P-----P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
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


    