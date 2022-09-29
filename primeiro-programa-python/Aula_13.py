MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade!"))

if idade >= MAIOR_IDADE:
    print("Maior que 18 anos, pode tirar cnh")

if idade < MAIOR_IDADE:
    print("Ainda nao pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior que 18 anos, pode tirar cnh")
else:
    print("Ainda nao pode tirar a cnh.")


if idade >= MAIOR_IDADE:
    print("Maior que 18 anos, pode tirar cnh")
elif idade == IDADE_ESPECIAL:
    print("pronto para as aulas teoricas")
else:
    print("Ainda nao pode tirar CNH.")
