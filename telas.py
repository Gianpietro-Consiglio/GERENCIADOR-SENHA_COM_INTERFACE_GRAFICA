from sys import maxsize
import PySimpleGUI as sg


def Tela_Login():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text('Login',font='Verdana'),sg.Input(key='login',pad=10)],
        [sg.Text('Senha',font='Verdana'),sg.Input(key='senha',pad=10,password_char='*')],
        [sg.Button('Logar',font='Verdana',button_color='BLUE',pad=10),sg.Button('Voltar',font='Verdana',button_color='BLUE',pad=10)],
        [sg.Text('',key='Mensagem',font='Verdana')],
        [sg.Text('Versão 1.1',font='Verdana')]
    ]

    return sg.Window('Login',layout=layout,finalize=True,element_justification='c',)
    
 
def Tela_Cadastro():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text('Nome',font='Verdana'),sg.Input(key='nome',pad=10)],
        [sg.Text('Senha',font='Verdana'),sg.Input(key='senha',pad=10,password_char='*')],
        [sg.Button('Enviar dados',font='Verdana',pad=10,button_color='BLUE'),sg.Button('Voltar',font='Verdana',pad=10,button_color='BLUE')],
        [sg.Text('',key='Mensagem',font='Verdana')],
        [sg.Text('Versão 1.1',font='Verdana')]
    ]
    return sg.Window('Cadastro',layout=layout,finalize=True,element_justification='c')   

 
        
def Tela_Opcoes(nome):
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text(F"CONTA ACESSADA: {nome}",text_color='GREEN',key="Mensagem",font='Verdana')],
        [sg.Button('Cadastrar Credencial', font='Verdana',button_color='BLUE',pad=10,border_width=5)],
        [sg.Button('Ver Credenciais',font='Verdana',button_color='BLUE',pad=10,border_width=5)],
        [sg.Button('Configurações',font='Verdana',button_color='BLUE',pad=10,border_width=5)],
        [sg.Button('Excluir Conta',font='Verdana',button_color='BLUE',pad=10,border_width=5)],
        [sg.Button('Sair',font='Verdana',button_color='BLUE',pad=10,border_width=5)],
        [sg.Text('Versão 1.1')]
    ]
        
    return sg.Window('Opções',layout=layout,finalize=True,element_justification='c')
        
def Tela_Cadastrar_Credencial():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text('Não é necessário usar a funcionalidade gerar senha, caso preferir, pode criar sua propria senha e colocar ela no campo senha!',font='Verdana')],
        [sg.Text('Site',font='Verdana'),sg.Input(key='site',pad=10)],
        [sg.Text('Usuário',font='Verdana'),sg.Input(key='usuario',pad=10)],
        [sg.Text('Senha',font='Verdana'),sg.Input(key='senha',pad=10)],
        [sg.Button('Cadastrar',font='Verdana',pad=10,button_color='BLUE',border_width=5),sg.Button('Voltar',font='Verdana',pad=10,button_color='BLUE',border_width=5),sg.Button('Limpar',font='Verdana',pad=10,button_color='BLUE',border_width=5)],
        [sg.Button('Gerar senha',font='Verdana',pad=10,button_color='BLACK',border_width=1),sg.Text('Quantidade de caracteres',font='Verdana'),sg.Input(key='quantidade',pad=10,size=5)],
        [sg.Text('',key='Mensagem',font='Verdana')],
        [sg.Text('Versão 1.1',font='Verdana')]
    ]
        
    return sg.Window('Cadastro de credenciais',layout=layout,finalize=True,element_justification='c')
        


