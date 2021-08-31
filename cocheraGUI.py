from tkinter import *
from cochera import *
raiz=Tk()
raiz.geometry("600x450")
raiz.title("GaragApp")

miFrame=Frame(raiz,width="600", height="450")
miFrame.pack()

labelPresentacion=Label(miFrame,text="Garagcom", fg="red", font=("Comics Sans MS",20))
labelPresentacion.grid(row=0, column=0, pady=20, columnspan=3)
labelComentario=Label(miFrame,text="Este software gestiona todos los vehiculos que se guardan en un \ndeterminado garage")
labelComentario.grid(row=1, column=0, padx=5, columnspan=3)
labelComentario.config(justify="center")

botonMostrar=Button(miFrame, text="Mostrar Autos", width=12, height=2, command=miCuchera.MostrarAutos)
botonMostrar.grid(row=2, column=0, pady=5)

botonAdd=Button(miFrame, text="Agregar Auto", width=12, height=2)
botonAdd.grid(row=3, column=0, pady=5)

botonDel=Button(miFrame, text="Eliminar Auto", width=12, height=2)
botonDel.grid(row=4, column=0, pady=5)

botonClean=Button(miFrame, text="Limpiar Datos", width=12, height=2)
botonClean.grid(row=5, column=0, pady=5)

botonExit=Button(miFrame, text="Salir",width=12, height=2)
botonExit.grid(row=6, column=0, pady=5)

labelListado=Label(miFrame, height=12, width=30)
labelListado.grid(row=2, column=1,rowspan=4)
labelListado.config(background="white")

raiz.mainloop()