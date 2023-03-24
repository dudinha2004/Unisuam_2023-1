salarioOriginal = float(input("Digite o valor do Salário Original: "))

if salarioOriginal<=280:
    percenturalAplicado = "20%"
    valorAumento = salarioOriginal*20/100
elif salarioOriginal<=700:
    percenturalAplicado = "15%"
    valorAumento = salarioOriginal * 15 / 100
elif salarioOriginal <= 1500:
    percenturalAplicado = "10%"
    valorAumento = salarioOriginal * 10 / 100
else:
    percenturalAplicado = "5%"
    valorAumento = salarioOriginal * 5 / 100

salarioReajustado = salarioOriginal + valorAumento


print(salarioOriginal)
print(percenturalAplicado)
print(valorAumento)
print(salarioReajustado)