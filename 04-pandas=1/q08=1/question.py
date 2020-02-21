##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c1 y una lista
##  separada por ':' de los valores de la columna _c2
##  para el archivo `tbl0.tsv`.
##
##  Rta/
##    _c0                        lista
##  0   A              1:1:2:3:6:7:8:9
##  1   B                1:3:4:5:6:8:9
##  2   C                    0:5:6:7:9
##  3   D                  1:2:3:5:5:7
##  4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
data =  pd.read_csv(
    "tbl0.tsv",
    sep = '\t',        
    thousands = None, 
    decimal = '.')
data = data[['_c1','_c2']]
data = data.groupby('_c1',as_index = False).agg(lambda x: x.sort_values().tolist())
data['_c2'] = data['_c2'].astype(str)
data['_c2'] = data['_c2'].str.replace(", ",":")
data['_c2'] = data['_c2'].str.replace("[","")
data['_c2'] = data['_c2'].str.replace("]","")
data.rename(columns=lambda x: x.replace('_c1', '_c0'), inplace=True)
data.rename(columns=lambda x: x.replace('_c2', 'lista'), inplace=True)
print(data)