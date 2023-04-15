def suma(a, b):
    print(a + b)
    
suma(1, 1)


def suman(a, b, c):
    print(a + b + c)
    
suman(1, 1, 1)

# xargs permite llamar todos los elementos que queramos

def sumaxargs(*numeros):   # el * transforma los parametros en ITERABLES
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)        # IMPORTANTISIOMO LA IDENTACION
    
sumaxargs(1, 1, 1, 1)
sumaxargs(1, 1, 1, 1, 1)
sumaxargs(1, 1, 1, 1, 1, 1)
sumaxargs(1, 1, 1, 1, 1, 1, 1)
sumaxargs(10000, 222)

