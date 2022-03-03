import requests
import PySimpleGUI as sg
from sistemas.telas import Telas as t 
from sistemas.funcoes import Funcoes as f








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
        cnpj = valor['-CNPJ-'].strip()
        
        if len(cnpj) < 14 or len(cnpj) > 14:
            sg.popup('Digite o CNPJ nesse formato: XXXXXXXXXXXXXX\nApenas 14 Caracteres!', title='CNPJ INVÁLIDO')
        else:
            dados = f.recuperar_dados(valor)

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
            
            #Natureza Jurídica
            NJ = dados['natureza_juridica'].split('-')
            natureza_juridica = NJ[-1].strip()

            janela['-ULTIMA_ATUALIZACAO-'].update(separado); janela['-TIPO-'].update(tipo)
            janela['-ABERTURA-'].update(abertura); janela['-PORTE-'].update(porte)
            janela['-RAZAO_SOCIAL-'].update(razao_social); janela['-NOME_FANTASIA-'].update(nome_fantasia)
            janela['-ATIVIDADE_PRINCIPAL-'].update(atvd_principal)
            janela['-SITUACAO_ATUAL-'].update(sit_atual); janela['-LOGRADOURO-'].update(rua)
            janela['-NUMERO-'].update(numero); janela['-BAIRRO-'].update(bairro); 
            janela['-UF-'].update(uf); janela['-EMAIL-'].update(email)
            janela['-TELEFONE-'].update(telefone); janela['-COMPLEMENTO-'].update(complemento)
            janela['-NATUREZA_JURIDICA-'].update(natureza_juridica)
        
        
        
        
        
        
