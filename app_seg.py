import pandas as pd
import webbrowser as web
import pyautogui as pg
import time
C=0

path='./BAJAS.xlsx'

df=pd.read_excel(path)

col = df['Nombre del profesor']
Col = len(col)
for i in range(Col):
	if(col[i]=='JESUS EMMANUEL DOMINGUEZ'):
		alum=df.iloc[i,2]
		tel=df.iloc[i,9]
		C=C+1
	

		print (alum)
		print (tel)
print(C)
