from classes import Zumbi,Jogador,Pizza,Coca_cafe
from main import *

def cria_Paredes(grid):
        Paredes = []
        x=y=0
        for linha in grid:
            for coluna in linha:
                if coluna =='P':
                    Paredes.append(Parede((x,y)))
                x+=32
            y+=32
            x=0
        return Paredes


Levels = []

grid_1=[
    'PPPPPPPPPPPPPPPPPPPP',
    'P------------------P',
    'P-PPPPPPP--PPPPPPP-P',
    'P-P--------------P-P',
    'P-P-PPPP----PPPP-P-P',
    'P-P----PPPPPP----P-P',
    'P-P-P----------P-P-P',
    'P-P-P--P-PP-P--P-P-P',
    'P-P-P--P-------P-P-P',
    'P-P----PPPPP-----P-P',
    'P-P-PPP------PPP-P-P',
    'P-P---P------P---P-P',
    'P-PPPPPPP--PPPPPPP-P',
    'P------------------P',
    'PPPPPPPPPPPPPPPPPPPP'
]

porta1 = Porta(18*32,1*32)
Paredes1 = cria_Paredes(grid_1)
jogador_coord_init1 = [1*32, 13*32]  #x_inicial, y_inicial,
jogador1 = Jogador(jogador_coord_init1, 10, porta1, Paredes1)  # coordenadas e velocidade

#A ordem dos zumbis vão de cima p/ baixo no mapa 1 - o Segundo é o zumbi no canto
Zumbis1 = [Zumbi(32, 32, 10, Paredes1, movimento_x=True),Zumbi(18*32, 13*32, 10, Paredes1, movimento_y=True),Zumbi(32*6, 9*32, 10, Paredes1, movimento_y=True,direcao_y = -1),Zumbi(14*32, 5*32, 10, Paredes1, movimento_y=True),Zumbi(11*32, 6*32, 10, Paredes1, movimento_y=True),Zumbi(12*32, 11*32, 10, Paredes1, movimento_x=True,direcao_x=-1)]

Pizzas1 = [Pizza(9*32+8, 3*32+8,),Pizza(5*32+8, 5*32+8),Pizza(12*32+8, 10*32+8)]
cracha1 = Cracha(10*32+8, 6*32+8)
Mapa1 = [Paredes1, porta1, jogador1, Zumbis1, Pizzas1, cracha1]
Levels.append(Mapa1)

grid_2=[
    'PPPPPPPPPPPPPPPPPPPP',
    'P------------------P',
    'P--PP--PP--PP--PP--P',
    'P--PP--PP--PP--PP--P',
    'P------------------P',
    'P------P-PPPP------P',
    'P--PP--P-P--P--PP--P',
    'P------P-P-PP------P',
    'P--PP--P---PP--PP--P',
    'P------PPPPPP------P',
    'P------------------P',
    'P--PP--PP--PP--PP--P',
    'P--PP--PP--PP--PP--P',
    'P------------------P',
    'PPPPPPPPPPPPPPPPPPPP'
]

porta2 = Porta(11*32,6*32)
Paredes2 = cria_Paredes(grid_2)
jogador_coord_init2 = [18*32, 12*32]  #x_inicial, y_inicial,
jogador2 = Jogador(jogador_coord_init2, 10, porta2, Paredes2)  # coordenadas e velocidade
Zumbis2 = [Zumbi(5*32,13*32, 10, Paredes2, movimento_y = True, direcao_y= -1), Zumbi(6*32, 1*32, 10, Paredes2, movimento_y = True),Zumbi(13*32,13*32, 10, Paredes2, movimento_y = True, direcao_y= -1), Zumbi(14*32, 1*32, 10, Paredes2, movimento_y = True), Zumbi(2*32, 1*32, 10, Paredes2, movimento_y = True),Zumbi(2*32, 6*32, 10, Paredes2, movimento_y = True),Zumbi(2*32, 11*32, 10, Paredes2, movimento_y = True),Zumbi(17*32, 5*32, 10, Paredes2, movimento_y = True, direcao_y=-1),Zumbi(17*32, 9*32, 10, Paredes2, movimento_y = True, direcao_y=-1), Zumbi(17*32, 13*32, 10, Paredes2, movimento_y = True, direcao_y=-1), Zumbi(1*32, 13*32, 10, Paredes2, movimento_x = True),Zumbi(8*32, 13*32, 10, Paredes2, movimento_x = True), Zumbi(14*32, 13*32, 10, Paredes2, movimento_x = True), Zumbi(17*32, 1*32, 10, Paredes2, movimento_x = True, direcao_x = -1),Zumbi(10*32, 1*32, 10, Paredes2, movimento_x = True, direcao_x = -1), Zumbi(3*32, 1*32, 10, Paredes2, movimento_x = True, direcao_x = -1)]
Pizzas2 = [Pizza(5*32+8, 2*32+8),Pizza(15*32+8, 4*32+8),Pizza(10*32+8, 10*32+8)]
cracha2 = Cracha(4*32+8, 7*32+8)
Mapa2 = [Paredes2, porta2, jogador2, Zumbis2, Pizzas2, cracha2]
Levels.append(Mapa2)

