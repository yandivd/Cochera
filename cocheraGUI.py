from tkinter import *
import pickle

class Auto():
    def __init__(self,marca,modelo,color,numChapa,velMax):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.numChapa=numChapa
        self.velMax=velMax

    def __str__(self):
        return "{} {} {} {} {}".format(self.marca, self.modelo, self.color, self.numChapa, self.velMax)

class Cochera():
    listaAutos=[]

    def __init__(self):
        archivo=open("archivoAutos","ab+")
        archivo.seek(0)
        try:
            self.listaAutos=pickle.load(archivo)
            print("Se cargaron {} autos".format(len(self.listaAutos)))
        except:
            print("Archivo Vacio")
        finally:
            archivo.close()
            del(archivo)
    
    def MostrarAutos(self):
        a=1
        for i in self.listaAutos:
            print("| ",a, i)
            a+=1        
    
    def AgregarAuto(self,auto):
        self.listaAutos.append(auto)
        self.AgregarAutoAlFichero()

    def AgregarAutoAlFichero(self):
        archivo=open("archivoAutos","wb")
        pickle.dump(self.listaAutos, archivo)
        archivo.close()
        del(archivo)

    def Vaciar(self):
        listaVacia=[]
        archivo=open("archivoAutos","wb")
        pickle.dump(listaVacia, archivo)
        archivo.close()
        del(archivo)
        archivo=open("archivoAutos","rb")
        self.listaAutos=pickle.load(archivo)
        archivo.close()
        del(archivo)

    def EliminarCoche(self,indice):
        archivo=open("fileAutos","wb")
        autoEliminado=self.listaAutos[indice]
        self.listaAutos.pop(indice)
        pickle.dump(self.listaAutos, archivo)
        print("Auto ",autoEliminado.numChapa," eliminado")
        archivo.close()
        del(archivo)


#######Ejecucion###############
miGarage=Cochera()
auto1=Auto("Ferrar", "XRG", "rojo", "LIB029", "120")
miGarage.AgregarAuto(auto1)

#######interfaz grafica#####################
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

botonMostrar=Button(miFrame, text="Mostrar Autos", width=12, height=2, command=miGarage.MostrarAutos)
botonMostrar.grid(row=2, column=0, pady=5)

botonAdd=Button(miFrame, text="Agregar Auto", width=12, height=2)
botonAdd.grid(row=3, column=0, pady=5)

botonDel=Button(miFrame, text="Eliminar Auto", width=12, height=2)
botonDel.grid(row=4, column=0, pady=5)

botonClean=Button(miFrame, text="Limpiar Datos", width=12, height=2)
botonClean.grid(row=5, column=0, pady=5)

botonExit=Button(miFrame, text="Salir",width=12, height=2)
botonExit.grid(row=6, column=0, pady=5)

#Label que deberia mostrar la informacion de los autos
listaDeLabel=StringVar()
labelListado=Label(miFrame, height=12, width=30, textvar=listaDeLabel)
labelListado.grid(row=2, column=1,rowspan=4)
labelListado.config(background="white")

raiz.mainloop()