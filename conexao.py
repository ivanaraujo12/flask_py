import mysql.connector
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


def executar(sql, fetch=False):
    try:
        con = mysql.connector.connect(host='localhost',database='python',user='root',password='')
        if con.is_connected():
             print(sql)
             cursor = con.cursor()
             cursor.execute(sql)
             con.commit()
             print("Conectado ao banco de dados ")
             if fetch:
                return cursor.fetchall()
    except mysql.connector.Error as erro:
        messagebox.showinfo(f"Erro ao conectar ao banco de dados: {erro}")


def pesquisar():
    id_cliente = codigo.get()
    sql = f"SELECT * FROM cad_cliente WHERE cod= {id_cliente};"
    print(sql)
    resultados = executar(sql, fetch=True)  # Obtemos todos os resultados

    if resultados:
        resultado = resultados[0]  # Pegamos o primeiro resultado
        janela_resultado = tk.Toplevel(root)
        janela_resultado.title("Resultado da Pesquisa")
        
        ttk.Label(janela_resultado, text=f"ID: {resultado[0]}").pack()
        ttk.Label(janela_resultado, text=f"Nome: {resultado[1]}").pack()
        ttk.Label(janela_resultado, text=f"Endereço: {resultado[2]}").pack()
        ttk.Label(janela_resultado, text=f"CPF: {resultado[3]}").pack()

def editar():
    sql = f"update cad_cliente set nome='{nome.get()}', endereco='{ende.get()}', cpf='{cpf.get()}' where cod= {codigo.get()}"
    executar(sql)


def excluir():
    sql = f"DELETE FROM cad_cliente WHERE cod = {codigo.get()}"
    executar(sql) 

def limpar():   
   codigo.set("")
   nome.set("")
   ende.set("")
   cpf.set("")
   
def adicionar():
    id_codigo= codigo.get()
    id_nome= nome.get()
    id_endereco= ende.get()
    id_cpf= cpf.get()

    sql = f"insert into cad_cliente(cod, nome, endereco,cpf ) values({id_codigo},'{id_nome}','{id_endereco}','{id_cpf}');"
    executar(sql)
    
root = tk.Tk()
frame = ttk.Frame(root, padding=100)
frame.grid()

ttk.Label(frame,text="Codigo: ").grid(column=0,row=0)
codigo = StringVar()
ttk.Entry(frame, textvariable=codigo).grid(column=1, row = 0)

ttk.Label(frame,text="Nome: ").grid(column=0,row=1)
nome = StringVar()
ttk.Entry(frame, textvariable=nome).grid(column=1, row = 1)

ttk.Label(frame,text="Endereço: ").grid(column=0,row=2)
ende = StringVar()
ttk.Entry(frame, textvariable=ende).grid(column=1, row = 2)

ttk.Label(frame,text="CPF: ").grid(column=0,row=3)
cpf = StringVar()
ttk.Entry(frame, textvariable=cpf).grid(column=1, row = 3)

ttk.Label(frame,text="              ").grid(column=2,row=0)

var = 3

ttk.Button(frame, text ="Todos", command=frame).grid(column=var,row=0)
ttk.Button(frame, text ="Pesquisar", command=pesquisar).grid(column=var,row=1)
ttk.Button(frame, text ="Adicionar", command=adicionar).grid(column=var,row=2)
ttk.Button(frame, text ="Editar", command=editar).grid(column=var,row=3)
ttk.Button(frame, text ="Excluir", command=excluir).grid(column=var,row=4)
ttk.Button(frame, text ="Limpar", command=limpar).grid(column=var,row=5)
ttk.Button(frame, text ="Imprimir", command=frame).grid(column=var,row=6)
ttk.Button(frame, text ="Sair", command=frame.destroy).grid(column=1 ,row=7)

frame.mainloop()