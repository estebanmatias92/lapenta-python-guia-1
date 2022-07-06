print("")
print(
    "3. Leer el nombre de una persona y un caracter y comprobar si dicho caracter esta en su nombre"
)
print("\n")

name = input("Ingrese nombre: ")
character = input("Ingrese caracter a buscar: ")

print(
    "El caracter ("
    + character
    + ") "
    + ("se" if character in name else "no se")
    + " encuentra en el nombre ("
    + name
    + ")"
)

print("\n\n")
