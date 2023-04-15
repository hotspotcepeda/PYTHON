"""   
numero = 1
while numero < 100: # Evalúa la condición de verdadero o falso que le estamos dando si es verdadero continúa si es falso se detiene
    print(numero)
    numero *= 2
    
# En este ejemplo simulamos un intérprete de comandos en la terminal con el dólar e imprimimos los comandos 
# que va introduciendo al usuario cuando el usuario introduce el comando salir se termina la ejecución
# Tenga en cuentaque hasta que no escribimos salir con minúsculas no se termina la ejecución 

comando = ""

while comando != "salir":    
    comando = input("$ ")
    print(comando)
    
comando = ""

while True:         # aquí estoy generando un bucle infinito La aplicación del terminal se va a ejecutar de manera continua
# hasta que la cancelemos con control+c
    comando = input("$ ")
    print(comando)
    
# Es muy importante siempre que te preparamos un LOOP tener una salida ESCAPE porque si no se estará ejecutando hasta el fin de los tiempos y nos joderá la vida
  
comando = ""
while True:          # Aquí lo corrijo colocando un if 
                    
    comando = input("$ ")
    print(comando)
    if comando.lower () == "salir":
        break
"""
# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=23822 https://youtu.be/Kp4Mvapo5kc?t=23822 https://youtu.be/Kp4Mvapo5kc?t=23822 https://youtu.be/Kp4Mvapo5kc?t=23822



### Loops ###

# While

my_condition = 11

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

