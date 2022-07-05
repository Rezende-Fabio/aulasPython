# Importando o módulo sqlite3 para criarmos nosso banco e manipulá-lo.
from datetime import date
from cores import Cores
from sqlite3 import Error

def inserir(tabela, conn):
	try:
		c = conn.cursor()
		if tabela == 'tarefas':
			descricao = input("Informe a tarefa: ").title()
			criado_em = date.today()
			tarefa = (descricao, criado_em)
			c.execute("INSERT INTO tarefas (descricao, criado_em) VALUES (?, ?);", tarefa)	
			conn.commit()
	except Error as e:
		print(e)
	else:
		print(f"{Cores.BOLD}{Cores.OKGREEN}Inserção com sucesso em {tabela}.{Cores.ENDC}")
		input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def atualizar(tabela, conn):
	try:
		c = conn.cursor()
		if tabela == 'tarefas':
			pesquisar(tabela, conn)
			x = input("Informe o id da tarefa a atualizar: ")
			descricao = input("Descrição: ").title()
			tarefa = (descricao, x)
			c.execute("UPDATE tarefas SET descricao=? WHERE idtarefas=?;", tarefa)	
			conn.commit()
	except Error as e:
		print(e)
	else:
		print(f"{Cores.BOLD}{Cores.OKGREEN}Atualização com sucesso em {tabela}.{Cores.ENDC}")
		input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")


def pesquisar(tabela, conn):
	try:
		c = conn.cursor()
		if tabela == 'tarefas':
			c.execute(
				"SELECT * FROM tarefas;"
			)
		resultado = c.fetchall()
		if resultado:
			"""
				os parametros passados para esse format() são o seguinte
				{:>4}  = 4 posições, alinhado a direita
				{:<47} = 47 posições, alinhado a esquerda
				{:^3}  = 3 posições, centralizado
			"""
			print(f"{Cores.BOLD}{Cores.OKGREEN}")
			print("{:<5} {:<50} {:<10}".format("ID", "Descrição", "Criado_em"))
			print(f"{Cores.ENDC} ")
			for item in range(len(resultado)):
				print("{:<5} {:<50} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
		else:
			print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

	except Error as e:
		print(e)
	else:
		print(f"{Cores.BOLD}{Cores.OKGREEN}Pesquisa realizada com sucesso em {tabela}.{Cores.ENDC}")
		input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def pesquisarUnico(tabela, conn):
	try:
		c = conn.cursor()
		if tabela == 'tarefas':
			descricao = input("Descrição: ").title()
			c.execute(
				"SELECT * FROM tarefas WHERE descricao like (?);", ('%'+descricao+'%',)
			)
		resultado = c.fetchall()
		if resultado:
			"""
				os parametros passados para esse format() são o seguinte
				{:>4}  = 4 posições, alinhado a direita
				{:<47} = 47 posições, alinhado a esquerda
				{:^3}  = 3 posições, centralizado
			"""
			print(f"{Cores.BOLD}{Cores.OKGREEN}")
			print("{:<5} {:<50} {:<10}".format("ID", "Descrição", "Criado_em"))
			print(f"{Cores.ENDC} ")
			for item in range(len(resultado)):
				print("{:<5} {:<50} {:<10}".format(resultado[item][0], resultado[item][1], resultado[item][2]))
		else:
			print(f"{Cores.BOLD}{Cores.FAIL}Não foram encontrados registros.{Cores.ENDC}")

	except Error as e:
		print(e)
	else:
		print(f"{Cores.BOLD}{Cores.OKGREEN}Pesquisa realizada com sucesso em {tabela}.{Cores.ENDC}")
		input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

def excluir(tabela, conn):
	try:
		c = conn.cursor()
		if tabela == 'tarefas':
			pesquisar(tabela, conn)
			x = input("Informe o id da tarefa a excluir: ")
			tarefa = (x,)
			c.execute("DELETE FROM tarefas WHERE idtarefas=?;", tarefa)	
			conn.commit()
	except Error as e:
		print(e)
	else:
		print(f"{Cores.BOLD}{Cores.OKGREEN}Exclusão com sucesso em {tabela}.{Cores.ENDC}")
		input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")