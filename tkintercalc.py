#Importando Tkinter e Ttk
import tkinter as tk
import tkinter.ttk as ttk

janela = tk.Tk()
janela.geometry("800x600")
janela.title("NoteBooks")
n = ttk.Notebook(janela)
frm1 = tk.Frame(n, relief="ridge", borderwidth=6)
frm2 = tk.Frame(n, relief="raised", borderwidth=6)
frm3 = tk.Frame(n, relief="raised", borderwidth=6)
txt1 = ttk.Label(frm1, text="Essa é a Guia 1")
txt2 = ttk.Label(frm2, text="Essa é a Guia 2")
txt3 = ttk.Label(frm3, text="Essa é a Guia 3")
n.add(frm1, text="Guia 1")
n.add(frm2, text="Guia 2")
n.add(frm3, text="Guia 3")
tk.Entry(frm2).pack()
n.pack(fill=tk.BOTH, expand=1)
txt1.pack(fill=tk.BOTH, expand=1)
txt2.pack(fill=tk.BOTH, expand=1)
txt3.pack(fill=tk.BOTH, expand=1)
b1= ttk.Button(frm3, text="Botão NOVO").pack()

janela.mainloop()













exit()
# Criando janela
janela = Tk()
janela.title("Exemplo combobox")
janela.geometry("600x400")
# Dias da semana
dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira",
               "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
# Criando o combobox
combo = StringVar()
combobox = ttk.Combobox(janela, values=meses, textvariable=combo)
combobox.pack(padx=75, pady=20)

b = Button(janela, text="Mostrar", 
           command=lambda: messagebox.showinfo(title="AVISO", message=combo.get()) )
b.pack()
b1= ttk.Button(janela, text="Botão NOVO").pack()

janela.mainloop()





exit()

root = tk.Tk()
root.title('Sizegrip Demo')
root.geometry('300x200')
root.resizable(False, False)

# grid layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create the sizegrip
sg = ttk.Sizegrip(root)
sg.grid(row=1, sticky=tk.SE)


root.mainloop()