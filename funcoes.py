import sqlite3
import time
import os
import random
import PySimpleGUI as sg


def send_to_txt(msg):
    os.chdir(r"C:\\Users\\Public\\GERENCIADOR-SENHAS\\")
    log = open('log.txt', 'a')
    hora = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())
    log.write(f'{hora} -> {msg}\n')
    log.close()


def gerador_senhas(qtd):
    f = 0
    senha = ''
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letras_grandes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    especiais = ['!', '@', '#', '$', '%', '*', '&']
    senha2 = []
    escolha = ['a','b','c','d']
    while f < qtd:
        f += 1
        a = random.choice(especiais)
        b = random.randint(0, 9)
        c = random.choice(letras_grandes)
        d = random.choice(letras)
        decisao = random.choice(escolha)
                
        if decisao == 'a':
            senha2.append(a)    

        elif decisao == 'b':
            senha2.append(b)

        elif decisao == 'c':
            senha2.append(c)

        elif decisao == 'd':
            senha2.append(d)   

    random.shuffle(senha2)  
    senha = "".join(str(v) for v in senha2)
    return senha


def get_information(nome):
    id = []
    site = []
    user = []
    senha = []
    try:
        banco = sqlite3.connect('gerenciador-senhas.db')
        cursor = banco.cursor()
        cursor2 = banco.cursor()
        cursor3 = banco.cursor() 
        cursor4 = banco.cursor()
        cursor.execute(F"SELECT id FROM contas WHERE nome = '{nome}'")
        cursor2.execute(F"SELECT site FROM contas WHERE nome = '{nome}'")
        cursor3.execute(F"SELECT usuario FROM contas WHERE nome = '{nome}'")
        cursor4.execute(F"SELECT senha FROM contas WHERE nome = '{nome}'")
        id = cursor.fetchall()
        site = cursor2.fetchall()
        user = cursor3.fetchall()
        senha = cursor4.fetchall()
        cursor.execute(F"SELECT id,site,usuario,senha FROM contas WHERE nome = '{nome}'")
        lista = cursor.fetchall()
                        

    except Exception as erro:
        send_to_txt(erro)
        sg.popup("Erro ao buscar informações!")   
        
       
        
    if len(lista) == 0:
            print('Sem credenciais cadastradas!')
    else:
        cont = -1
        try:
            while True:
                cont += 1 
                id_to_str = str(id[cont]).replace("(","").replace(")","").replace(","," ").replace("'","")
                site_to_str = str(site[cont]).replace("(","").replace(")","").replace(","," ").replace("'","")
                user_to_str = str(user[cont]).replace("(","").replace(")","").replace(","," ").replace("'","")
                senha_to_str = str(senha[cont]).replace("(","").replace(")","").replace(","," ").replace("'","")
                print(F" Identificador: {id_to_str}")
                print(F" Site: {site_to_str}")
                print(F" Usuário: {user_to_str}")
                print(F" Senha: {senha_to_str}")
                print('')
                print('')
                    
        except Exception as erro:
            pass
            send_to_txt(erro)  
             