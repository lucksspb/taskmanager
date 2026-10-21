from tkinter import *
from tkinter import ttk

def saudar():
    nome = campo.get()
    if nome:
        msg.config(text = f"olar {nome}")
    else:
        msg.config(text = "poe o nome ai pae q isso")



root = Tk()
frame = ttk.Frame(root, padding=100)
root.title("Task manager do Borba")
root.geometry("600x400")
frame.grid()

ttk.Label(frame, text = "Digite seu nome").grid(column = 0, row = 0) # texto

campo = ttk.Entry(root)
campo.grid(column=1, row = 1) # para digitar algo 

ttk.Button(frame, text = "Enviar", command= saudar).grid(column = 0, row = 2) 

msg = ttk.Label(frame, text="")
msg.grid(column= 0, row = 4)

ttk.Button(frame, text = "sair", command= quit).grid(column = 0, row = 6) 

root.mainloop()
