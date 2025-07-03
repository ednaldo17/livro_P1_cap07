from TestaFuncao import *

# MOSTRA ABA COM OPÇÕES DE CÁLCULO
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Cálculo das áreas de figuras geométricas:")
print("1. Círculo\n2. Triângulo\n3. Retângulo")
resposta = int(input("Qual figura você deseja calcular a área? "))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# VERIFICA QUAL RESPOSTA FOI ESCOLHIDA
if resposta == 1:
    raio_usuario = float(input("Informe o raio do círculo (cm): ")) # PERGUNTA O RAIO DO CÍRCULO
    circulo = calcula_area_circulo(raio_usuario) # CHAMA A FUNÇÃO DE CALCULAR A ÁREA DO CÍRCULO
    print(f"A área do círculo com raio igual a {raio_usuario} cm é {circulo} cm².") # IMPRIME O RESULTADO DA ÁREA
elif resposta == 2:
    base_triangulo_usuario = float(input("Informe a base do triângulo (cm): ")) # PERGUNTA A BASE DO TRIÂNGULO
    altura_triangulo_usuario = float(input("Informe a altura do triângulo (cm): ")) # PERGUNTA A ALTURA DO TRIÂNGULO
    triangulo = calcula_area_triangulo(base_triangulo_usuario, altura_triangulo_usuario) # CHAMA A FUNÇÃO DE CALCULAR A ÁREA DO TRIÂNGULO
    print(f"A área do triângulo com base {base_triangulo_usuario} cm e altura {altura_triangulo_usuario} cm é {triangulo} cm².") # IMPRIME O RESULTADO DA ÁREA
elif resposta == 3:
    base_retangulo_usuario = float(input("Informe a base do retângulo (cm): ")) # PERGUNTA A BASE DO RETÂNGULO
    altura_retangulo_usuario = float(input("Informe a altura do retângulo (cm): ")) # PERGUNTA A ALTURA DO RETÂNGULO
    retangulo = calcula_area_retangulo(base_retangulo_usuario, altura_retangulo_usuario) # CHAMA A FUNÇÃO DE CALCULAR A ÁREA DO RETÂNGULO
    print(f"A área do retângulo com base {base_retangulo_usuario} cm e altura {altura_retangulo_usuario} cm é {retangulo} cm².") # IMPRIME O RESULTADO DA ÁREA
else:
    print("Opção inválida.") # INFORMA QUE A OPÇÃO DIGITADA É INVÁLIDA
