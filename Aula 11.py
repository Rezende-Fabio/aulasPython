import requests
import json
from cores import Cores

def buscar_dados():
    request = requests.get("https://api.github.com/users/anagiancoli/followers")
    todos = json.loads(request.content)

    print(f"{Cores.BOLD}{Cores.OKGREEN}")
    print("{:<20} {:<55}".format("LOGIN", "URL"))
    print(f"{Cores.ENDC} ")

    for k in todos:
        print("{:<20} {:<55}".format(k['login'], k['html_url']))
        
    input(f"{Cores.BOLD}{Cores.OKBLUE}Pressione <ENTER> para continuar ...{Cores.ENDC}")

if __name__ == '__main__':
    buscar_dados()


#https://medium.com/@renatojlelis/trabalhando-com-json-no-python-1eb0f97c0c50
#https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/json.html
