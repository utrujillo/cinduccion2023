# pip install pandas openpyxl
import pandas as pd

data = {
  'edad': [10,9,13,14,12,11,12],
  'cm': [115,110,130,155,125,120,125],
  'pais':['co','mx','co','mx','mx','ch','ch'],
  'genero':['M','F','F','M','M','M','F'],
  'Q1':[5,10,8,8,7,8,3],
  'Q2':[7,9,9,8,8,8,9]
}
dataframe = pd.DataFrame( data )
print(dataframe)

# Asignando indices
dataframe = pd.DataFrame( data, index=['Ana', 'Benito', 'Camilo', 'Daniel', 'Erika', 'Fabian', 'Gabriela'] )
print( dataframe )

# Obteniendo indices
print( dataframe.index )

# Obteniendo columnas
print( dataframe.columns )

# Obteniendo valores
print( dataframe.values )

# Obteniendo una columna especifica
print( dataframe['edad'] )

# Obteniendo multiples columnas
print( dataframe[['edad','cm','Q1']] )

# Buscando un solo indice
print( dataframe.loc[ 'Erika' ] )

# Encontrar un valor especifico
print('Valor especifico')
print( dataframe.loc['Daniel']['Q1'] )

# Buscando una indice especifico con datos especificos
print('Busqueda por indice especifico y persona especifica')
print( dataframe.loc[ 'Ana', ['edad', 'cm', 'Q1'] ] )

# Buscando multiples indices con multiples datos
print( dataframe.loc[['Ana', 'Erika'], ['edad','cm','Q1']] )

# Mostrar indice y extrayenbdo campos especificos
print( dataframe.loc[:,['edad','Q1']] )

# Filtrando por condiciones
print('Filtrando por condiciones')
print( dataframe['edad'] >= 12 )

# Mostrando elementos mediante un filtro
print("Filtrando datos por condiciones")
print( dataframe[dataframe['edad'] >= 12] )

# Filtrando multiples condiciones
print( dataframe[(dataframe['edad'] >= 12) & (dataframe['pais'] == 'mx')] )

# Filtrando por condiciones utilizando query
print( dataframe.query('edad >= 12') )

# Filtrando multiples condiciones utilznado query
print( "Filtrado multiple con query" )
print( dataframe.query('edad >= 12 & pais == "mx"') )