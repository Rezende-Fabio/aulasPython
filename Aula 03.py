#Teste 01
"""mes =  int (input("Qual mês você deseja saber a quantidade de dias?: "))
 
if mes <= 0:
    print("Esse mês não existe!!")
elif mes == 1:
    print("Janeiro tem 31 dias")
elif mes == 2:
    ano = int (input("Escolha o ano que que deseja: "))
    if (ano % 400 == 0 or ano % 4 == 0) and (ano % 100 != 0):
        print(f"Fevereiro em {ano} tem 29 dias")
    else:
        print(f"Fevereiro em {ano} tem 28 dias")
elif mes == 3:
    print("Março tem 31 dias")
elif mes == 4:
    print("Abril tem 30 dias")
elif mes == 5:
    print("Maio tem 31 dias")
elif mes == 6:
    print("Junho tem 30 dias")
elif mes == 7:
    print("Julho tem 31 dias")
elif mes == 8:
    print("Agosto tem 31 dias")
elif mes == 9:
    print("Setembro tem 30 dias")
elif mes == 10:
    print("Outubro tem 31 dias")
elif mes == 11:
    print("Novembro tem 30 dias")
elif mes == 12:
    print("Dezembro tem 31 dias")
else:
    print("Esse mês não existe!!")"""
#Teste 02
nome = str(input("Qual o seu nome?: "))
peso = float(input("Qual seu peso?: "))
altura = float(input("Qual a sua Altura?: "))

imc = float(peso / (altura*altura))

print("Menor que 17.0  | Muito abaixo do peso")
print("De 17.0 a 18.50 | Abaixo do peso")
print("De 18.50 a 25.0 | Peso normal")
print("De 25.0 a 30.0  | Acima do peso")
print("De 30.0 a 35.0  | Obesidade I")
print("De 35.0 a 40.0  | Obesidade II")
print("Acima de 40.0   | Obesidade III (mórbida)\n")

if imc < 17.0:
    print(f"{nome}, pesa {peso} KG, tem {altura}, e seu IMC é {imc: .2f} Muito abaixo do peso")
elif 17.0 <= imc < 18.50:
    print(f"{nome}, pesa {peso} KG, tem {altura}, e seu IMC é {imc: .2f} Abaixo do peso")
elif 18.50 <= imc < 25.0:
    print(f"{nome}, pesa {peso} KG, tem {altura}, e seu IMC é {imc: .2f} Peso normal")
elif 25.0 <= imc < 30.0:
    print(f"{nome}, pesa {peso} KG, tem {altura}, e seu IMC é {imc: .2f} Acima do peso")
elif 30.0 <= imc <35.0:
    print(f"{nome}, pesa {peso} KG, tem {altura}, e seu IMC é {imc: .2f} Obesidade I")
elif 35.0 <= imc < 40.0:
     print(f"{nome}, pesa {peso} KG, tem {altura}, e seu IMC é {imc: .2f} Obesidade II")
else:
     print(f"{nome}, pesa {peso} KG, tem {altura}, e seu IMC é {imc: .2f} Obesidade III")