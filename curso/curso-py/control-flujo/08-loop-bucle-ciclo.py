# Cuando nosotros estamos ejecutando el primer for , el codigo se ejecuta de arriba a abajo.
# La primera vez que se ejecuta el for va a tener el valor de cero


# Estamos imprimiendo 4 veces de la j los valores de k que son dos  DANGER cuando usamos muchos datos, valorar otras alternativas al loop anidado


for j in range(4):   # primer for se inicializa en 0  j=0  ---> outer for / loop
    for k in range (2):  # segundo for, se inicializa en 0  k = 0   ---> inner for / loop
        print(f"{j}, {k}")  # En primer lugar imprimimos los valores de j y de k que son cero
        


# nos sirve para iterar 