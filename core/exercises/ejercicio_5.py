print("")
print(
    "5. Un psiquiatra tiene un paciente que habla invirtiendo las frases completas. "
    + '(por ejemplo: si quiere decir "hola caracola", lo que realmente dice es: "alocarac aloh"). '
    + "Para poder comunicarse con el paciente decide hacer un programa que traduzca lo que el dice al lenguaje del paciente. "
    + "Implementar dicho programa"
)
print("\n")

phrase = input("Ingrese la frase que desea invertir: ")
print("")


# Reverse string object function
def reverse(string):
    temp = ""

    for character in string:
        temp = character + temp

    return temp


# Using the function i've created
inverted_phrase = reverse(phrase)
print("La frase invertida es: " + inverted_phrase)

print("\n\n")
