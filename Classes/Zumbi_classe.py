import pygame
class Zumbi():
    cor = (70, 109, 67)

    # As variáveis x e y iniciais são usadas para criação do retângulo e como coordenadas padrão para onde os zumbis voltarão dps do fim de jogo.
    # Os movimentos são booleanas que avaliam se devem mover-se para um lado ou para o outro.
    def __init__(self, x_inicial, y_inicial, movimento_x, movimento_y, direcao_x, direcao_y, Paredes, imagem,
                 imagem_y_tras, imagem_y_frente, saida):
        self.rect = pygame.Rect(x_inicial, y_inicial, 32, 32)
        self.Paredes = Paredes
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.mov_x = movimento_x
        self.mov_y = movimento_y
        self.direcao_x = direcao_x
        self.direcao_y = direcao_y
        self.saida = saida
        self.velocidade_base = 10
        self.velocidade = 10
        self.imagem_frente = imagem_y_frente
        self.imagem_tras = imagem_y_tras

        #Movimento Horizontal
        if movimento_x:
            self.carrega_imagem = pygame.image.load(imagem)
            self.imagem = pygame.transform.scale(self.carrega_imagem, (32, 32))
            if self.direcao_x == -1:
                self.imagem = pygame.transform.flip(self.imagem, True, False)

        #Movimento vertical
        elif movimento_y:
            if self.direcao_y == -1:
                self.carrega_imagem = pygame.image.load(self.imagem_tras)
                self.imagem = pygame.transform.scale(self.carrega_imagem, (32, 32))
            elif self.direcao_y == 1:
                self.carrega_imagem = pygame.image.load(self.imagem_frente)
                self.imagem = pygame.transform.scale(self.carrega_imagem, (32, 32))

    #Antes de movimentar, checa se a instância possui movimento na determinada direção.
    def movimento(self):
        if self.mov_x:
            self.rect.x += self.direcao_x * self.velocidade
            self.colisao(self.Paredes)
        if self.mov_y:
            self.rect.y += self.direcao_y * self.velocidade
            self.colisao(self.Paredes, )

    #Quando colide com uma parede, muda o sentido do movimento
    def colisao(self, paredes):

        for parede in paredes:
            if self.rect.colliderect(parede.rect):
                if self.mov_x : 
                    if self.direcao_x == 1:
                        self.rect.right = parede.rect.left - 1 
                    elif self.direcao_x == -1:
                        self.rect.left = parede.rect.right + 1
                    self.direcao_x *= -1
                    self.imagem=pygame.transform.flip(self.imagem, True, False)
                    
                if self.mov_y:   
                    self.direcao_y *= -1  
                    if self.direcao_y==-1:
                        self.rect.bottom = parede.rect.top - 1
                        self.carrega_imagem =pygame.image.load(self.imagem_tras)
                        self.imagem = pygame.transform.scale(self.carrega_imagem, (32, 32))
                    elif self.direcao_y==1:
                        self.rect.top = parede.rect.bottom + 1
                        self.carrega_imagem =pygame.image.load(self.imagem_frente)
                        self.imagem = pygame.transform.scale(self.carrega_imagem, (32, 32))
                        
        if self.rect.colliderect(self.saida.rect):
            if self.mov_x:
                self.direcao_x *= -1
                self.imagem = pygame.transform.flip(self.imagem, True, False)

            if self.mov_y:
                if self.direcao_y == -1:
                    self.carrega_imagem = pygame.image.load(self.imagem_tras)
                    self.imagem = pygame.transform.scale(self.carrega_imagem, (32, 32))
                elif self.direcao_y == 1:
                    self.carrega_imagem = pygame.image.load(self.imagem_frente)
                    self.imagem = pygame.transform.scale(self.carrega_imagem, (32, 32))

    def desenhar(self, janela):
        janela.blit(self.imagem, (self.rect.x, self.rect.y))

