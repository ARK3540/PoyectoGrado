import  Tkinter
from Tkinter import*


def Grafic():
    #root.iconify()
    otra_ventana= Tkinter.Toplevel(root)
    #otra_ventana.title("")
    otra_ventana.geometry("339x95")
    otra_ventana.resizable(False, False)
    Phot=PhotoImage(file='Tab1.gif')
    fondo=Label(otra_ventana,image=Phot)
    fondo.pack()
    bot = Tkinter.Button(otra_ventana,text="Detener",cursor='hand1', command=otra_ventana.destroy)
    bot.place(x=230, y=60, width=100, height=30)
    root.mainloop()

root = Tkinter.Tk()
root.title("Interprete Graficador")
root.geometry("300x300")
root.resizable(False, False)
photo = PhotoImage(file='Intro.gif')
fondo=Label(root,image=photo)
fondo.pack()
boton = Tkinter.Button(root,text="Grabar",activeforeground="#6e0987", relief='flat',cursor='hand1', command=Grafic)
boton.place(x=80, y=160, width=150, height=30)
boton1 = Tkinter.Button(root,text="Revisualizar",activeforeground="#6e0987", relief='flat',cursor='hand1', command=Grafic)
boton1.place(x=80 , y=210, width=150, height=30)
boton2 = Tkinter.Button(root,text="Salir",activeforeground="#6e0987", relief='flat',cursor='hand1', command=root.destroy)
boton2.place(x=177, y=260, width=100, height=30)
root.mainloop()
