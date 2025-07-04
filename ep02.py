from TestaFuncao import *

linhas_usuario = int(input("Informe a linha da matriz desejada: "))
colunas_usuario = int(input("Informe a coluna da matriz desejada: "))
intervalo_inicial_usuario = int(input("Informe o intervalo inicial para geração dos elementos da matriz desejada: "))
intervalo_final_usuario = int(input("Informe o intervalo final para geração dos elementos da matriz desejada: "))

M = gera_matriz_aleatoria(linhas_usuario, colunas_usuario, intervalo_inicial_usuario, intervalo_final_usuario)
print(f"Matriz gerada: {M}")

if len(M) == len(M[0]):
    traco_matriz_usuario = calcula_traco_matriz(M)
    print(f"O valor do traço da matriz gerada é {traco_matriz_usuario}")
else:
    print("Não é possível calcular o valor do traço da matriz gerada.")
