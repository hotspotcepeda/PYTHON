# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###                 -->                            identificamos nuestro codigo en un hambito de actuacion

# identificamos nuestro codigo en un hambito
# Las class se definen en CamelCase     buenas practicas

# Definición

class MyEmptyPerson:                # Solo en esto ya está definida la clase
    pass                            # Para poder dejar la clase vacía porque si no lo ponemos una clase vacia da un error 


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas


class Person:                       # clase objeto persona
    def __init__(self, name, surname, alias="Sin alias"):          # el __init__ es un constructor de clase   self se refiere a la instancia , asignamos propiedadas
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)
