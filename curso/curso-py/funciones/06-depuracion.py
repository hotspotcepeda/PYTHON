# Partimos de este caso dónde queremos contar los caracteres del string largo y el resultado que nos entrega es 1 . Lo está haciendo mal

# def largo(texto):
#     resultado = 0
#     for _ in texto:
#         resultado += 1
#         return resultado


# l = largo("Hola mundo")
# print(l)


def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("brakpoint")         # Marcamos con un punto rojo dónde queremos que se detenga el depurador después vamos a la pestaña variablees local función variables largos y hacemos la inspección del documento desde el icono de debug
l = largo("Hola mundo")
print(l)
