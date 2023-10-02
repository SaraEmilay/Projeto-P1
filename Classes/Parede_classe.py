import pygame
class Parede(object):
    paredes = []
    cor = (100, 217, 65)

    def __init__(self, posicao, imagem):
        Parede.paredes.append(self)
        self.rect = pygame.Rect(posicao[0], posicao[1], 32, 32)
        self.carrega_imagem =pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.carrega_imagem, (32, 32))

    def desenhar(self, janela):
        janela.blit(self.imagem, (self.rect.x, self.rect.y))