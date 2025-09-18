from functools import (reduce)
numeros=[1,2,3,4,5,6,7,8,9]
quadrados = map(lambda n: n**2, numeros)
print(tuple(quadrados))

nomes=["Ana", "Pedro","martha"]
novos_nomes = list(map(lambda nome: "**" + nome + "**", nomes))
print(novos_nomes)

pares = tuple(filter(lambda n: n%2 ==0, numeros))
print(pares)

print(sum(numeros))

print(reduce(lambda t,n: t * n, numeros))

#outra forma de fazer funções lambda
x = lambda arg : arg *2
print(x(2))

#função lambda com operação ternária
y = lambda x: x*2 if x > 10 else x-2
print(y(10))