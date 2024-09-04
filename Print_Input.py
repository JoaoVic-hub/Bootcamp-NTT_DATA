nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")
print(nome, idade, "...\n")
print("Olá mundo" + idade) #and == &&

#or == ||
#not == !

nome_curso = "novo curso"
curso = nome_curso
saldo = 100
limite = 100
frutas = ["laranja", "maçã"]

print("laranja" in frutas)
print(nome_curso is curso)
print(saldo is limite)
print(saldo is not limite)
print("curso" in nome_curso)