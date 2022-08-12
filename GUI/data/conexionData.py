from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from directory import getDirectory
from tkcalendar import Calendar, DateEntry
from data.sql import *


#pestaña conexion a base de datos

#imagen del programa
ruta = getDirectory()

def conexionBD():
    nuevaPestanna = Toplevel()
    nuevaPestanna.config(background="#E6EDf5")
    nuevaPestanna.title("Conexión a la base de datos")
    nuevaPestanna.geometry("320x300")
    nuevaPestanna.iconbitmap(ruta)

    dbInputName = Entry(nuevaPestanna)
    dbInputName.place(x=85,y=60)
    labelDBName = Label(nuevaPestanna, text="Base de datos:", bg="#E6EDf5", font=("Bell MT", 8, BOLD))
    labelDBName.place(x=10,y=60)

    labelTituloDB = Label(nuevaPestanna, text="Ingresar credenciales de la base de datos:", bg="#E6EDf5", font=("Bell MT", 11, BOLD))
    labelTituloDB.place(relx=0.5, rely=0.05, anchor=CENTER)   

    dbInputTable = Entry(nuevaPestanna)
    dbInputTable.place(x=110,y=90)
    labelDBTable = Label(nuevaPestanna, text=" Nombre de la tabla:", bg="#E6EDf5", font=("Bell MT", 8, BOLD))
    labelDBTable.place(x=5,y=90)

    dbInputUsuario = Entry(nuevaPestanna)
    dbInputUsuario.place(x=85,y=120)
    labelDBUsuario = Label(nuevaPestanna, text="Usuario:", bg="#E6EDf5", font=("Bell MT", 8, BOLD))
    labelDBUsuario.place(x=10,y=120)

    dbInputPassword = Entry(nuevaPestanna)
    dbInputPassword.place(x=85,y=150)
    labelDBPassword = Label(nuevaPestanna, text="Contraseña:", bg="#E6EDf5", font=("Bell MT", 8, BOLD))
    labelDBPassword.place(x=10,y=150)

    def resolucionConexion():
        conexion = Toplevel()
        conexion.config(background="#E6EDf5")
        conexion.geometry("400x100")
        conexion.title("Conexión a la base de datos")
        # pendiente poner mensaje condicional si la conexion fue exitosa o fue fallda
        Label(conexion, text="Conexión realizada con exito", bg="#E6EDf5", font=("Bell MT", 14, BOLD)).place(relx=0.5, rely=0.2, anchor=CENTER)

        def cerrarPestannas():
            nuevaPestanna.destroy()
            conexion.destroy()
    

        botonFinalizar = Button(conexion, text="Aceptar", command=cerrarPestannas)
        botonFinalizar.config(bg="#5089eb", cursor="hand2")
        botonFinalizar.place(relx=0.5, rely=0.5, anchor=CENTER)

    def storeVariables():
        #conection data storage
        db = dbInputName.get()
        table = dbInputTable.get()
        user = dbInputUsuario.get()
        password = dbInputPassword.get()

        conectar(db, table, user, password)

        resolucionConexion()

        

        
    

    botonEstablecerConexion = Button(nuevaPestanna, text="Conectar", command=storeVariables)
   
    botonEstablecerConexion.config(bg="#5089eb", width=20, cursor="hand2")
    botonEstablecerConexion.place(relx=0.5, rely=0.76, anchor=CENTER)

    





