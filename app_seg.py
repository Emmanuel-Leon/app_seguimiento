import pywhatkit
import pandas as pd
C=0

path='./BAJAS.xlsx'

df=pd.read_excel(path)

col = df['Nombre del profesor']
Col = len(col)
for i in range(Col):
	if(col[i]=='JESUS EMMANUEL DOMINGUEZ'):
		alum=df.iloc[i,2]
		#tel=df.iloc[i,8]
		tel='2291204090'
		C=C+1
		pywhatkit.sendwhatmsg(tel, "Test",2,10)

		print (alum)
		print (tel)

