from classes import Zumbi,Jogador,Pizza,Coca_cafe
from main import *
#zumbies/pizzas/coca/player


zumbi_1_1 = Zumbi(100, 30, 10,
               movimento_y=True)
zumbi_1_2 = Zumbi(300, 30, 10,
               movimento_y=True)
zumbi_1_3 = Zumbi(400, 30, 10,
               movimento_y=True)



jogador_1 = Jogador(640 // 2, 480 // 2, 10)  # x_inicial, y_inicial, velocidade

 
# Pizzas e Coca café
pizza_1_1 = Pizza(400, 300)  # x_inicial, y_inicial, coletada = False
pizza_1_2 = Pizza(400, 100)  # x_inicial, y_inicial, coletada = False
coca_1 = Coca_cafe(50, 100)  # x_inicial, y_inicial, coletada = False

leveit=[[zumbi_1_1,zumbi_1_2,zumbi_1_3],[pizza_1_1,pizza_1_2],[coca_1],[jogador_1]]

print(zumbi_1_1.cor)

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