import tkinter as tk
from tkinter import ttk

raiz=tk.Tk()

def usuarioNuevo(evento):
    contador=0
    nombre=identidad.get()
    lastName=apellido.get()
    phone=telefono.get()
    correoElectronico=email.get()
    ubicacion=direccion.get()

    agenda.insert('',contador,contador, text=contador, values=(nombre,lastName,phone,correoElectronico,ubicacion))

    contador=contador+1
    

ttk.Label(raiz, text="nombre").pack(padx=5,pady=5)
identidad=ttk.Entry(raiz)
identidad.bind("<Return>", usuarioNuevo)
identidad.pack(padx=10,pady=10)


ttk.Label(raiz, text="apellido").pack(padx=5,pady=5)
apellido=ttk.Entry(raiz)
apellido.bind("<Return>",usuarioNuevo)
apellido.pack(padx=10,pady=10)

ttk.Label(raiz, text="telefono").pack(padx=5,pady=5)
telefono=ttk.Entry(raiz)
telefono.bind("<Return>",usuarioNuevo)
telefono.pack(padx=10,pady=10)

ttk.Label(raiz, text="email").pack(padx=5,pady=5)
email=ttk.Entry(raiz)
email.bind("<Return>",usuarioNuevo)
email.pack(padx=10,pady=10)

ttk.Label(raiz, text="direccion").pack(padx=5,pady=5)
direccion=ttk.Entry(raiz)
direccion.bind("<Return>",usuarioNuevo)
direccion.pack(padx=10,pady=10)


boton=ttk.Button(raiz, text="Pinche el boton o presione enter para guardar los valores")
boton.bind("<Button-1>", usuarioNuevo)
boton.pack()


agenda=ttk.Treeview(raiz, columns=('nombre','apellido','telefono','email','direccion'))
agenda.heading("#0", text="ID")
agenda.heading("nombre",text="nombre")
agenda.heading("apellido",text="apellido")
agenda.heading("telefono",text="telefono")
agenda.heading("email",text="email")
agenda.heading("direccion",text="dirección")



agenda.pack(padx=25,pady=25)


raiz.mainloop()