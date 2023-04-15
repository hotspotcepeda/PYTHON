#esto es lo que venimos haciendo 

def suma(a, b):
    resultador = a + b
    print(resultador)
    
suma(1, 2)

#Si queremos obtener el resultado de la función para asignárselo a una variable lo haremos de la siguiente manera 

def suman(a, b):
    resultado = a + b
    return resultado
   
c = suman(2, 3)
d = suman(c, 2)

print(c)
print(d)