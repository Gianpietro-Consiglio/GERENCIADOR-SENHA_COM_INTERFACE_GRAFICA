import sqlite3
import funcoes
import os
import PySimpleGUI as sg
import telas
import time
import webbrowser
import sys

"""

JANELA0 = TELA PRINCIPAL
JANELA1 = TELA CADASTRO
JANELA2 = TELA LOGIN
JANELA3 = TELA OPCOES 
JANELA4 = TELA CADASTRO_CREDENCIAL
JANELA6 = TELA VER CREDENCIAIS
JANELA7 = TELA VER CONFIGURAÇÕES
JANELA8 = TELA ALTERAR CREDENCIAL
JANELA9 = TELA INFOS 

"""

try:
    os.mkdir(r"C:\\Users\\Public\\GERENCIADOR-SENHAS\\")
    
except Exception as erro:
    funcoes.send_to_txt(erro)    
    pass
    

try:
    os.chdir(r"C:\\Users\\Public\\GERENCIADOR-SENHAS\\")

except Exception as erro:
    funcoes.send_to_txt(erro)  
    sg.popup('Erro ao localizar diretório!') 
    sys.exit()

try:
    banco = sqlite3.connect('gerenciador-senhas.db')
    cursor = banco.cursor()
    cursor2 = banco.cursor()
    cursor3 = banco.cursor() 
    cursor4 = banco.cursor()  
    cursor.execute("CREATE TABLE user(id integer primary key, nome text, senha text, cadastro text, ultima_alteracao text)")
    cursor.execute("CREATE TABLE contas(id integer primary key, nome text, site text, usuario text, senha text, cadastro text, ultima_alteracao text)")
    banco.commit()
                     
except Exception as erro:
    funcoes.send_to_txt(erro)
    pass

