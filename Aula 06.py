"""#Teste 01
#Dicionarios
d = {}
d = {1: "Fabio", 2: "OPA", 10: "REZENDE"}
print(d)
"Fabio" in d
#Criando Dicionarios
dict()
w = {}
a = ("Fabio", 1200)
b = ("Silva", 2200)
c = ("Rezende", 5000) 
nomes = dict([a, b, c])

telefones = dict(ana = 10 , paula = 23 , giancoli = 100, muller = 7)

#tel = dict(10 = 2, 3 = 4, 5 = 7) Para os dicionarios as chaves devem ser strings 

tupla = (2, 4, 6, 8, 10)
{x: x**2 for x in tupla}

letras = {}
letras.fromkeys([4, 5, 6])
letras.fromkeys([4, 5, 6], 0)

letras = letras.fromkeys(["a", "b", "c"], 5) 
t = letras.get("b")  
t = letras.get("v", "Não foi encontrado") 
v = letras.items() 
z = letras.keys()
x = letras.values()

#pop
d = {1: 30, 2: 40, 3: 50, 4: 60}
#d.pop() não vai fazer nada pois preciso passar a chave 
d.pop(2) #Vai excluir a chave 2"""

"""notas = {"Tiago": [10, 3.5], "Paula": [3.8, 6.7], "Ana": [10, 5.5]}
for x in notas:
    media = sum(notas[x]) / len(notas[x])
    print(f"{x} tem Média = {media}")

print("********************")

for r, g in notas.items():
    media = sum(notas[r]) / len(notas[r])
    print(f'{r} tem média = {media}, com as notas {g}.')"""

#Atividade 01
texto = ("Um cidadão fez voto de desapego e pobreza. Dispôs de todos os seus bens e propriedades, reservou para si apenas duas tangas, e saiu pelo mundo afora em busca de todos os sábios, medindo na verdade o desapego de cada um. Levava apenas uma tanga no corpo").lower()  
list(texto)

a = texto.count("a")
e = texto.count("e")
i = texto.count("i")
o = texto.count("o")
u = texto.count("u")

#Pegando valores do teclado para colocar em um diconário 
listagem = {}
nome = input("Nome: ").capitalize()
while nome != "":
    listagem[nome] = [
        float(input("Nota1: ")),
        float(input("Nota2: "))
    ]
    nome = input("Nome: ").capitalize()
print(listagem)

dic = {"letras A": a, "letras E": e, "letras I": i, "letras O": o, "letras U": u}

for x in dic:
    print(x,"=",dic[x])
