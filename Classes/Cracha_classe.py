import pygame
class Cracha():
    cor = (0, 255, 0)

    def __init__(self, x_inicial, y_inicial, imagem, coletada=False):
        self.rect = pygame.Rect(x_inicial, y_inicial, 12, 12)
        self.coletada = coletada
        self.carrega_imagem =pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.carrega_imagem, (15, 20))

    def desenhar(self, janela):
        janela.blit(self.imagem, (self.rect.x, self.rect.y))