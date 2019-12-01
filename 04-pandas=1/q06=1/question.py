##
##  Programación con Pandas
##  ===========================================================================
##
##  Agregue una columna con la suma de _c0 y     al archivo `tbl0.tsv`. 
##
##  Rta/
##      _c0 _c1  _c2         _c3  suma
##  0     0   E    1  1999-02-28     1
##  1     1   A    2  1999-10-28     3
##  ...
##  38   38   E    1  1999-09-28    39
##  39   39   E    5  1998-01-26    44
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)
data3=pd.read_csv(
    "tbl0.tsv",
    sep = '\t',
    thousands = None,  
    decimal = '.')     
data3['suma']=data3['_c0']+data3['_c2']
print(data3)