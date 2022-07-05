# Importando o módulo do sqlite3 para manipularmos o banco de dados SQLITE3
import sqlite3
# Importando o módulo do sqlite3 e a classe Error para exibir mensagens de erro
from sqlite3 import Error
# Importando o módulo time para utilizar o método sleep que aguarda o 
# tempo em segundos informando dentro do parênteses
from time import sleep
# Importando o arquivo schema.py para criar as tabelas do banco de dados
import schema
# Importando o arquivo tabelas para manipular as informações nelas (CRUD)
# Criar, atualizar, excluir, e pesquisar.
import tabelas
# Importando o o arquivo cores.py, a classe Cores para colocar cores nos textos
from cores import Cores
# IMportanto a biblioteca grafica Tkinter
#import tkinter as tk
import tkinter as tk

def menu():
	print(25 * '*')
	print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Menu de Opções --***{Cores.ENDC}")
	print(25 * '*')
	print(f"{Cores.BOLD}1. Manter Tarefas{Cores.ENDC}")
	print(f"{Cores.BOLD}{Cores.FAIL}2. Sair{Cores.ENDC}")
	print(25 * '*')
	selecao = int(input('Selecione uma opção: '))
	return selecao


def submenu(tabela):
	print(25 * '*')
	print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Opção {tabela}--***{Cores.ENDC}")
	print(25 * '*')
	print(f"{Cores.BOLD}{Cores.FAIL}0. Retornar ao menu principal{Cores.ENDC}")
	print(f"{Cores.BOLD}1. Inserir {tabela}")
	print(f"2. Atualizar {tabela}")
	print(f"3. Pesquisar {tabela}")
	print(f"4. Pesquisar Único {tabela}")
	print(f"5. Excluir {tabela}{Cores.ENDC}")
	print(25 * '*')
	opcaosub = int(input('Selecione uma opção: '))
	return opcaosub

def criar_conexao(banco):
	"""Criando a conexão com o banco de dados Sqlite3."""
	# Variável conn inicializada para estabelecer a conexão com o banco
	conn = None
	# Tentará fazer a conexão com o banco de dados
	try: 
		# Criando a conexão com o banco e salvando o objeto Connection na variável conn.
		conn = sqlite3.connect(banco)
		# Exibe a versão do Sqlite
		print(sqlite3.sqlite_version)
		# Sucesso na conexão. É retornado a conexão a quem chamou.
		return conn
		# Caso negativo, não conseguiu estabelecer conexão, retorna o erro que ocorreu.	
	except Error as e: 
		print(e)


# Função para limpar a tela antes de exibir a próxima instrução
def limpar():
    # Importando o módulo do sistema operacional (os) para usar instruções dele
    import os
    # Importando o módulo time para utilizar o método sleep que aguarda o 
    # tempo em segundos informando dentro do parênteses
    from time import sleep
    
    # Função para limpar a tela
    def screen_clear():
    # Para os sistemas operacionais: mac and linux(here, os.name is 'posix')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
        # Para o sistema operacional windows
            _ = os.system('cls')
    # Aguarda 1 segundo para executar a próxima instrução
    sleep(1)
    # Chama a função de limpeza
    screen_clear()

def interace_grafica():
	janela1 = tk.Tk()
	janela1.geometry("1500x800")

	texto_titulo = "Projeto Banco de Dados", 
	titulo = tk.Label(janela1, text="Projeto Banco de Dados").place(x=700, y=10, height=200)

	janela1.mainloop()



if __name__ == '__main__':
	limpar()
	interace_grafica()
	print(27 * '*')
	print(f"{Cores.BOLD}{Cores.OKBLUE}***-- Projeto Exemplo --***{Cores.ENDC}")
	print(27 * '*')
	print(f"{Cores.BOLD}{Cores.OKBLUE}Criando o banco de dados se não existir ... {Cores.ENDC}")
	banco = input('Informe o nome do banco a ser criado: ')
	print(f"{Cores.BOLD}{Cores.OKBLUE}Criando conexão ... {Cores.ENDC}")
	conn = criar_conexao(banco)
	print(f"{Cores.BOLD}{Cores.OKBLUE}Criando tabelas do banco de dados se não existirem ... {Cores.ENDC}")
	schema.criar_tabelas(banco)
	sleep(2)
	input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")
	limpar()
	opcao = menu()
	limpar()
	while opcao != 2:	
		if opcao == 1:
			tabela = 'tarefas'
		else:
			print('Opção inválida!')
		
		opcaosub = submenu(tabela)
		limpar()
		while opcaosub != 0:
			if opcaosub == 1:
				print(f'Inserir {tabela}')
				tabelas.inserir(tabela, conn)
			elif opcaosub == 2:
				print(f'Atualizar {tabela}')
				tabelas.atualizar(tabela, conn)
			elif opcaosub == 3:
				print(f'Pesquisar {tabela}')
				tabelas.pesquisar(tabela, conn)
			elif opcaosub == 4:
				print(f'Pesquisar único {tabela}')
				tabelas.pesquisarUnico(tabela, conn)
			elif opcaosub == 5:
				print(f'Excluir {tabela}')
				tabelas.excluir(tabela, conn)
			else:
				print('Opção inválida!')
			limpar()
			opcaosub = submenu(tabela)
			limpar()
		opcao = menu()
		limpar()
	else:
		print("Obrigada. Volte sempre!")

	
	