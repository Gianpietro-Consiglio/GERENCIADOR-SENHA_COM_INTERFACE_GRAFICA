import sqlite3
import PySimpleGUI as sg
import os


def Tela_Principal():
    layout = [
        [sg.Text("Comando SQL:"), sg.Input(key="campo")],
        [sg.Button("Enviar"),sg.Button('Parar')],
        [sg.Output(background_color="Black",font="Verdana",text_color="Green",size=(50,30))]
    ]

    return sg.Window('Alimentador_de_banco',layout=layout,element_justification='c',finalize=True)


janela = Tela_Principal()
while True:
    window,event,values = sg.read_all_windows()
    
    if window == janela and event == sg.WIN_CLOSED:
        break

    if window == janela and event == 'Enviar':
        try:
            os.chdir("C:\\Users\Public\\GERENCIADOR-SENHAS\\")
            banco = sqlite3.connect('gerenciador-senhas.db')
            cursor = banco.cursor()
        except Exception as erro:
            sg.popup('bad command!') 
            break
        cont = 0       
        while True:
            cont += 1
            try:
                cursor.execute(f"{values['campo']}")
                banco.commit()
            except Exception as erro:
                sg.popup('bad command')
                break

            else:
                print(F"EVENTO[{cont}] -> ENVIADO COM SUCESSO!")
                if window == janela and event == "Parar":
                    break

    
