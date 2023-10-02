import pygame
class Jogador():
    cor = (255, 255, 255)

    def __init__(self, coordenadas, velocidade, saida, Paredes, imagem, vidas=3):
        self.rect = pygame.Rect(*coordenadas, 18, 18)
        self.Paredes = Paredes
        self.x_inicial = coordenadas[0]
        self.y_inicial = coordenadas[1]
        self.velocidade = velocidade
        self.vidas = vidas
        self.invulnerabilidade = False
        self.tem_cracha = 0 
        self.saida = saida
        self.passou_de_fase = False
        self.carrega_imagem = pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.carrega_imagem, (20, 20))



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

    def desenhar(self, janela):
        janela.blit(self.imagem, (self.rect.x, self.rect.y))
