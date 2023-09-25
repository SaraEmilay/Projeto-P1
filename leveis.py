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