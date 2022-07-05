"""class Gato:

    def __init__(self, nome, idade, tutor):
        self.nome = nome
        self.idade = idade
        self.tutor = tutor

    def arranhar(self):
        print(f"{self.nome.title()} arranhou seu tutor {self.tutor}.")

    def pular(self):
        print(self.nome.title() + " está louco, pulando ...")

    def buscarIdade(self):
        print(self.nome.title() + " tem " + str(self.idade) + " anos.")

nome  = input("Indique o nome do seu Garo: ")
tutor = input("Indique o nome do Tutor: ")
idade = input("Indique o nome do seu Gato: ")
novogato = Gato(nome, idade, tutor)

novogato.arranhar()
novogato.buscarIdade()
novogato.pular()"""

class Carro:

    def __init__(self, fabricante, modelo, ano):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.hodometro = 0
        self.tanque = 0

    def buscar_descricao(self):
        descricao = f"Carro {self.modelo}, do ano {self.ano}, do fabricante {self.fabricante}, está com {self.hodometro} km rodados e {self.tanque} litros de combustível."
        return descricao

    def ler_hodometro(self):
        print("Esse carro tem " + str(self.hodometro) + " km rodados.")

    def atualizar_hodometro(self, km):
        if km >= self.hodometro:
            self.hodometro = km
        else:
            print("Você está tentando reduzir o valor do hodômetro. É ilegal!")

    def incrementar_hodometro(self, km):
        if km > 0:
            self.hodometro += km
        else: 
            print("Você está tentando reduzir o valor do hodômetro. É ilegal!")

    def abastecer(self, litros):
        self.tanque += litros
        print("Tanque está atualizado com " + str(self.tanque) + " litros de combustível.")

    def __repr__(self):
        return f'<Carro({self.modelo},{self.fabricante},{self.ano})>'

    def __str__(self):
        return f'Carro {self.modelo}|{self.fabricante}|{self.ano}'


class CarroEletrico(Carro):

    def __init__(self, fabricante, modelo, ano):
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()

    def buscar_descricao(self):
        descricao = f"Carro {self.modelo}, do ano {self.ano}, do fabricante {self.fabricante}, está com {self.hodometro} km rodados e com uma bateria com capacidade de {self.bateria} kwh."
        return descricao

    def abastecer(self):
        print("Este tipo de carro não tem tanque de combustível.")


class Bateria:

    def __init__(self, capacidade=70):
        self.capacidade = capacidade

    def ler_bateria(self):
        print(f"Esse carro tem capacidade de  {self.capacidade} kwh.")

    def atualizar_bateria(self, capacidade):
        self.capacidade = capacidade

    def buscar_faixa(self):
        if self.capacidade == 70:
            faixa = 300
        elif self.capacidade >= 80:
            faixa = 500

        texto = "Esse carro pode percorrer +/- " + str(faixa) + "km com a bateria cheia."

        print(texto)

    def __str__(self):
        return f'{self.capacidade}'

print('****** Carro *******')
novocarro = Carro('Fiat', 'Uno', 2015)
novocarro.abastecer(40)
print(novocarro.buscar_descricao())

print('****** Eletrico *******')
novoeletrico = CarroEletrico('Tesla', 'Model S', 2021)
print(novoeletrico.buscar_descricao())
novoeletrico.abastecer()
novoeletrico.atualizar_hodometro(200)
novoeletrico.ler_hodometro()
novoeletrico.bateria.ler_bateria()
novoeletrico.bateria.atualizar_bateria(80)
novoeletrico.bateria.ler_bateria()