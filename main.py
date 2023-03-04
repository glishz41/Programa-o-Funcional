from functools import reduce

# lista de números inteiros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filtrando apenas os números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))

# elevando ao quadrado
quadrados = list(map(lambda x: x ** 2, pares))

# somando todos os elementos
soma = reduce(lambda x, y: x + y, quadrados)

print(soma)
