from classes import*



def gera_mapas(grid, porta_arg, jogador_arg, zumbis_arg, pizzas_arg, cocas_arg, cracha_arg, porta_imagem):
    paredes = cria_paredes(grid)
    porta = Porta(*porta_arg, porta_imagem)
    jogador = Jogador(*jogador_arg, porta, paredes, 'player.png')
    zumbis = []
    for zumbi_arg in zumbis_arg:
        zumbis.append(Zumbi(*zumbi_arg, paredes,'zumbi.png',"tras_personagem.png","frente_personagem.png",porta))
    pizzas = []
    for pizza_arg in pizzas_arg:
        pizzas.append(Pizza(*pizza_arg, 'pizza.png'))
    cocas = []
    if len(cocas_arg) > 0:
        for coca_arg in cocas_arg:
            cocas.append(Coca_cafe(*coca_arg, 'coca.png'))
    cracha = Cracha(*cracha_arg, 'cracha.png')
    return (paredes, porta, jogador, zumbis, pizzas, cocas, cracha)
def cria_paredes(grid):
        paredes = []
        x=y=0
        for linha in grid:
            for coluna in linha:
                if coluna =='P':
                    paredes.append(Parede((x,y), 'parede.jpg'))
                x+=32
            y+=32
            x=0
        return paredes


