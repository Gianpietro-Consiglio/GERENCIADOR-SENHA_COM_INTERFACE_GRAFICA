import PySimpleGUI as sg


def Tela_Login():
    sg.theme('DarkBlack')
    layout = [
        [sg.Text('Login',font='Verdana'),sg.Input(key='login',pad=10)],
        [sg.Text('Senha',font='Verdana'),sg.Input(key='senha',pad=10,password_char='*')],
        [sg.Button('Logar',font='Verdana',button_color='SNOW',pad=10),sg.Button('Voltar',font='Verdana',button_color='SNOW',pad=10)],
        [sg.Text('',key='Mensagem',font='Verdana')],
        [sg.Text('Versão 1.0')]
    ]

    return sg.Window('Login',layout=layout,finalize=True,element_justification='c')
    
 



def Tela_Cadastro():
    sg.theme('DarkBlack')
    layout = [
        [sg.Text('Nome',font='Verdana'),sg.Input(key='nome',pad=10)],
        [sg.Text('Senha',font='Verdana'),sg.Input(key='senha',pad=10,password_char='*')],
        [sg.Text('E-mail',font='Verdana'),sg.Input(key='email',pad=10)],
        [sg.Button('Enviar dados',font='Verdana',pad=10,button_color='SNOW'),sg.Button('Já tenho cadastro',font='Verdana',pad=10,button_color='SNOW')],
        [sg.Text('',key='Mensagem',font='Verdana')],
        [sg.Text('Versão 1.0')]
    ]
    return sg.Window('Cadastro',layout=layout,finalize=True,element_justification='c')   

 
        
def Tela_Opcoes():
    sg.theme('DarkBlack')
    layout = [
        [sg.Button('Cadastrar Credencial', font='Verdana',button_color='SNOW',pad=10,border_width=5)],
        [sg.Button('Ver Credenciais',font='Verdana',button_color='SNOW',pad=10,border_width=5)],
        [sg.Button('Configurações',font='Verdana',button_color='SNOW',pad=10,border_width=5)],
        [sg.Button('Excluir Conta',font='Verdana',button_color='SNOW',pad=10,border_width=5)],
        [sg.Text('Versão 1.0')]
    ]
        
    return sg.Window('Opções',layout=layout,finalize=True,element_justification='c')
        
def Tela_Cadastrar_Credencial():
    sg.theme('DarkBlack')
    layout = [
        [sg.Text('Site',font='Verdana'),sg.Input(key='site',pad=10)],
        [sg.Text('Usuário',font='Verdana'),sg.Input(key='usuario',pad=10)],
        [sg.Text('Senha',font='Verdana'),sg.Input(key='senha',password_char='*',pad=10)],
        [sg.Button('Cadastrar',font='Verdana',pad=10,button_color='SNOW'),sg.Button('Voltar',font='Verdana',pad=10,button_color='SNOW')],
        [sg.Text('',key='Mensagem',font='Verdana')]
    ]
        
    return sg.Window('Cadastro de credenciais',layout=layout,finalize=True,element_justification='c')
        


def Tela_Validacao_Email():
    sg.theme('DarkBlack')
    layout = [
        [sg.Text('Valide seu E-mail',font='Verdana',pad=10)],
        [sg.Input(key='codigo',border_width=5)],
        [sg.Button('Validar',font='Verdana',pad=10,button_color='SNOW'),sg.Button('Voltar',font='Verdana',pad=10,button_color='SNOW')],
        [sg.Text('',key='Mensagem')],
        [sg.Text('Versão 1.0')]
        
    ]

    return sg.Window('Validação de E-mail',layout=layout,finalize=True,element_justification='c')


def Tela_Ver_Credenciais():
    sg.theme('DarkBlack')
    layout = [
        [sg.Text('Suas credenciais',font='Verdana')],
        [sg.Output(size=(50,20),background_color='Black',text_color='GREEN',font='Verdana',key='Mensagem',)],
        [sg.Button('Buscar',font='Verdana',button_color='SNOW'),sg.Button('Voltar',font='Verdana',button_color='SNOW')],
        [sg.Button('Excluir',font='Verdana',button_color='RED'),sg.Text('Id de credencial que deseja excluir: '), sg.Input(key='id_credencial')],
        [sg.Button('Alterar',font='Verdana',button_color='YELLOW'),sg.Text('Id de credencial que deseja alterar: '), sg.Input(key='id_credencial1')],
        [sg.Text('Versão 1.0')]
    ]

    return sg.Window('Suas Credenciais',layout=layout,finalize=True,element_justification='c')
          

def Tela_Configuracoes():
    sg.theme('DarkBlack')
    layout = [
        [sg.Text("Suas informações",font='Verdana')],
        [sg.Text("Nome",pad=10,font='Verdana'),sg.Input(key="nome")],
        [sg.Text("Senha",pad=10,font='Verdana'),sg.Input(key="senha")],
        [sg.Text("E-mail",pad=10,font='Verdana'),sg.Input(key="email",)],
        [sg.Button("Ver dados",pad=10,font='Verdana',button_color='SNOW'),sg.Button("Alterar",pad=10,font='Verdana',button_color='SNOW'),sg.Button("Voltar",pad=10,font='Verdana',button_color='SNOW')],
        [sg.Text("",key="Mensagem",font='Verdana',pad=10)]
    ]

    return sg.Window("Seus dados cadastrais",layout=layout,finalize=True,element_justification="c")


def Tela_Alterar_Credencial():
    sg.theme('DarkBlack')
    layout = [
        [sg.Text("Informação da sua credencial",font='Verdana')],
        [sg.Text("Site",pad=10,font='Verdana'),sg.Input(key="site")],
        [sg.Text("Usuário",pad=10,font='Verdana'),sg.Input(key="usuario")],
        [sg.Text("Senha",pad=10,font='Verdana'),sg.Input(key="senha",)],
        [sg.Button("Ver dados",pad=10,font='Verdana',button_color='SNOW'),sg.Button("Alterar",pad=10,font='Verdana',button_color='SNOW'),sg.Button("Voltar",pad=10,font='Verdana',button_color='SNOW')],
        [sg.Text('',key="Mensagem")]
    ]

    return sg.Window("Alterar Credencial",layout=layout,finalize=True,element_justification="c")

