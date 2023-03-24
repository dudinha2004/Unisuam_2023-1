h = float(input("Digite a sua altura: "))
sexo = input("Digite H para homem e M para mulher: ")

if sexo == "H":
    pesoIdeal = (72.7*h) - 58
else:
    pesoIdeal = (62.1*h) - 44.7

print(pesoIdeal)