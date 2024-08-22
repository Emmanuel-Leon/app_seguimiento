from tkinter import Tk, Label, Button, Entry, Frame, END 
import pandas as pd
from tkinter import messagebox


ventana = Tk()
ventana.config(bg='black')
ventana.geometry("260x400")
nombre1,telefono1= [],[]
ventana.resizable(0,0)
ventana.title('App Seguimiento:CETEC')



C=0
path='./BAJAS.xlsx'
df=pd.read_excel(path)
col = df['Nombre del profesor']
Col = len(col)
		

def agregar_datos():
	global nombre1, telefono1

	

	for i in range(Col):
		if(col[i]==nombre):
			alum=df.iloc[i,2]
			tel=df.iloc[i, 8]
			telefono = tel
	
			C=C+1

			nombre1.append(alum)

			ingresa_nombre.delete(0,END)
	


def guardar_datos():	
	global alum,telefono1
	datos = [{'Nombre Completo':alum, 'Telefono':telefono1}] 
	nom_excel  = str(nombre_archivo.get() + ".xlsx")	
	df = pd.DataFrame(datos,columns =  ['Nombre Completo', 'Telefono']) 
	df.to_excel(nom_excel)
	nombre_archivo.delete(0,END)

frame1 = Frame(ventana, bg='gray')
frame1.grid(column=0, row=0)
frame2 = Frame(ventana, bg='gray')
frame2.grid(column=1, row=0, sticky='nsew')


nombre = Label(frame1, text ='Escribe el nombre \n del profesor', width=18, height=2).grid(column=0, row=0, pady=20, padx= 10)
ingresa_nombre = Entry(frame1,  width=25, font = ('Arial',12))
ingresa_nombre.grid(column=0, row=2)


agregar = Button(frame1, width=10, font = ('Arial',12, 'bold'), text='Aceptar', bg='green4',bd=5, command =agregar_datos)
agregar.grid(column=0, row=3, pady=20, padx= 10)

archivo = Label(frame1, text ='Ingrese Nombre del archivo', width=25, bg='gray16',font = ('Arial',12, 'bold'), fg='white')
archivo.grid(column=0, row=4, pady=10, padx= 10)

nombre_archivo = Entry(frame1, width=19, font = ('Arial',12),highlightbackground = "blue", highlightthickness=4)
nombre_archivo.grid(column=0, row=5, pady=1, padx= 10)

guardar = Button(frame1, width=10, font = ('Arial',12, 'bold'), text='Guardar', bg='red',bd=5, command =guardar_datos)
guardar.grid(column=0, row=6, pady=20, padx= 10)


#messagebox.showinfo(message="La cantidad de alumnos del profesor es: \n ", title="MENSAJE URGENTE")

ventana.mainloop()