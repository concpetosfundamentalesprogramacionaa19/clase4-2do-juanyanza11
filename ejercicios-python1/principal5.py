"""
    @reroes
    Manejo de estructuras
"""

diccionario = {"nombre": "René", "apellidos": "Elizalde"}
diccionario1 = {"nombre": "Luis", "apellidos": "Alvarez"}

lista = [diccionario,diccionario1]
print("Imprimir diccionario")
for l in lista:
	midiccionario = l
	print("Mi nombre es %s y mi apellido es %s" %\
	(midiccionario["nombre"],midiccionario["apellidos"]))
	
