# CALCULA A ÁREA DE UM CIRCULO

from math import pi

def calcula_area_circulo(raio):
    return round(pi * raio ** 2, 2)

##################################################

# CALCULA A ÁREA DE UM TRIÂNGULO

def calcula_area_triangulo(base, altura):
    return round((base * altura) / 2, 2)

##################################################

# CALCULA A ÁREA DE UM RETÂNGULO

def calcula_area_retangulo(base, altura):
    return base * altura

##################################################

# GERA MATRIZ ALEATÓRIA

import random

def gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = random.randint(intervalo_inicial, intervalo_final)
            linha.append(valor)
        matriz.append(linha)
    return matriz

##################################################

# CALCULA TRAÇO DA MATRIZ

def calcula_traco_matriz(matriz):
    traco = 0
    for i in range(len(matriz)):
        traco += matriz[i][i]
    return traco
