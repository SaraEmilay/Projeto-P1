import pygame
class Porta():
    cor = (255, 0, 0)

    def __init__(self, x, y, imagem):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.carrega_imagem =pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.carrega_imagem, (32, 32))

    def desenhar(self, janela):
        janela.blit(self.imagem, (self.rect.x, self.rect.y))