grid_1=[
    'PPPPPPPPPPPPPPPPPPPP',
    'P-------------------',
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


porta_1 = (19*32,1*32)
porta_imagem_padrao = 'porta.jpg'
jogador_coord_init_1 = (1*32, 13*32)  #x_inicial, y_inicial,
jogador_1 = (jogador_coord_init_1, 10)  # coordenadas e velocidade

#A ordem dos zumbis vão de cima p/ baixo no mapa 1 - o Segundo é o zumbi no canto
zumbis_1 = ((1*32, 1*32, True, False, 1, 1),
           (18*32,12*32, False, True, 1, 1),
           (32*6, 9*32, False, True, 1, -1),
           (14*32, 5*32, False, True, 1, 1),
           (11*32, 6*32, False, True, 1, 1),
           (12*32, 11*32, True, False, -1, 1))
pizzas_1 = [(9*32+8, 3*32+8,),(5*32+8, 5*32+8),(12*32+8, 10*32+8)]
cocas_1 = []
cracha_1 = (10*32+8, 6*32+8)
mapa_1 = (grid_1, porta_1, jogador_1, zumbis_1, pizzas_1, cocas_1, cracha_1, porta_imagem_padrao)


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

porta_2 = (11*32,6*32)
jogador_coord_init_2 = [18*32, 12*32]  #x_inicial, y_inicial,
jogador_2 = (jogador_coord_init_2, 10)  # coordenadas e velocidade
zumbis_2 = [(5*32,13*32, False, True, 1, -1),
           (6*32, 1*32, False, True, 1, 1),
           (13*32,13*32, False, True, 1, -1),
           (14*32, 1*32, False, True, 1, 1),
           (2*32, 1*32, False, True, 1, 1),
           (2*32, 6*32, False, True, 1, 1),
           (2*32, 11*32, False, True, 1, 1),
           (17*32, 5*32,False, True, 1, -1),
           (17*32, 9*32,False, True, 1, -1),
           (17*32, 13*32,False, True, 1, -1),
           (1*32, 13*32,True, False, 1, 1),
           (8*32, 13*32,True, False, 1, 1),
           (14*32, 13*32,True, False, 1, 1),
           (17*32, 1*32,True, False, 1, -1),
           (10*32, 1*32,True, False, 1, -1),
           (3*32, 1*32,True, False, 1, -1)]
pizzas_2 = [(5*32+8, 2*32+8),(15*32+8, 4*32+8),(10*32+8, 10*32+8)]
cocas_2 = []
cracha_2 = (4*32+8, 7*32+8)
mapa_2 = (grid_2, porta_2, jogador_2, zumbis_2, pizzas_2, cocas_2,cracha_2, porta_imagem_padrao)


grid_3=[
    'PPPPPPPPPPPPPPPPPPPP',
    'P-----------P-------',
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

porta_3 = (19*32,1*32)
jogador_coord_init_3 = [18*32, 4*32]  #x_inicial, y_inicial,
jogador_3 = (jogador_coord_init_3, 10)  # coordenadas e velocidade
zumbis_3 = [(3*32, 12*32, True, False, -1, 1),
           (10*32, 4*32, False, True, 1, -1),
           (11*32, 6*32, True, False, 1, 1),
           (16*32, 7*32, False, True, 1, 1),
           (4*32, 13*32, True, False, -1, 1),
           (16*32, 2*32, True, False, 1, 1),
           (16*32, 4*32, True, False, 1, 1),
           (13*32, 3*32, True, False, -1, 1),]
pizzas_3 = [(2*32+8, 1*32+8),(7*32+8, 5*32+8)]
cocas_3 = [(10*32+8, 11*32+8)]
cracha_3 = (5*32+8, 7*32+8)
mapa_3 = (grid_3, porta_3, jogador_3, zumbis_3, pizzas_3, cocas_3, cracha_3, porta_imagem_padrao)


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
porta_4 = (608,416)
jogador_coord_init_4 = [64, 416]  #x_inicial, y_inicial,
jogador_4 = (jogador_coord_init_4, 10)  # coordenadas e velocidade
zumbis_4 = [(32, 64, False, True, 1, 1),
            (200, 32, True, False, 1, 1),
            (32, 400, False, True, 1, -1),
            (224, 352, True, False, 1, 1),
            (384, 224, False, True, 1, 1),
            (160, 224, False, True, 1, 1),
            (512, 256, True, False, 1, 1),
            (512, 384, True, False, 1, 1),
            (544, 128, True, False, 1, 1)]
pizzas_4 = [(192+8, 32+8),(320+8, 160+8),(128+8, 416+8)]
cocas_4 = [(288+8, 288+8)]
cracha_4 =  (480+8, 64+8)
mapa_4 = (grid_4, porta_4, jogador_4, zumbis_4, pizzas_4, cocas_4, cracha_4, porta_imagem_padrao)
# Zumbi(2*32, 13*32, 10, Paredes3, movimento_x=True,direcao_x = -1) #jogador_coord_init3 = [18*32, 4*32]


grid_5=[
    'PPPPPPPPPPPPPPPPPPPP',
    'P--P--------P------P',
    'P----PP---P-P---P-PP',
    'PPPP-P----P-P--P---P',
    'P----PPPP-P-P--P-PPP',
    'PPPP---P--P-PPPP-P-P',
    'P--PPPPPPPP-P----P-P',
    'P-----------P--PPP-P',
    'P-PPP-P-P-PPP------P',
    'P-P-P-P-P-P-P----P-P',
    'P-P-PPPPPPP-PP-P-P-P',
    'P-P-----P---P--PPP-P',
    'P-PP--P-PPP-PP-P---P',
    'P----P---------P---P',
    'PPPPPPPPPPPPPPPPPPPP'
]

porta5 = (3*32,2*32)
#grade_imagem = pygame.image.load('porta_marcelinho.avif')
jogador_coord_init5 = [13*32, 4*32]  #x_inicial, y_inicial,
jogador5 =(jogador_coord_init5, 10,)  # coordenadas e velocidade
zumbis5 = [(6*32, 1*32,True,False,-1,1),
           (14*32, 1*32,True,False,1,-1),
           (9*32, 4*32,False,True,1,1),
           (7*32, 7*32,True,False,1,1),
           (14*32, 8*32,True,False,-1,1),
          (14*32, 6*32,False,True,1,1),
           (18*32, 9*32,False,True,1,-1),
           (1*32, 10*32,False,True,1,1),
           (5*32, 11*32,True,False,1,1),
           (12*32, 13*32,True,False,1,1)
            ]

pizzas5 = [(7*32+8, 9*32+8),(16*32+8, 5*32+8),(16*32+8, 12*32+8), (11*32+8, 9*32+8)]
cocas5 = [(10*32+8, 11*32+8)]
cracha5 = (8*32+8, 5*32+8)
mapa_5 = (grid_5, porta5, jogador5, zumbis5, pizzas5, cocas5, cracha5, porta_imagem_padrao)


Levels = (mapa_1,mapa_2,mapa_3,mapa_4,mapa_5)