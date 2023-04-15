# Funciones Landa funciones anónimas

usuarios = [
    ["pancho", 4],
    ["pincho", 1],
    ["puncho", 9],
    ["pencho", 2]
]
print(usuarios)

usuarios.sort(key=lambda el: el[1], reverse=True)     # Ordenalos elementos por key
print(usuarios)


usuarios.sort(key=lambda el: el[1])     # Ordenalos elementos por key
print(usuarios)