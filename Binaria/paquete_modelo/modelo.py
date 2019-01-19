class Operaciones(object):
	#Constructor que recibe un arreglo ordenado .sort
	def __init__(self, array):
		self.arreglo = array
	#Metodo de Busqueda Binaria
	def Busqueda(self, item):
		pos = -1 #posicion icia en -1
		menor = 0
		mayor = len(self.arreglo) -1 #mayor tendra el tamanio del arreglo -1 
		mitad = int((menor + mayor +1) /2) #mitad vale lo que tiene: (menor + mayor +1) / 2 
		item_bin = item #asigno el valor de item a item binario
		
		while (menor <= mayor) and (pos == -1): #mientras menor sea menor o igual a mayor y la posicion sea -1 se ejecuta el ciclo
			if(item_bin == self.arreglo[mitad]): #si el item binario es igual al valor que esta en la mitad del arreglo la posicion sera igual a mitad
				pos = mitad
			
			if(item_bin < self.arreglo[mitad]): #si el item binario es menor al valor que esta en la mitad del arreglo, mayor sera igual a mitad +1
				mayor = mitad - 1
			
			else:
				menor = mitad + 1 #sino menor tomara el valor de mitad +1

			mitad = int((menor + mayor +1) / 2) # mitad tomara el  valor de un entero (cambio a entero que por defecto es string) resultante de: (menor + mayor +1) /2
 
		return pos #reorna la posicion del item ingresado