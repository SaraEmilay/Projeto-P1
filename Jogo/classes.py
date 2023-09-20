import pygame

#Metaclasse que irá pertmitir iterações sobre as outras classes(Zumbi, Pizza e Coca_cafe)
class Iterador(type):
    def __iter__(cls):
        return iter(cls._registro)

#Classe do Jogador, com único método movimento.
class Jogador:
    cor = (255, 255, 255)
    def __init__(self, x_inicial, y_inicial, velocidade, vidas = 3):
        self.rect = pygame.Rect(x_inicial,y_inicial, 20, 20)    
        self.velocidade = velocidade
        self.vidas = vidas
    def movimento(self, comandos, LARGURA, ALTURA):        
        if comandos[pygame.K_UP] and self.rect.y > 0:
            self.rect.y = max(0, self.rect.y - self.velocidade)
        if comandos[pygame.K_DOWN] and self.rect.y < ALTURA - 20:
            self.rect.y = min(ALTURA - 20, self.rect.y + self.velocidade)
        if comandos[pygame.K_RIGHT] and self.rect.x < LARGURA - 20:
            self.rect.x = min(LARGURA - 20, self.rect.x + self.velocidade)
        if comandos[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x = max(0, self.rect.x - self.velocidade)

#Classe dos Zumbis. É iterável, e possui como método o movimento.
class Zumbi(metaclass = Iterador):
    _registro = []
    cor = (105, 131, 98)

    #As variáveis x e y iniciais são usadas para criação do retângulo e como coordenadas padrão para onde os zumbis voltarão dps do fim de jogo. Os movimentos são booleanas que avaliam se deve se mover nessa direção(temporário) e as direção(sentido seria mais apropriado?) definem se se movem para um lado ou para o outro. 
    def __init__(self, x_inicial, y_inicial, velocidade, movimento_x = False, movimento_y = False, direcao_x = 1, direcao_y = 1):
        self._registro.append(self)
        self.rect = pygame.Rect(x_inicial, y_inicial, 20, 20)
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
            if self.rect.x <= 0 or self.rect.x >= LARGURA - 20:
                self.direcao_x *= -1
        if self.mov_y:
            self.rect.y += self.direcao_y * self.velocidade
            if self.rect.y <= 0 or self.rect.y >= ALTURA - 20:
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