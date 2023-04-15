numeros  = [1, 2, 3]

primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]

print(primero)
print(segundo)
print(tercero)
print(primero,segundo,tercero)



primer, segun, tercer = numeros  # Hace lo mismo que la parte de arriba pero de una manera más elegante y ortodoxa es como hay que hacerlo

print(primer)
print(segun)
print(tercer)
print(primer,segun,tercer)

primer, *otros = numeros    # Lo que hace con el* es meter el resto de elementos en otra variable que se llama otros

print(primer)
print(otros)


#Para acceder al primer y el segundo elemento de la lista Podemos hacerlo igual

primer, segun, *otros = numeros

print(primer, segun)
print(otros)


#Para acceder al primer y el último elemento de la lista

primer, *otros, ultimo = numeros    

print(primer, ultimo)
print(otros)