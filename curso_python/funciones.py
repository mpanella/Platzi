def imprimir_mensaje():
	print("Mensaje espesial")
	print("Estoy aprendiendo a usar funciones")

def saludar(op):
	print("Hola como estas")
	print("Elegiste la opcion ")

	saludar = "Elegiste la opcion " + str(op)
	print(saludar)
	print("Adios")

def sumar(a,b):
	print("Se suman dos numeros")
	resultado = a + b 
	return resultado



opcion = input("Elige una opcion (1,2,3)  : ")

saludar(opcion)





