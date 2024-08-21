from tkinter import Tk, Label, Button, Entry, Frame, END 
import pandas as pd
from tkinter import messagebox


ventana = Tk()
ventana.config(bg='black')
ventana.geometry("390x400")
nombre1,dx1,oi1,od1,dt1 = [],[],[],[],[]
ventana.resizable(0,0)
ventana.title('App Seguimiento:CETEC')


C=0
path='./BAJAS.xlsx'
df=pd.read_excel(path)
col = df['Nombre del profesor']


frame1 = Frame(ventana, bg='gray15')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='gray16')
frame2.grid(column=1, row=0, sticky='nsew')



nombre = Label(frame1, text ='Nombre \n del profesor', width=15, height=2).grid(column=0, row=0, pady=20, padx= 10)
ingresa_nombre = Entry(frame1,  width=28, font = ('Arial',12))
ingresa_nombre.grid(column=1, row=0)


Col = len(col)


for i in range(Col):
	if(col[i]==nombre):
		alum=df.iloc[i,2]
		tel=df.iloc[i, 8]

		C=C+1	


def agregar_datos():
	global nombre1, dx1, oi1, od1, dt1

	nombre1.append(ingresa_nombre.get())
	#dx1.append(ingresa_dx.get())
	#oi1.append(ingresa_oi.get())
	#od1.append(ingresa_od.get())
	#dt1.append(ingresa_dt.get())

	ingresa_nombre.delete(0,END)
	#ingresa_dx.delete(0,END)
	#ingresa_oi.delete(0,END)
	#ingresa_od.delete(0,END)
	#ingresa_dt.delete(0,END)

def guardar_datos():	
	global nombre1,dx1,oi1,od1,dt1
	datos = {'Nombre Completo':nombre1 } 
	nom_excel  = str(nombre_archivo.get() + ".xlsx")	
	df = pd.DataFrame(datos,columns =  ['Nombre Completo', 'Diagnostico', 'Ojo Izquierdo', 'Ojo Derecho', 'Fecha']) 
	df.to_excel(nom_excel)
	nombre_archivo.delete(0,END)


agregar = Button(frame1, width=20, font = ('Arial',12, 'bold'), text='Aceptar', bg='green4',bd=5, command =agregar_datos)
agregar.grid(columns=2, row=5, pady=20, padx= 10)

archivo = Label(frame2, text ='Ingrese Nombre del archivo', width=25, bg='gray16',font = ('Arial',12, 'bold'), fg='white')
archivo.grid(column=0, row=0, pady=10, padx= 10)


nombre_archivo = Entry(frame2, width=23, font = ('Arial',12),highlightbackground = "blue", highlightthickness=4)
nombre_archivo.grid(column=0, row=1, pady=1, padx= 10)

guardar = Button(frame2, width=20, font = ('Arial',12, 'bold'), text='Guardar', bg='red',bd=5, command =guardar_datos)
guardar.grid(column=0, row=2, pady=20, padx= 10)


messagebox.showinfo(message="La cantidad de alumnos del profesor es: \n ", title="MENSAJE URGENTE")


ventana.mainloop()