##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c4
##  del archivo `tbl1.tsv`.
##
##  Rta/
##      _c0    lista
##  0     0    b,f,g
##  1     1    a,c,f
##  ...
##  38   38      d,e
##  39   39    a,d,f
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
data1 =  pd.read_csv(
    "tbl1.tsv",
    sep = '\t',         
    thousands = None, 
    decimal = '.')
data1 = data1[['_c0','_c4']]
data1 = data1.groupby('_c0',as_index = False).agg(lambda x: x.sort_values().tolist())
data1['_c4'] = data1['_c4'].astype(str)
data1['_c4'] = data1['_c4'].str.replace(", ",",")
data1['_c4'] = data1['_c4'].str.replace("'","")
data1['_c4'] = data1['_c4'].str.replace("[","")
data1['_c4'] = data1['_c4'].str.replace("]","")
data1.rename(columns=lambda x: x.replace('_c4', 'lista'), inplace=True)
print(data1)