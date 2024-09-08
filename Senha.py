from cryptography.fernet import Fernet, InvalidToken
from PyQt5 import uic, QtWidgets
import mysql.connector
from mysql.connector import Error


def salvar_chave(key):
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(key)

def carregar_chave():
    with open("chave.key", "rb") as chave_arquivo:
        return chave_arquivo.read()


try:
    key = carregar_chave()
except FileNotFoundError:
    key = Fernet.generate_key()
    salvar_chave(key)

cipher_suite = Fernet(key)


banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="senhas"
)

def criptografar(texto):
    
    return cipher_suite.encrypt(texto.encode()).decode()

def descriptografar(texto):
    
    try:
        return cipher_suite.decrypt(texto.encode()).decode()
    except InvalidToken:
        print("Token de criptografia inválido.")
        return None

def abrir_forms():
    
    tela_login.label_4.setText("")  
    nome_usuario = tela_login.lineEdit.text()
    senha = tela_login.lineEdit_2.text()
    
    try:
        cursor = banco.cursor()
        cursor.execute("SELECT senha FROM cadastro WHERE login = %s", (nome_usuario,))
        senha_sql = cursor.fetchall()
        cursor.close()

        
        if senha_sql:
            senha_armazenada = senha_sql[0][0]
            senha_descriptografada = descriptografar(senha_armazenada)
            if senha_descriptografada and senha == senha_descriptografada:
                tela_login.close()  
                forms.show()        
            else:
                tela_login.label_4.setText("Senha incorreta.")  
        else:
            tela_login.label_4.setText("Usuário não encontrado.")  

    except Error as e:
        print("Erro ao validar senha:", e)
        tela_login.label_4.setText("Erro ao validar senha.")  

def funcao_principal():
    
    linha1 = forms.lineEdit.text()
    linha2 = forms.lineEdit_2.text()

    print("Aplicativo:", linha1)
    print("Senha:", linha2)
    
    try:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO informacao (app, senha) VALUES (%s, %s)"
        dados = (linha1, linha2)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        cursor.close()
    except Error as e:
        print("Erro ao inserir dados:", e)
    
    forms.lineEdit.setText("")
    forms.lineEdit_2.setText("")

def chamar_segunda_tela():
    
    segunda_tela.show()
    try:
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM informacao")
        dados_lidos = cursor.fetchall()
        cursor.close()

        segunda_tela.tableWidget.setRowCount(len(dados_lidos))
        segunda_tela.tableWidget.setColumnCount(3)

        for i in range(len(dados_lidos)):
            for j in range(3):
                segunda_tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    except Error as e:
        print("Erro ao carregar dados:", e)

def excluir_dados():
    
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    try:
        cursor = banco.cursor()
        cursor.execute("SELECT id FROM informacao")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM informacao WHERE id = %s", (valor_id,))
        banco.commit()
        cursor.close()
    except Error as e:
        print("Erro ao excluir dados:", e)

def abre_tela_cadastro():
    
    tela_cadastro.show()

def cadastrar():
    
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    if senha == c_senha:
        try:
            cursor = banco.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cadastro (
                    nome VARCHAR(255),
                    login VARCHAR(255),
                    senha VARCHAR(255)
                )
            """)
            cursor.execute("""
                INSERT INTO cadastro (nome, login, senha) 
                VALUES (%s, %s, %s)
            """, (nome, login, criptografar(senha)))
            banco.commit()
            cursor.close()
            tela_cadastro.label.setText("Usuário cadastrado com sucesso!")
        except Error as e:
            print("Erro ao inserir os dados:", e)
            tela_cadastro.label.setText("Erro ao cadastrar usuário.")
    else:
        tela_cadastro.label.setText("As senhas digitadas não conferem.")


app = QtWidgets.QApplication([])
forms = uic.loadUi("formSenha.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_login = uic.loadUi("tela_login.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")


tela_login.pushButton.clicked.connect(abrir_forms)
tela_login.pushButton_2.clicked.connect(abre_tela_cadastro)
forms.pushButton.clicked.connect(funcao_principal)
forms.pushButton_2.clicked.connect(chamar_segunda_tela)
segunda_tela.pushButton.clicked.connect(excluir_dados)
tela_cadastro.pushButton.clicked.connect(cadastrar)


tela_login.show()
app.exec()
