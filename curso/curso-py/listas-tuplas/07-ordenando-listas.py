numeros = [2, 4, 7, 66, 33, 3, 5, 100]

numeros.sort()   # Ordena los elementos del array de menor a mayor
print(numeros)

numeros.sort(reverse=True)   # Ordena los elementos del array de mayor a menor
print(numeros)


# nos devuelve una lista nueva Sin alterar la existente
numeros2 = sorted(numeros)
print(numeros)
print(numeros2)

# nos devuelve una lista nueva Sin alterar la existente esta vez ordena inversa
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [
    ["pancho", 4],
    ["pincho", 1],
    ["puncho", 9],
    ["pencho", 2]
]
print(usuarios)

usuarios.sort()     # Ordenalos elementos
print(usuarios)


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)     # Ordenalos elementos por key
print(usuarios)


# def ordena(elemento):
#     return elemento[1]


## Ordenalos elementos por key en reverse
# usuarios.sort(key=ordena, reverse=True)
# print(usuarios)
