#Teste 01
"""lista = ['Ana', 'Paula', 'Tiago', 'Gustavo', 'Amanda']
novalista = lista[:]

for nome in lista[:]:
    if len(nome) > 3:
        novo = input("Indeique o nome: ")
        lista.insert(0, novo)
    print(nome)

print(lista)
print(novalista)"""""

#Teste 02
"""lista = ['Ana', 'Paula', 'Tiago', 'Gustavo', 'Amanda']
c = 0
for nome in lista:
    novo = input("Informe um nome: ")
    if novo == nome:
        print("Existe")
        c += 1
print(lista)
print(f"Tem {c} iguais")"""

#Teste 03 
"""num = [10, 20, 30, 40, 50, 60, 70]

print(num)
print(sum(num) / len(num))
print(sum(num))
print(len(num))
#print(num.count(20))"""

#Teste 04
"""for x in range(0, 100, 3): #O valor 3 é a variavel que vai acrescentando ou decrementando.
    print(x)"""

#Teste 05
"""nomes = ['Ana', 'Paula', 'Tiago', 'Gustavo', 'Amanda']
for x in range(len(nomes)):
    print(x, nomes[x])"""""

#Exercicio 01 
"""aux = 0
for x in range(1000, 2001, 1):
    aux += x
    print(x)
print(f"a soma {aux}")"""

#Teste 06
"""nome = "fabio da silva rezende"
nome[0:3]
nome[0:9]
nome[0:20:2]"""

#Exercicio 02
"""for x in range(14, 201, 1):
    aux = x * x
    print(aux)"""

#Exercicio 03
cpf = input("Entre com seu CPF com ponto e hífen: ") #3 7 11 510.506.018-07
list(cpf)

while cpf[3] and cpf[7] != ".":
    if cpf[3] and cpf[7] != "." and cpf[11] != "-":
        print("O cpf que foi informado, não segue o padrão pedido")
    
    cpf = input("Digiete o cpf novamente: ")
    list(cpf)

carac = int(cpf[0])
carac1 = int(cpf[1])
carac2 = int(cpf[2])
carac3 = int(cpf[4])
carac4 = int(cpf[5])
carac5 = int(cpf[6])
carac6 = int(cpf[8])
carac7 = int(cpf[9])
carac8 = int(cpf[10])

valid1 = int(cpf[12])
valid2 = int(cpf[13])

soma1 = carac *10 + carac1 *9 + carac2 *8 + carac3 *7 + carac4 *6 + carac5 *5 + carac6 *4 + carac7 *3 + carac8 *2
result1 = soma1 * 10 %11

soma2 = carac *11 + carac1 *10 + carac2 *9 + carac3 *8 + carac4 *7 + carac5 *6 + carac6 *5 + carac7 *4 + carac8 *3 + result1 *2
result2 = soma2 *10 %11

if result1 == 10:
    result1 = 0

if result2 == 10:
    result2 = 0

print(result1,  result2)

if result1 == valid1 and result2 == valid2:
    print(f"O cpf {cpf} é válido!")
else:
    print(f"O cpf {cpf} não é válido!")


    
  


