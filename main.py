import requests
import PySimpleGUI as sg
from sistemas.telas import Telas as t 









cabeca_atvdSECU = ['Cód.', 'Descrição']
atvdSECU = list()
        
cabeca_socios = ['Qualificação', 'Nome']
socios = [["47.72-5-00", "Comércio varejista de cosméticos, produtos\n de perfumaria e de higiene pessoal"], ["teste3", "teste4"]]


telaPrincipal = t.tela_principal(socios, cabeca_socios, cabeca_atvdSECU, atvdSECU)



while True:
    janela, evento, valor = sg.read_all_windows()
    
    if evento == sg.WIN_CLOSED:
        break
    
    if evento == '-PESQUISAR-':
        cnpj = valor['-CNPJ-']
        req = requests.get(f'https://receitaws.com.br/v1/cnpj/{cnpj}')
        dados = req.json()
        
        print(dados)
        #Ultima atualização
        apoio = dados['ultima_atualizacao'].split('T')
        separado = apoio[0]

    
        #Tipo
        tipo = dados['tipo']

        #Abertura
        abertura = dados['abertura']

        #Porte
        porte = dados['porte']

        #Razão Social
        razao_social = dados['nome']

        #Nome Fantasia
        nome_fantasia = dados['fantasia']

        #Atvd Principal
        atvd_principal = dados['atividade_principal'][0]['text']

        #Atvds Secundarias // possivelmente vou precisar por no laço for, contudo preciso aprender a dimensionar a table
        
        atvdSECU.append(dados['atividades_secundarias'][0]['text'])
        atvdSECU.append(dados['atividades_secundarias'][0]['code'])

        #Situação Atual
        sit_atual = dados['situacao']

        #Logradouro
        rua = dados['logradouro']

        #nª
        numero = dados['numero']

        #Bairro
        bairro = dados['bairro']

        #UF
        uf = dados['uf']

        #Complemento
        complemento = dados['complemento']

        #E-mail
        email = dados['email']

        #Telefone
        telefone = dados['telefone']

        #Socio ADM
        socio_adm = dados['qsa'][0]['nome']


        #Demais Sócios

        janela['-ULTIMA_ATUALIZACAO-'].update(separado); janela['-TIPO-'].update(tipo)
        janela['-ABERTURA-'].update(abertura); janela['-PORTE-'].update(porte)
        janela['-RAZAO_SOCIAL-'].update(razao_social); janela['-NOME_FANTASIA-'].update(nome_fantasia)
        janela['-ATIVIDADE_PRINCIPAL-'].update(atvd_principal); janela['-ATIVIDADES_SECUNDARIAS-'].update(atvdSECU)
        janela['-SITUACAO_ATUAL-'].update(sit_atual); janela['-LOGRADOURO-'].update(rua)
        janela['-NUMERO-'].update(numero); janela['-BAIRRO-'].update(bairro); janela['-COMPLEMENTO-'].update(complemento)
        janela['-UF-'].update(uf); janela['-EMAIL-'].update(email)
        janela['-TELEFONE-'].update(telefone); janela['-SOCIO_ADM-'].update(socio_adm)
        janela['-SOCIOS-'].update("Deu certo")
        
        
        
        
        
