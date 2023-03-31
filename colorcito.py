#lorenzo hernandez hernandez 
from tkinter import *
from tkinter import messagebox as messageBox
from tkinter import ttk
from tkinter import colorchooser as colorChooser 
root=Tk()
root.geometry()


def Cambiando():
    
    print("#"+color.get()+color2.get()+color3.get())
    x=color.get()+color2.get()+color3.get()
    if len(x)>6:
       BB.config(text=f'Tienes mas numeros de lo requerido')

    elif len(x)<6:
       BB.config(text=f'No son suficientes numeros')
   
    else:
     ventanaPrincipal.config(bg=("#"+color.get()+color2.get()+color3.get()))
    

color=StringVar()
color2=StringVar()
color3=StringVar()
ventanaPrincipal=Frame(root)
ventanaPrincipal.pack(fill="both", expand=1)

Titul=Label(ventanaPrincipal,text="Introduce un valor de 6 digitos",font=("Vanilla Caramel",25))
Titul.grid(row=1,column=2,padx=5,pady=5)

Rojito=Label(ventanaPrincipal,text="Rojito",font=("Vanilla Caramel",20))
Rojito.grid(row=3,column=1,padx=5,pady=5)
Pcolor=Entry(ventanaPrincipal,textvariable=color,font=("Vanilla Caramel",10))
Pcolor.grid(row=3,column=2,padx=5,pady=5)

verdecito=Label(ventanaPrincipal,text="verde",font=("Vanilla Caramel",20))
verdecito.grid(row=6,column=1,padx=5,pady=5)
Scolor=Entry(ventanaPrincipal,textvariable=color2,font=("Vanilla Caramel",10))
Scolor.grid(row=6,column=2,padx=5,pady=5)

Azulito=Label(ventanaPrincipal,text="Azul",font=("Vanilla Caramel",20))
Azulito.grid(row=9,column=1,padx=5,pady=5)
Tcolor=Entry(ventanaPrincipal,textvariable=color3,font=("Vanilla Caramel",10))
Tcolor.grid(row=9,column=2,padx=5,pady=5)


CambiandoColor=Button(ventanaPrincipal,text="RESULTADO",font=("Vanilla Caramel",15),command=Cambiando)
CambiandoColor.grid(row=13,column=2,padx=5,pady=5)

BB = Label(ventanaPrincipal, text="", font=("Vanilla Caramel",15))
BB.grid(row=15, column=2, padx=10, pady=10)


root.mainloop()