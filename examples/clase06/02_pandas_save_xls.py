import pandas as pd
import os.path

data = {
    'edad': [1000,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,8,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}

# Creando informacion en el dataframe
dataframe = pd.DataFrame( data )

# Estableciendo el path donde sera encontrado el archivo
PATH = '/apps/examples/clase06/{}'
# Guardando datos en el archivo de excel
dataframe.to_excel( PATH.format('data.xlsx') )