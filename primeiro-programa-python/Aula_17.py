nome = "Katia"


print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Ola Mundo!    "
print(texto)
print(texto.strip() + ".")
print(texto.lstrip()+ ".")
print(texto.rstrip()+ ".")

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14,"#"))


for letra in menu:
    print(letra, end="-")
print()

print("-".join(menu))





