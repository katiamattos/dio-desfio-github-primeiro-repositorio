for numero in range(0,11):
    print(numero, end=" ")


#range
# 0 = start
# 51 =  fim
# 5 = step
for numero in range(0,51,5):
    print(numero, end=" ")

print()

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()