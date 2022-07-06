print("")
print(
    '4. Leer una cadena de caracteres, donde en lugar de "ñ" se utilicen los caracteres "ny". Crear una nueva cadena substituyendo "ny" por "ñ"'
)
print("\n")

phrase = input('Ingresar oracion con "ny": ')
print("")
print("Frase original: " + phrase)

replaced_phrase = phrase.replace("ny", "ñ")
print("Frase convertida: " + replaced_phrase)

print("\n\n")
