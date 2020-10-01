# variables

texto = "Master en Python"
texto2 = "con Tono Albiol"
numero = 45
decimal = 9.3

# texto = 1
print(texto)
print(texto2)
print(numero)
print(decimal)

numero = 77
decimal = 8.66
print("____")
print(numero)
print(decimal)

# concatenar
print("*****************")

nombre = "Tono"
apellido = "albiol"
apodo = "Tonoman"
web = f"www.tonoman.es {apodo}"

print(nombre + " " + apellido + " " + web)
print(f"{nombre} {apellido} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))