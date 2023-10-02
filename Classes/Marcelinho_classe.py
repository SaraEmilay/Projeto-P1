import pygame
class Marcelinho:
    cor = (12, 155, 23)

    def __init__(self, x_inicial, y_inicial, imagem, coletada=False):
        self.rect = pygame.Rect(x_inicial, y_inicial, 20, 20)
        self.coletada = coletada
        self.carrega_imagem =pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.carrega_imagem, (20, 20))

    def desenhar(self, janela):
        janela.blit(self.imagem, (self.rect.x, self.rect.y))