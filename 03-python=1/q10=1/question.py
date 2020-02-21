##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima una tabla en formato CSV que contenga 
##  por registro, la letra de la columna 1 y la cantidad de elementos de las 
##  columnas 4 y 5. 
## 
##  Rta/
##  E,3,5
##  A,3,4
##  B,4,4
##  ...
##  C,4,3
##  E,2,3
##  E,3,3
##
##  >>> Escriba su codigo a partir de este punto <<<
##
Archivo= open ("data.csv","r")
Archivo2=[y.strip() for y in Archivo]
Archivo2=[r.split('\t') for r in Archivo2]
Col=[[c[0],c[3],c[4]] for c in Archivo2]
for x in Col: 
  print(x[0]+','+str(len(x[1].split(',')))+','+str(len(x[2].split(','))))

