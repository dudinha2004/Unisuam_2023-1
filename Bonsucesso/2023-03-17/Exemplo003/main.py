matricula = input("Digite a sua Matricula: ")
nome = input("Digite o seu Nome: ")
n1 = float(input("Digite o seu Teste: "))
n2 = float(input("Digite a sua Prova: "))

media = (n1 + n2) /2

if media >= 7:
  situacao = "Aprovado"
else:
  situacao = "Reprovado"

print("Matricula: " + matricula)
print("Nome: " + nome)
print("Média: " , media)
print("Situação: " + situacao)