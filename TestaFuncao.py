import math

def calcula_area_circulo(raio):
    area_circulo = math.pi * raio ** 2
    return round(area_circulo, 2)

##################################################

def calcula_area_triangulo(base, altura):
    area_triangulo = (base * altura) / 2
    return round(area_triangulo, 2)

##################################################

def calcula_area_retangulo(base, altura):
    return base * altura

