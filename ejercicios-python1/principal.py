"""
    @reroes
    Ejemplo de manejo de paquetes
"""
import math
from paquete1.informacion2 import hacer_potencia
from paquete1.informacion import valores # Crear un archivo llamado __init__ dentro de una carpeta para poder importar
#valor 2 elevado a la potencia 2 es igual a 4

for l in valores:
	r = hacer_potencia(l,2)
	int(r)
	print("valor %d elevado a la potencia %d es igual a %d\n" % (l,2,r))
