from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from directory import getDirectory
from tkcalendar import DateEntry
from data.conexionData import *
from data.sql import *




root = Tk()
#titulo
root.title("Reportes - byJames")
#imagen del programa
ruta = getDirectory()
root.iconbitmap(ruta)
#tamaño de la ventana y ajustabilidad
root.resizable(0,0)
root.geometry("350x450")
root.config(bg="#00A86B")
#Creacion del frame
frame = Frame()
frame.pack()
frame.config(bg="#E6EDf5")
frame.config(width="345", height="447")
#widgets
labelTitulo = Label(frame, text="Generar reportes.", bg="#E6EDf5", font=("Bell MT", 12, BOLD))
labelTitulo.place(relx=0.5, rely=0.05, anchor=CENTER)
#widgets fechas
fechaInicio = DateEntry(frame, width=10, bg="white", foreground= "white",bd=2)
fechaInicio.place(x=40, y=100)
labelFechaInicio = Label(frame, text="Fecha inicio:", bg="#E6EDf5", font=("Bell MT", 10, BOLD))
labelFechaInicio.place(x=40, y=75)

fechaFin = DateEntry(frame, width=10, bg="white", foreground= "white",bd=2)
fechaFin.place(x=225, y=100)
labelFechaFin = Label(frame, text="Fecha fin:", bg="#E6EDf5", font=("Bell MT", 10, BOLD))
labelFechaFin.place(x=225, y=75)

#widget combo box selector de empresa
labelSelectEmpresa = Label(frame, text="Empresa a obtener reporte:", bg="#E6EDf5", font=("Bell MT", 12, BOLD))
labelSelectEmpresa.place(relx=0.5, rely=0.4, anchor=CENTER)

selector = ttk.Combobox(frame)
selector.place(relx=0.5, rely=0.45, anchor=CENTER)
selector['values'] = ('empresa1', 'empresa2', 'empresa3', 'empresa4')
selector.current(0)

#boton exportar desde la database la info solicitada
botonExportar = Button(frame, text="Exportar datos", command=consulta)
botonExportar.place(relx=0.5, rely=0.65, anchor=CENTER)
botonExportar.config(bg="#40db93", width=20, cursor="hand2")

#boton conectar a base de datos
botonConectar = Button(frame, text="Conectar a base de datos", command=conexionBD)
botonConectar.place(relx=0.5, rely=0.76, anchor=CENTER)
botonConectar.config(bg="#5089eb", width=20, cursor="hand2")





'''def mostrarFecha():
    date = fechaInicio.get_date()
    conversion = date.strftime("%d-%m-%Y")    
    resultado.config(text=conversion)


botonEjemplo = Button(frame, text="enviar", command=mostrarFecha)
botonEjemplo.place(x=100, y=150)

resultado = Label(frame, text="")
resultado.place(x=100, y=200) '''

root.mainloop()