# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=32030

### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Excepción base: try except            si hay un try  tiene que haber un except como mínimo   // en este caso no hacemos nada con el error

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally       // en este caso no hacemos nada con el error seguimos haciendo cosas


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo                   captura de excepciones po tipo    // en este caso capturamos el error concreto


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción                       // en este caso capturamos el error y lo podemos manejar


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:                                 # mete el error en una variable
    print(error)
except Exception as my_random_error_name:                   # exception es un error generico, sea el error que sea, se controla y se puede manejar alternativa
    print(my_random_error_name)