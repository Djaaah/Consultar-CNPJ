import requests
import PySimpleGUI as sg


class Telas:
    def tela_principal(socios, cabeca_socios, cabeca_atvdSECU, atvdSECU):
        
        font = ("Futura, 14")
        
        CNPJ = [
            [sg.Text('CNPJ', font=font), sg.Input(size=(20,1), border_width=0, key='-CNPJ-'), sg.Button('Pesquisar', key='-PESQUISAR-', border_width=0, font=font, button_color=(sg.theme_background_color()))],
        ]
        
        
        QSA = [
            [sg.Text("Quadro Societário", font=font)]
        ]
        
        
        
        dados = [
            # ROW 1
            [sg.Text('Atualizado em', font=font, size=(12,1)), sg.Input(readonly=True, border_width=0, key='-ULTIMA_ATUALIZACAO-', size=(15,1)),
             sg.Text('Tipo', font=font, size=(8,1)), sg.Input(readonly=True, border_width=0, key='-TIPO-', size=(15,1)),
             
             ],
            # ROW 2
            [sg.Text('Abertura', font=font, size=(12,1)), sg.Input(readonly=True, border_width=0, key='-ABERTURA-', size=(15,1)),
             sg.Text('Porte', font=font, size=(8,1)), sg.Input(readonly=True, border_width=0, key='-PORTE-', size=(15,1))
               
             ],
            # ROW 3
            [sg.Text('Razão Social', font=font, size=(12,1)), sg.Input(readonly=True, border_width=0, key='-RAZAO_SOCIAL-', size=(46,1))],
            
            # ROW 4
            [sg.Text('Nome Fantasia', font=font, size=(12,1)), sg.Input(readonly=True, border_width=0, key='-NOME_FANTASIA-', size=(46,1))],
            
            # ROW 5
            [sg.Text('Atvd. Principal', font=font, size=(12,1)),
            sg.Input(readonly=True, border_width=0, key='-ATIVIDADE_PRINCIPAL-', size=(46,1))],
             
            # ROW 6
            [sg.Text(' '*33), sg.Text('Atividades Secundárias', font=font)],
            
            # ROW 7
            
            [sg.Table(values=atvdSECU, 
                      headings=cabeca_atvdSECU, 
                      num_rows=3, row_height=45,
                      auto_size_columns=True,
                      justification='center', 
                      max_col_width=40,
                      expand_y=True,
                      key='-ATIVIDADES_SECUNDARIAS-' 
                      )],
        
            # ROW 8
            [sg.HSep()],
            [sg.Text('Situação Atual', font=font, size=(12,1)),
            sg.Input(readonly=True, border_width=0, key='-SITUACAO_ATUAL-', size=(46,1))],
            
            # ROW 9
            [sg.Text('Logradouro', font=font, size=(12,1)),
            sg.Input(readonly=True, border_width=0, key='-LOGRADOURO-', size=(46,1))],
            
            
            # ROW 10
            [sg.Text('nª', font=font, size=(12,1)),
            sg.Input(readonly=True, border_width=0, key='-NUMERO-', size=(7,1)),
            sg.Text('Bairro', font=font),
            sg.Input(readonly=True, border_width=0, key='-BAIRRO-', size=(16,1)),
            sg.Text('UF', font=font),
            sg.Input(readonly=True, border_width=0, key='-UF-', size=(5,1))],
            
            
            [sg.Text('Complemento', font=font, size=(12,1)),
             sg.Input(readonly=True, border_width=0, key='-COMPLEMENTO-', size=(46,1))],
            
            # ROW 12
            [sg.Text('E-mail', font=font, size=(12,1)),
             sg.Input(readonly=True, border_width=0, key='-EMAIL-', size=(46,1))],
            
            # ROW 13
            [sg.Text('Telefone', font=font, size=(12,1)),
             sg.Input(readonly=True, border_width=0, key='-TELEFONE-', size=(46,1))],
            
            # ROW 14
            [sg.HSep()],
            [sg.Column(QSA, justification='center')],
            
            # ROW 15
            [sg.Text('Sócio Adm.', font=font, size=(12,1)),
             sg.Input(readonly=True, border_width=0, key='-SOCIO_ADM-', size=(46,1))],
            
            # ROW 16
            [sg.Text(' '*36), sg.Text('Demais Sócios.', font=font, size=(12,1))],
            
            # ROW 17
            [sg.Table(values=socios, 
                      headings=cabeca_socios, 
                      num_rows=3, row_height=45,
                      auto_size_columns=True,
                      justification='center', 
                      max_col_width=35,
                      key='-SOCIOS-' 
                      )],
        
            
        ]   
        
        
        layout = [
            [sg.Column(CNPJ, justification='center')],
            [sg.HSep()],
            [sg.Column(dados, scrollable=True,  vertical_scroll_only=True, size=(500,500))]
        ]
        
        
        return sg.Window('Consultar CNPJ', layout=layout, finalize=True)
    pass