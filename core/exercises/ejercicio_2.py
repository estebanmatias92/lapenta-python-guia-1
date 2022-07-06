print("")
print(
    "2. Leer el nombre y los dos apellidos de una persona (en tres cadenas de caracteres diferentes) y unirlo en una unica cadena. Luego muestre:"
)
print("\n")

first_name = input("Ingrese nombre: ")
last_name = input("Ingrese apellido: ")
second_last_name = input("Ingrese segundo apellido: ")
print("")

print("Nombre: " + first_name)
print("Apellido: " + last_name)
print("Segundo Apellido: " + second_last_name)

print("\n\n")


# Ejercicio 2.a
print("\t a. La cadena resultante")
print("")

name = " ".join([first_name, last_name, second_last_name])
print("\t Nombre completo: " + name)

print("\n\n")


# Ejercicio 2.b
print("\t b. La cantidad de caracteres resultante")
print("")

char_count = str(len(name))
print("\t Total de caracteres: " + char_count)

print("\n\n")


# Ejercicio 2.c
print("\t c. Convierta todo su contenido a mayusculas y minusculas")
print("")

uppercase = name.upper()
lowercase = name.lower()
print("\t Mayusculas: " + uppercase)
print("\t Minusculas: " + lowercase)

print("\n\n")


# Ejercicio 2.d
print('\t d. Verifique si la cadena "Fernandez" se encuentra en el texto')
print("")

target = "Fernandez"
print(
    "\t "
    + target
    + " "
    + ("se" if target in name else "no se")
    + " encuentra en '"
    + name
    + "'"
)

print("\n\n")


# Ejercicio 2.e
print("\t e. Muestre en Mayusculas la primera letra de cada palabra")
print("")

# name_list = name.split()
# capitalized_list = [word.capitalize() for word in name_list]
# print("\t Palabras capitalizadas: " + " ".join(capitalized_list))
print(
    "\t Palabras capitalizadas: " + " ".join(word.capitalize() for word in name.split())
)

print("\n\n")
