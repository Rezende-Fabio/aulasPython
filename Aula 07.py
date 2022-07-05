#teste 01
"""ano_atual = int(input("Entre com o ano atual: "))
ano_aniv = int(input("Entre com o ano que nasceu: "))

def soma_idade(ano_atual, ano_aniv):
     resp = ano_atual - ano_aniv
     return resp

print(f"A sua Idade é {soma_idade(ano_atual, ano_aniv)}")"""

#teste 02
"""def par(num):
    return num % 2
print(par(11))

x = lambda num, b: b + num % 2
print(x(11, 8))

def multa(numero):
    return lambda x: x * numero

multa10 = multa(10)
print(multa10(8))

multa100 = multa(100)
print(multa100(3))

def tabuada(x):
    return lambda y, u, r: y * x * r * u

tabuada10 = tabuada(10)
for i in range(20):
    print(tabuada10(i, 3, 5))"""""

#teste 03
# Gasto total é parametro de entrada para calcular a gasolina, sendo que 40% da despesa é com gasolina.

"""gasto = float(input("Informe o gasto total da despesa: "))

# Sem funcao lambda - Uso de funcao regular
def gasolina(despesa):
    return despesa * 0.4

print(f'Funcao Regular: Gasolina representa: {gasolina(gasto)} reais da despesa total.')

# Com funcao lambda e um argumento
gasolinaD = lambda d: d * 0.4
print(f'Funcao Lambda: Gasolina representa: {gasolinaD(gasto)} reais da despesa total.')

# Com funcao lambda e dois argumentos
gasolinaT = lambda d, r: d * r
r = float(input("Informe o percental da despesa: "))
print(f'Funcao Lambda: Gasolina representa: {gasolinaT(gasto, r)} reais da despesa total.')

# Com funcao regular retornando uma funcao lambda
def gasol(x):
    return lambda despesa: despesa * x
imp4 = gasol(.4)
imp5 = gasol(.5)

print(f'Funcao Regular e Lambda: Gasolina representa:\n 40% = {imp4(gasto)} reais da despesa total.\n 50% = {imp5(gasto)} reais da despesa total.')"""""

#teste 04
"""numeros = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
numero = [10, 92]

result = []
for x in numeros:
    if x > 7:
        result.append(x)
print(result)

print(list(filter(lambda num: num > 7, numeros)))

mapear = list(map(lambda num: num * 2, numeros))
print(mapear)

print(list(filter(lambda num: num >= 1, mapear)))"""

#Exercício 01
print("Entre com cinco números")
numeros = []
for x in range(5):
    numeros[x] = input(f"entre com {x + 1} número: ")

print(list(filter(lambda result: result %2, numeros)))

"""numeros = []

for i in range(5):
  n = int(input("Digite um número: "))
  numeros.append(n)
par = list(filter(lambda n: n % 2 == 0, numeros))
impar = list(filter(lambda n: n % 2 != 0, numeros))
mapear = list(map(lambda num: num % 2, numeros))

print("\n-----Números pares-----")
par = sorted(par)
print(par)
print("-----Números impares-----")
impar = sorted(impar, reverse=True)
print(impar)
print("-----Restos mapeados-----")
print(mapear)"""
