def conversor(tipo_pesos,valor_dolares):
	pesos = input("Cuantos pesos " + tipo_pesos + " tienens?")
	pesos = float(pesos)
	dolares = pesos/valor_dolares
	dolares =round(dolares,2)
	dolares = str(dolares)
	print("Tienes $"+dolares+" dolares")

menu = """
Bienveido al conversor de monedas

1-Pesos Colombiano
2-Pesos Argentinos
3-Pesos Mexicano

Elige una opcion
"""

opcion = int(input(menu))


if opcion == 1:

	conversor("Colombiano" , 3875)
elif opcion == 2:
		conversor("Argentinos" , 215)

elif opcion == 3:

		conversor("Mexicano" , 24)

else:
	print("Ingrese una opcion")
	pass




