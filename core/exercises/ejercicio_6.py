print("")
print("6. Realice los siguientes calculos: Sean a = 28, b = 3")
print("\n")

a = 28
b = 3

# Ejercicio 6.a
print("\t a. Suma, resta, producto, cociente de enteros entre a y b")
print("")

addition = a + b
print("\t (a + b): = (%d + %d): %d" % (a, b, addition))

substraction = a - b
print("\t (a - b): = (%d - %d): %d" % (a, b, substraction))

multiple = a * b
print("\t (a * b): = (%d * %d): %d" % (a, b, multiple))

quotient = a / b
print("\t (a / b): = (%d / %d): %.2f" % (a, b, quotient))

print("\n\n")


# Ejercicio 6.b
print(
    "\t b. Dados los entereos ingresados por teclado, realice las operaciones anteriores"
)
print("")

x = int(input("\t Ingrese valor entero para X: "))
y = int(input("\t Ingrese valor entero para Y: "))

print("")

addition = x + y
print("\t (x + y): = (%d + %d): %d" % (x, y, addition))

substraction = x - y
print("\t (x - y): = (%d - %d): %d" % (x, y, substraction))

multiple = x * y
print("\t (x * y): = (%d * %d): %d" % (x, y, multiple))

quotient = x / y
print("\t (x / y): = (%d / %d): %.2f" % (x, y, quotient))

print("\n\n")


# Ejercicio 6.c
print("\t c. Sean Z1 = -2-5j y Z2 = -2+3j. Realice todas las operaciones basicas")
print("")

Z1 = -2 - 5j
Z2 = -2 + 3j

addition = Z1 + Z2
print("\t (Z1 + Z2): = (%s + %s): %s" % (Z1, Z2, addition))

substraction = Z1 - Z2
print("\t (Z1 - Z2): = (%s - %s): %s" % (Z1, Z2, substraction))

multiple = Z1 * Z2
print("\t (Z1 * Z2): = (%s * %s): %s" % (Z1, Z2, multiple))

quotient = Z1 / Z2
print("\t (Z1 / Z2): = (%s / %s): %s" % (Z1, Z2, quotient))

print("\n\n")
