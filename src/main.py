# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.
# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV

#Importing the neccesary librarys 
import os
from humanize import naturalsize
import time
import pandas as pd

#Iterating on the location of the files:
for root, dirs, files in os.walk('/workspaces/JLL_exercise-terminal-challenge'):
   for file in files:
#Extracting the data: name, size and modification date:
        file_path = os.path.join(root, file) 
        file_size = os.stat(file_path).st_size
        file_date = os.path.getmtime(file_path)
#Cleaning the data for visualization:
        file_path = os.path.basename(file_path)
        file_size = naturalsize(file_size)
        file_date = time.ctime(file_date)

#Creating table from data with pandas:
        table = [[file_path,file_size,file_date]]
        table_df = pd.DataFrame(table)
        table_df.columns = "File", "Size", "Modification Date"
        print(table_df)



    

