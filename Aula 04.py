import random
x =0 
while x <= 10:
    print(random.randint(10, 20))
    x += 1

min = int(input("Entre com o número mínimo para sortear: "))
max = int(input("Entre com o número máximo para sortear: "))
erros = 0
resp = 0

result = random.randint(min, max)

resp = int(input("Agora tente acertar o número sorteado: "))

while resp != result:

    resp = int(input("Tente Novamnete:")) 
    
    if resp == result:
        print(f"Acertou com {erros} erros")
    elif resp == result + 1:
        print("Esta quente")
        erros += 1
    elif resp == result - 1:
        print("Esta quente")
        erros += 1
    else:
        erros += 1