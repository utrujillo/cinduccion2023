import pandas as pd
import os.path

# Estableciendo el path donde sera encontrado el archivo
PATH = '/apps/examples/clase06/{}'

# Verificamos si existe el archivo
if( os.path.isfile( PATH.format('data.xlsx') ) ):
    print('Leyendo datos desde el dataframe')
    # Leyendo informacion del archivo de excel e insertando los datos en dataframes
    data_from_xls = pd.read_excel( PATH.format('data.xlsx'),  index_col=0 )
    print( data_from_xls )
else:
    print('No existe el archivo')