def Tela_Ver_Credenciais():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text('Suas credenciais',font='Verdana')],
        [sg.Output(size=(80,30),background_color='Black',text_color='White',font='Verdana',key='Mensagem')],
        [sg.Button('Buscar',font='Verdana',button_color='BLUE',border_width=5),sg.Button('Voltar',font='Verdana',button_color='BLUE',border_width=5)],
        [sg.Button('Avistar',font='Verdana',button_color='GREEN',size=(10),pad=10,border_width=3),sg.Text('Id de credencial: '), sg.Input(key='id_credencial2',size=(10))],
        [sg.Button('Alterar',font='Verdana',button_color='#ffa500',size=(10),pad=10,border_width=3),sg.Text('Id de credencial: '), sg.Input(key='id_credencial1',size=(10))],
        [sg.Button('Excluir',font='Verdana',button_color='RED',size=(10),pad=10,border_width=3),sg.Text('Id de credencial: '), sg.Input(key='id_credencial',size=(10))],
        [sg.Text('Versão 1.1',font='Verdana')]
    ]

    return sg.Window('Suas Credenciais',layout=layout,finalize=True,element_justification='c')
          

def Tela_Configuracoes():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text("Suas informações",font='Verdana')],
        [sg.Text("Nome",pad=10,font='Verdana'),sg.Input(key="nome")],
        [sg.Text("Senha",pad=10,font='Verdana'),sg.Input(key="senha")],
        [sg.Button("Ver dados",pad=10,font='Verdana',button_color='BLUE',border_width=5),sg.Button("Alterar",pad=10,font='Verdana',button_color='BLUE',border_width=5),sg.Button("Voltar",pad=10,font='Verdana',button_color='BLUE',border_width=5)],
        [sg.Text("",key="Mensagem",font='Verdana',pad=10)],
        [sg.Text('Versão 1.1',font='Verdana')]
    ]

    return sg.Window("Seus dados cadastrais",layout=layout,finalize=True,element_justification="c")


def Tela_Alterar_Credencial():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text("Informação da sua credencial",font='Verdana')],
        [sg.Text("Site",pad=10,font='Verdana'),sg.Input(key="site")],
        [sg.Text("Usuário",pad=10,font='Verdana'),sg.Input(key="usuario")],
        [sg.Text("Senha",pad=10,font='Verdana'),sg.Input(key="senha",)],
        [sg.Button("Ver dados",pad=10,font='Verdana',button_color='BLUE',border_width=5),sg.Button("Alterar",pad=10,font='Verdana',button_color='BLUE',border_width=5),sg.Button("Voltar",pad=10,font='Verdana',button_color='BLUE',border_width=5),sg.Button('Limpar',font='Verdana',pad=10,button_color='BLUE',border_width=5)],
        [sg.Button('Gerar senha',font='Verdana',pad=10,button_color='BLACK',border_width=1),sg.Text('Quantidade de caracteres',font='Verdana'),sg.Input(key='quantidade',pad=10,size=5)],
        [sg.Text('',key="Mensagem")],
        [sg.Text('Versão 1.1',font='Verdana')]
    ]

    return sg.Window("Alterar Credencial",layout=layout,finalize=True,element_justification="c")


def Tela_Principal():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text(' Gerenciador de senhas NG',font='Verdana')],
        [sg.Button('Entrar',font='Verdana',button_color='BLUE',pad=10,border_width=5),sg.Button('Registrar',font='Verdana',button_color='BLUE',pad=10,border_width=5)],
        [sg.Button('Infos',font='Verdana',button_color='BLUE',pad=10,border_width=5),sg.Button('Sair',font='Verdana',button_color='BLUE',pad=10,border_width=5)],
        [sg.Text('Versão 1.1',font='Verdana')]
    ]

    return sg.Window('Menu Principal',layout=layout,finalize=True,element_justification='c')

def Tela_Infos():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text('Versão atual do software: 1.1')],
        [sg.Button('Instagram',font='Verdana',button_color='BLUE',pad=10,border_width=5),sg.Button('GitHub',font='Verdana',button_color='BLUE',pad=10,border_width=5),sg.Button('Voltar',font='Verdana',button_color='BLUE',pad=10,border_width=5)]
    ]

    return sg.Window('Informações',layout=layout,finalize=True,element_justification='c')