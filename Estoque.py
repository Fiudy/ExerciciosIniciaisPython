#Importando Tkinter e Ttk
from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox

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
b1 = ttk.Button(janela, text="Botão Novo").pack()


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