mascotas = ["Pedro", "Pablo", "Pepin", "Peluso"]
print(mascotas)

print(mascotas [0])
print(mascotas [1])
print(mascotas [2])
print(mascotas [3])


mascotas[0] = "Bicho"  #Cambiamos el valor del primer elemento de la lista por bicho
print(mascotas)
print(mascotas [0])


print(mascotas [0:2])   # Nos entregan los elementos desde el principio hasta el que le indiquemos
print(mascotas [:2])  #Si no ponemos nada al principio nos coge desde el principio

print(mascotas [2:])  # Si no ponemos nada al final pues nos toma hasta el final

print(mascotas [-2]) # Sí le indicamos un índice negativonos va cogiendo los valoresdesde el finalpara atrás

print(mascotas [::2])  # Muestra los elementos pares solamente, Los toma de manera alternativa va cogiendo de 2 en dos

print(mascotas [1::2]) 

print(mascotas [1:2:2])

numeros = list(range(21))

print(numeros)

print(numeros [1::2])  # Entrega impares
print(numeros [::2])   # Entrega pares empezando por el 0

print(numeros [2::2])   # Entrega pares empezando por el 2

