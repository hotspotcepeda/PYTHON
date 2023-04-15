#
def get_product(**datos):   # cuando llamemos a este tipo de funciones tenemos que indicar el parametro
    print(datos)
    
get_product(id="id")

get_product(id="id", 
            name="iPhone",
            description="Esto es un iPhone")

get_product(id="1", 
            name="iPhone",
            description="Esto es un iPhone",
            valoracion="Buena")


def getProduct(**datos):   # cuando llamemos a este tipo de funciones tenemos que indicar el parametro
    print(datos["id"], datos["name"], datos["description"], datos["valoracion"])

getProduct(id="23", 
            name="Samsung",
            description="Esto es un smartphone Samsung",
            valoracion="Buena *** ")