##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c5a
##  y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
##  Rta/
##      _c0                                lista
##  0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
##  1     1              aaa:3,ccc:2,ddd:0,hhh:9
##  ...
##  38   38                    eee:0,fff:9,iii:2
##  39   39                    ggg:3,hhh:8,jjj:5
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
data1 =  pd.read_csv(
    "sample_data/tbl2.tsv",
    sep = '\t',        
    thousands = None, 
    decimal = '.')
data1['_c5'] = data1['_c5a'] + ':' + data1['_c5b'].apply(str)
data1 = data1.groupby('_c0',as_index = False)['_c5'].agg(lambda x: x.sort_values().tolist())
data1['_c5'] = data1['_c5'].astype(str)
data1['_c5'] = data1['_c5'].str.replace("'","")
data1['_c5'] = data1['_c5'].str.replace(" ","")
data1['_c5'] = data1['_c5'].str.replace("[","")
data1['_c5'] = data1['_c5'].str.replace("]","")
data1.rename(columns=lambda x: x.replace('_c5', 'lista'), inplace=True)
print(data1)
