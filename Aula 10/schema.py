# Importando o módulo sqlite3 para criarmos nosso banco e manipulá-lo.
import sqlite3
from sqlite3 import Error
from cores import Cores

def criar_tabelas(banco):
	# Definindo a conexão com o BD chamado 
	conn = sqlite3.connect(banco)
	# Definindo o cursor cuja função é permitir navegar e manipular os registros do BD.
	c = conn.cursor()
	
	try:
		# Executando a instrução de criação da tabela tarefas no BD
		# o idtarefas aponta para rowid (chave primaria da tabela)
		c.execute("""
		CREATE TABLE IF NOT EXISTS tarefas (
				idtarefas INTEGER primary key,
				descricao TEXT NOT NULL,
				criado_em DATE NOT NULL);
			""")
		
		c.execute("""
    	CREATE TABLE IF NOT EXISTS TIPOS_USUARIO (
      		SIGLA_USUARIO TEXT NOT NULL primary key,
      		TIPO_USUARIO TEXT,
      		DESCRICAO_USUARIO TEXT);
    		""")
		
		# Exibindo na tela a mensagem de sucesso de criação da tabela tarefas.
		return print(f"{Cores.BOLD}{Cores.OKGREEN}Tabelas criadas com sucesso!{Cores.ENDC}")
	except Error as e:
		print(e)