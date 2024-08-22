import pandas as pd
from pandas import ExcelWriter
import numpy as np 
import xlsxwriter
from xlsxwriter.workbook import Workbook


data = {'Matricula': {},  
        
      'USP': {},  
                
        'Name': {0: 'Ram', 1: 'Deep',  
               2: 'Yash', 3: 'Aman',  
               4:'' , 5: 'Aditya',  
               6: 'Divya', 7: 'Chalsea',  
               8: 'Akash' },
                  
        'Comentario': { },


      'Grupo': {0: 'B', 1: 'A', 2: 'F', 3: 'C',  
                4: 'E', 5: 'C', 6: 'A', 7: 'B',  
                8: 'B'},  

        
      'Dias': {}, 

        
      'Telefono': {}   
    }  

#data =(list(zip(List01, List02, List03, List04, List05)))

df = pd.DataFrame(data)

workbook = xlsxwriter.Workbook('./DEUBAJSEM34.xlsx')
worksheet = workbook.add_worksheet() 

worksheet.autofit()

workbook.close()
#workbook = xlsxwriter.Workbook('./DEUBAJSEM34.xlsx')
#worksheet = workbook.add_worksheet() 
#worksheet.set_column(1, 3, 50)
df.to_excel('./DEUBAJSEM34.xlsx')