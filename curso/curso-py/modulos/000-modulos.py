# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=34583

### Modules ### 

# librerias, ficheros de codigo que puedo usar en mi codigo.

# ojo que los ficheros que queremos hacer import no pueden empezar por numeros, 

from math import pi as PI_VALUE
import math
from my_module import sumValue, printValue
import my_module                            # importando un fichero que tengo en la misma carpeta my_module.py

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")


sumValue(5, 3, 1)
printValue("Hola python")


print(math.pi)
print(math.pow(2, 8))


print(PI_VALUE)