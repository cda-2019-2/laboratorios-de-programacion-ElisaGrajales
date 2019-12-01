##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima la cantidad de registros por cada letra 
##  de la columna _c1 del archivo `data.tsv` usando pandas.
## 
##  Rta/
##  _c1
##  A     8
##  B     7
##  C     5
##  D     6
##  E    14
##  Name: _c0, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import numpy as np
data=pd.read_csv(
    "data.tsv",
    sep = '\t',
    thousands = None,  
    decimal = '.') 
count_data = (data.groupby(['_c1'])['_c0'].count())
print(count_data)