global nome,senha,email,nome_antigo,teste_nome,site1,senha_credencial1,usuario1,query_to_window8,senha1
janela0,janela1,janela2,janela3,janela4,janela5,janela6,janela7,janela8,janela9 = telas.Tela_Principal(),None,None,None,None,None,None,None,None,None
while True:
    window,event,values = sg.read_all_windows()
    if window == janela8 and event == 'Gerar senha':
        maximo = 100
        try:
            quantidade = values['quantidade']
            quantidade = int(quantidade)
            if quantidade > maximo:
                sg.popup('Máximo de caracteres: 100')
                continue
            senha_gerada = funcoes.gerador_senhas(quantidade)
        except Exception as erro:
            funcoes.send_to_txt(erro)
            sg.popup('Não foi possível gerar sua senha')
            window['quantidade'].update('')
        else:
            window['senha'].update(senha_gerada)
            window['quantidade'].update('')
            window['Mensagem'].update('')

    elif window == janela8 and event == "Ver dados":
        try:
            cursor.execute(F"SELECT site FROM contas WHERE id = {query_to_window8} ")
            cursor2.execute(F"SELECT usuario FROM contas WHERE id = {query_to_window8} ")
            cursor3.execute(F"SELECT senha FROM contas WHERE id = {query_to_window8} ")
        except Exception as erro:
            funcoes.send_to_txt(erro)
            sg.popup('Erro ao buscar informações!')    
        site1 = cursor.fetchall()
        site1 = str(site1).replace("(","").replace(")","").replace("[","").replace("]","").replace(",","").replace("'","")
        usuario1 = cursor2.fetchall()
        usuario1 = str(usuario1).replace("(","").replace(")","").replace("[","").replace("]","").replace(",","").replace("'","")
        senha1 = cursor3.fetchall()
        senha1 = str(senha1).replace("(","").replace(")","").replace("[","").replace("]","").replace(",","").replace("'","")
        window['site'].update(site1) 
        window['usuario'].update(usuario1)
        window['senha'].update(senha1)

    elif window == janela6 and event == 'Avistar':
        try:
            id = values['id_credencial2']
            cursor.execute(F'SELECT site FROM contas where id = {id}')
            site = cursor.fetchall()
        except Exception as erro:
            funcoes.send_to_txt(erro)
            sg.popup('Erro ao abrir site')    
        else:
            window['id_credencial2'].update('')
            try:
                site = str(site).replace("(","").replace(")","").replace("[","").replace("]","").replace(",","").replace("'","")
            except Exception as erro:
                funcoes.send_to_txt(erro)
                sg.popup('Erro ao abri site')
            else:
                webbrowser.open(site)

    elif window == janela8 and event == "Alterar":
        consulta_site = values['site'] 
        consulta_user = values['usuario']
        consulta_senha = values['senha']
        if consulta_site == '':
            window['Mensagem'].update("Preencha campo Nome!")
            continue

        elif consulta_user == '':
            window['Mensagem'].update("Preencha campo Senha!") 
            continue

        try:
            cursor.execute(F"UPDATE contas SET site = '{values['site']}' WHERE id = {query_to_window8}")
            banco.commit()
            cursor.execute(F"UPDATE contas SET usuario = '{values['usuario']}' WHERE id = {query_to_window8}")
            banco.commit()
            cursor.execute(F"UPDATE contas SET senha = '{values['senha']}' WHERE id = {query_to_window8}")
            banco.commit()
        except Exception as erro:
            funcoes.send_to_txt(erro)
            sg.popup('Erro ao alterar dados')  
        else:
            sg.popup('Sucesso ao alterar dados') 

               

    elif window == janela7 and event == 'Ver dados':
        cursor2.execute(F"SELECT nome FROM user WHERE nome = '{nome}' ")
        cursor3.execute(F"SELECT senha FROM user WHERE nome = '{nome}' ")
        nome = cursor2.fetchall()
        nome = str(nome).replace("(","").replace(")","").replace("[","").replace("]","").replace(",","").replace("'","")
        senha = cursor3.fetchall()
        senha = str(senha).replace("(","").replace(")","").replace("[","").replace("]","").replace(",","").replace("'","")
        window['nome'].update(f"{nome}") 
        window['senha'].update(f"{senha}")
                        
    elif window == janela7 and event == 'Alterar':
        consulta_nome = values['nome'] 
        consulta_senha = values['senha']
        cursor.execute(F"SELECT nome FROM user WHERE nome = '{consulta_nome}' ")
        x = cursor.fetchall()
        if len(x) > 0:
            window['Mensagem'].update("Nome indisponível!")
            continue
        
        elif consulta_nome == '':
            window['Mensagem'].update("Preencha campo Nome!")
            continue

        elif consulta_senha == '':
            window['Mensagem'].update("Preencha campo Senha!") 
            continue

        else:
            try:
                cursor.execute(F"UPDATE user SET nome = '{values['nome']}' WHERE nome = '{nome}'")
                banco.commit()
                cursor.execute(F"UPDATE user SET senha = '{values['senha']}' WHERE nome = '{nome}'")
                banco.commit()
            
            except Exception as erro:
                funcoes.send_to_txt(erro)
                sg.popup('Erro ao alterar dados')  
            else:
                sg.popup('Sucesso ao alterar dados') 

            try:
                cursor.execute(F"UPDATE contas SET nome = '{consulta_nome}' WHERE nome = '{nome_antigo}'") 
                banco.commit()
                sg.popup('Por favor, realize login novamente!')
                janela7.hide()
                janela2.un_hide()

            except Exception as erro:
                funcoes.send_to_txt(erro)
                sg.popup('Erro ao concluir processo de alterações nas credenciais!')            

    elif window == janela1 and event == 'Enviar dados':
        consulta_nome = values['nome']
        consulta_senha = values['senha']
        cursor.execute(F"SELECT nome from user WHERE nome = '{consulta_nome}'")                
        query = cursor.fetchall() 
        if len(query) > 0:
            window['Mensagem'].update('Nome indisponível!')
            continue

        elif consulta_nome == '':
            window['Mensagem'].update("Preencha campo Nome!")
            continue

        elif consulta_senha == '':
            window['Mensagem'].update("Preencha campo Senha!") 
            continue

        else:
            try:
                hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
                cursor.execute(F"INSERT INTO user(nome,senha,cadastro) VALUES('{consulta_nome}','{consulta_senha}','{hora}')")
                banco.commit()
            
            except Exception as erro:
                funcoes.send_to_txt(erro)
                sg.popup('Erro ao enviar informações para banco de dados!')
                continue 

            else:
                sg.popup("Cadastro finalizado com sucesso!")
                janela1.hide()
                janela0.un_hide()
   

    elif window == janela2 and event == 'Logar':
        try:
            nome_antigo = values['login']
            nome_antigo = str(nome_antigo)
            cursor = banco.cursor()
            cursor2 = banco.cursor()
            cursor.execute("SELECT nome FROM user WHERE nome = '" + nome_antigo + "'")
            cursor2.execute("SELECT senha FROM user WHERE nome = '" + nome_antigo + "' ")
            compara_login = cursor.fetchall()
            compara_senha = cursor2.fetchall()
                
            compara_login_transform = str(compara_login)
            compara_login_transform = compara_login_transform.replace("(", "").replace(")", "").replace("[","").replace("]","").replace(",","").replace("'","")
            compara_senha_transform = str(compara_senha)
            compara_senha_transform = compara_senha_transform.replace("(", "").replace(")", "").replace("[","").replace("]","").replace(",","").replace("'","")
           
        except Exception as erro:
            funcoes.send_to_txt(erro)
            window['Mensagem'].update("Processo de verificação falhou!")
            continue
           
        if values['login'] == compara_login_transform and values['senha'] == compara_senha_transform:
            nome = values['login']
            senha = values['senha']
            window['login'].update('')
            window['senha'].update('')
            window['Mensagem'].update('')
            sg.popup("Login realizado com sucesso!")
                        
            janela2.hide()
            janela3 = telas.Tela_Opcoes(nome)
                 
        elif len(compara_login) == 0:
            window['Mensagem'].update("Usuário não localizado!")
            continue 
                                                
        else: 
            window['Mensagem'].update("Login ou senha não correspondem!")
            continue

    
    elif window == janela4 and event == 'Limpar':
        window['site'].update('')
        window['usuario'].update('')
        window['senha'].update('')
        window['quantidade'].update('')

    elif window == janela8 and event == 'Limpar':
        window['site'].update('')
        window['usuario'].update('')
        window['senha'].update('')
        window['quantidade'].update('')    
        
    elif window == janela4 and event == 'Gerar senha':
        maximo = 100
        try:
            quantidade = values['quantidade']
            quantidade = int(quantidade)
            if quantidade > maximo:
                sg.popup('Máximo de caracteres: 100')
                continue
            senha_gerada = funcoes.gerador_senhas(quantidade)
        except Exception as erro:
            funcoes.send_to_txt(erro)
            sg.popup('Não foi possível gerar sua senha')
            window['quantidade'].update('')
        else:
            window['senha'].update(senha_gerada)
            window['quantidade'].update('')
            window['Mensagem'].update('')
        
    elif window == janela4 and event == 'Cadastrar':

        if values['site'] == '':
            window['Mensagem'].update("Preencha campo Site!") 
            continue          
        elif values['usuario'] == '':
            window['Mensagem'].update("Preencha campo Usuário!")  
            continue  
        elif values['senha'] == '':
            window['Mensagem'].update("Preencha campo Senha!")    
            continue   
        try:
            hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
            cursor.execute(F"INSERT INTO contas(nome, site, usuario, senha, cadastro) VALUES('{nome}','"+ values['site'] +"', '"+ values['usuario'] +"', '" + values['senha'] + "', '"+ hora +"')")
            banco.commit()
                            
        except Exception as erro:
            funcoes.send_to_txt(erro)
            window['Mensagem'].update("Erro ao enviar dados")  
            continue  

        else:
            window['site'].update('')
            window['usuario'].update('')
            window['senha'].update('')
            window['Mensagem'].update('')
            sg.popup("Dados enviados com sucesso")
  
    elif window == janela3 and event == 'Ver Credenciais':
        janela3.hide()   
        janela6 = telas.Tela_Ver_Credenciais() 

    elif window == janela6 and event == 'Buscar':
        window['Mensagem'].update('')
        funcoes.get_information(nome)
            
   
    if window == janela3 and event == 'Excluir Conta':
        try:
            cursor.execute(f"DELETE FROM user WHERE nome = '{nome}'")  
            cursor2.execute(f"DELETE FROM contas WHERE nome = '{nome}'")   
        except Exception as erro:
            sg.popup('Erro ao excluir conta!')   
            funcoes.send_to_txt(erro)    
        else:
            banco.commit()
            sg.popup('Conta excluída!')
            janela3.close()    
            janela0.un_hide()

    elif window == janela6 and event == 'Excluir':
        window['id_credencial'].update('')
        try:
            cursor.execute(F"SELECT id FROM contas WHERE id = {values['id_credencial']} AND nome = '{nome}'")
            query = cursor.fetchall()
            if len(query) == 0:
                sg.popup('Crdencial não localizada!')
                continue
            else:
                pass
        except Exception as erro:
            sg.popup('Erro ao pegar informações!')  
            funcoes.send_to_txt(erro)  
            continue

        try:
            cursor.execute(F"DELETE FROM contas WHERE id = {values['id_credencial']} AND nome = '{nome}' ") 
            banco.commit()
        except Exception as erro:
            sg.popup("Erro ao excluir credencial!")
            funcoes.send_to_txt(erro)
            continue
        else:
            sg.popup('Credencial excluída!')
            window['Mensagem'].update('')
            funcoes.get_information(nome)

    elif window == janela3 and event == sg.WIN_CLOSED:
        break     
    elif window == janela4 and event == sg.WIN_CLOSED:
        break    
    elif window == janela2 and event == sg.WIN_CLOSED:
        break             
    elif window == janela1 and event == sg.WIN_CLOSED:
        break
    elif window == janela6 and event == sg.WIN_CLOSED:
        break
    elif window == janela7 and event == sg.WIN_CLOSED:
        break
    elif window == janela8 and event == sg.WIN_CLOSED:
        break

    elif window == janela0 and event == sg.WIN_CLOSED:
        break
    elif window == janela0 and event == 'Sair':
        break

    elif window == janela4 and event == 'Voltar':
        janela4.hide()
        janela3.un_hide()        
            
    elif window == janela2 and event == 'Voltar':
        janela2.hide()
        janela0.un_hide()

    elif window == janela6 and event == 'Voltar':
        janela6.close()
        janela3.un_hide()   
   
   
    elif window == janela7 and event == 'Voltar':
        janela7.hide()
        janela3.un_hide()    

    elif window == janela8 and event == 'Voltar':
        janela8.close()
        janela6 = telas.Tela_Ver_Credenciais()         
        
    elif window == janela3 and event == 'Sair':
        janela3.hide()
        janela0.un_hide()        

    elif window == janela0 and event == 'Registrar':
        janela0.hide()
        janela1 = telas.Tela_Cadastro()  

    elif window == janela0 and event == 'Entrar':
        janela0.hide()
        janela2 = telas.Tela_Login()  
    
    
    elif window == janela6 and event == 'Alterar':
        window['id_credencial1'].update('')
        
        try:
            query_to_window8 = values['id_credencial1']
            cursor.execute(F"SELECT site FROM contas WHERE id = {values['id_credencial1']}")
            cursor2.execute(F"SELECT usuario FROM contas WHERE id = {values['id_credencial1']}")
            cursor3.execute(F"SELECT senha FROM contas WHERE id = {values['id_credencial1']}")
        except Exception as erro:
            funcoes.send_to_txt(erro)
            sg.popup("Erro ao carregar informações!")   
            continue
        else:
            site1 = cursor.fetchall()
            usuario1 = cursor2.fetchall()
            senha_credencial1 = cursor3.fetchall()
        
        if len(site1) == 0:
            sg.popup("Não foi possível localizar credencial!")
            continue
        elif len(usuario1) == 0:
            sg.popup("Não foi possível localizar credencial!")    
            continue
        elif len(senha_credencial1) == 0:
            sg.popup("Não foi possível localizar credencial!")   
            continue 
        else:
            window["id_credencial1"].update("") 
            janela6.hide()
            janela8 = telas.Tela_Alterar_Credencial()    

    
    elif window == janela3 and event == 'Configurações':
        janela3.hide()
        janela7 = telas.Tela_Configuracoes()

    elif window == janela1 and event == 'Voltar':
        janela1.hide() 
        janela0 = telas.Tela_Principal()

    elif window == janela3 and event == 'Cadastrar Credencial':
        janela3.hide()
        janela4 = telas.Tela_Cadastrar_Credencial()  

    elif window == janela0 and event == 'Infos':
        janela0.hide()    
        janela9 = telas.Tela_Infos()  

    elif window == janela9 and event == 'Instagram':
        webbrowser.open('https://www.instagram.com/gian_consiglio/')

    elif window == janela9 and event == 'GitHub':
        webbrowser.open('https://github.com/Gianpietro-Consiglio')   

    elif window == janela9 and event == 'Voltar':
        janela9.hide()         
        janela0.un_hide()

    elif window == janela9 and event == sg.WIN_CLOSED:
        break    

