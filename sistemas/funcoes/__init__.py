import requests
import PySimpleGUI as sg



class Funcoes:
    
    def recuperar_dados(valor):
        cnpj = valor['-CNPJ-']
        req = requests.get(f'https://receitaws.com.br/v1/cnpj/{cnpj}')
        dados = req.json()
        
        return dados