grid_3=[
    'PPPPPPPPPPPPPPPPPPPP',
    'P-----------P------P',
    'PPPP--PPP---P----PPP',
    'P-----P-P---P----P-P',
    'P-PPPPP-P---P----P-P',
    'P-------PP--P----P-P',
    'P-PPPPPPP---PP--PP-P',
    'P-P---------P----P-P',
    'P-P--PPPPPPPP-P--P-P',
    'P-P-----------P--P-P',
    'P-PPPPPPPPPPPPPP-P-P',
    'P------P---------P-P',
    'P------PPPPPPPPPPP-P',
    'P------------------P',
    'PPPPPPPPPPPPPPPPPPPP'
]

porta3 = Porta(18*32,1*32)
Paredes3 = cria_Paredes(grid_3)
jogador_coord_init3 = [18*32, 13*32]  #x_inicial, y_inicial,
jogador3 = Jogador(jogador_coord_init3, 10, porta3, Paredes3)  # coordenadas e velocidade
Zumbis3 = [Zumbi(1*32, 11*32, 10, Paredes3, movimento_x=True,direcao_x = -1),Zumbi(10*32, 4*32, 10, Paredes3, movimento_y=True,direcao_y = -1),Zumbi(11*32, 5*32, 10, Paredes3, movimento_x=True,direcao_y = 1),Zumbi(16*32, 7*32, 10, Paredes3, movimento_y=True,direcao_y = 1),Zumbi(2*32, 13*32, 10, Paredes3, movimento_x=True,direcao_x = -1),Zumbi(3*32, 16*32, 10, Paredes3, movimento_x=True,direcao_x = 1),Zumbi(4*32, 13*32, 10, Paredes3, movimento_x=True,direcao_x = -1),Zumbi(5*32, 16*32, 10, Paredes3, movimento_x=True,direcao_x = 1),]
Pizzas3 = [Pizza(2*32+8, 1*32+8),Pizza(7*32+8, 5*32+8)]
Cocas3 = [Coca_cafe(10*32+8, 11*32+8)]
Cracha3 = Cracha(5*32+8, 7*32+8)
Mapa3 = [Paredes3, porta3, jogador3, Zumbis3, Pizzas3, Cracha3, Cocas3]
Levels.append(Mapa3)

#Esse aqui é o de Ismael
grid_4=[
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
porta4 = Porta(608,416)
Paredes4 = cria_Paredes(grid_4)
jogador_coord_init4 = [64, 416]  #x_inicial, y_inicial,
jogador4 = Jogador(jogador_coord_init4, 10, porta4, Paredes4)  # coordenadas e velocidade
Zumbis4 = [Zumbi(32, 64, 10, Paredes4, movimento_y=True),Zumbi(200, 32, 10, Paredes4, movimento_x=True),Zumbi(32, 400, 10, Paredes4, movimento_y=True,direcao_y = -1),Zumbi(224, 352, 10, Paredes4, movimento_x=True),Zumbi(384, 224, 10, Paredes4, movimento_y=True),Zumbi(160, 224, 10, Paredes4, movimento_y=True),Zumbi(512, 256, 10, Paredes4, movimento_x=True),Zumbi(512, 384, 10, Paredes4, movimento_x=True),Zumbi(544, 128, 10, Paredes4, movimento_x=True)]
Pizzas4 = [Pizza(480+8, 64+8),Pizza(320+8, 160+8),Pizza(128+8, 416+8)]
Cocas4 = [Coca_cafe(288+8, 288+8)]
cracha4 = Cracha(192+8, 32+8)
Mapa4 = [Paredes4, porta4, jogador4, Zumbis4, Pizzas4, Cocas4, cracha4]
Levels.append(Mapa4)

#Tá vazio pq não pensei em nada bom ainda
grid_5=[
    'PPPPPPPPPPPPPPPPPPPP',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'P------------------P',
    'PPPPPPPPPPPPPPPPPPPP'
]

















