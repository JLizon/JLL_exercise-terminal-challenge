# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.
# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV

import os
 
ficheros = os.walk('/workspaces/JLL_exercise-terminal-challenge')
print(len(list(ficheros)))