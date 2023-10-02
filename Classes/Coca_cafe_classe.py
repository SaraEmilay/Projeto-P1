import pygame
class Coca_cafe():
    cor = (111, 78, 55)

    def __init__(self, x_inicial, y_inicial, imagem, coletada=False):
        self.rect = pygame.Rect(x_inicial, y_inicial, 10, 10)
        self.coletada = coletada
        self.carrega_imagem =pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.carrega_imagem, (15, 20))

    def desenhar(self, janela):
        janela.blit(self.imagem, (self.rect.x, self.rect.y))