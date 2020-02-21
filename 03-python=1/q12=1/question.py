##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima por cada fila, la columna 1 y la suma 
##  de los valores de la columna 5.
##
##  Rta/
##  E,22
##  A,14
##  B,14
##  ....
##  C,8
##  E,11
##  E,16
##
##  >>> Escriba su codigo a partir de este punto <<<
##

import re
Archivo= open ("data.csv","r")
Archivo2=[y.strip() for y in Archivo]
Archivo2=[r.split('\t') for r in Archivo2]
col = [[c[0], c[4]] for c in Archivo2]
for i in col:
    num = re.findall('\d+', i[1])
    num = [int(x) for x in num]
    print(i[0]+','+str(sum(num)))

