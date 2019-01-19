from paquete_archivos.miarchivo import *
from paquete_modelo.modelo import *

leer_archivo = MiArchivo()

arreglo = leer_archivo.obtener_informacion()
arreglo = [l.split(",") for l in arreglo]
#creo arreglo de ordenada
ordenada = [] 
#ciclo que recorre el arreglo
for i in arreglo: 
	# for interno en el arreglo
	for n in i : 
		#enlazo los numeros anteriormente strings a lista de ordenada
		ordenada.append(int(n))
#.sort permite ordenamiento
ordenada.sort()
#imprime arreglo ordenado 
print(ordenada)

#creo el objeto de operaciones el cual recibe la lista ordenada
op = Operaciones(ordenada)
#mediante el input hago que el usuario ingrese una cadena que convierto en numero con int para registrar numero a buscar
item = int(input("Que numero desea buscar?\n"))
#int toma el valor y ejecuta la busqueda 
num = (op.Busqueda(item) )
#imprime la posicion de numero ingresado
print("El numero ingresado se encuentra en la posicion: %d" %(num))
