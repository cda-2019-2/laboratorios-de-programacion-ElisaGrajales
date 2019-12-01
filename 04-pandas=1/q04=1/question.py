##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima una lista con los valores unicos de la columna _c4 de 
##  del archivo `tbl1.csv` en mayusculas.
## 
##  Rta/
##  ['A', 'B', 'C', 'D', 'E', 'F', 'G']
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
datos=pd.read_csv(
    "sample_data/tbl1.tsv",
    sep = '\t',
    thousands = None,  
    decimal = '.')     
datos1=datos.sort_values('_c4',ascending=True)
datos2=pd.unique(datos1['_c4'].str.upper())
print(datos2.tolist())

