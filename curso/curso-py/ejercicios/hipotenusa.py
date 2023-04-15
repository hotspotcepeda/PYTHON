# Calculadora de hipotenusa en un triangulo rectangulo.
# hipotenusa es = a la suma de los cuarados de los catetos, los catetos son los que hacen el angulo recto.

import math

print("\nBienvenido a la calculadora de hipotenusas de triangulos rectangulos")

cateto_1 = int(input('\nInserte la medida del primer cateto: '))
cateto_2 = int(input('Inserte la medida del segundo cateto: '))

hipotenusa = (math.sqrt((cateto_1 ** 2) + (cateto_2 ** 2)))  
area = ((cateto_1 * cateto_2) / 2)
perimetro = (cateto_1 + cateto_2 + hipotenusa)

print("\nLa hipotenusa mide: ", hipotenusa)
print("El área de este triangulo rectangulo es de: ", area)
print("El perímetro de este triangulo rectangulo es de: ", perimetro)