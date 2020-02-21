##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv, imprima una tabla en formato CSV que contenga 
##  la cantidad de registros en que aparece cada clave de la columna 5.
##
##  Rta/
##  aaa,13
##  bbb,16
##  ccc,23
##  ddd,23
##  eee,15
##  fff,20
##  ggg,13
##  hhh,16
##  iii,18
##  jjj,18
##
##  >>> Escriba su codigo a partir de este punto <<<
##

Archivo= open ("data.csv","r")
Archivo2=[y.strip() for y in Archivo]
Archivo2=[r.split('\t') for r in Archivo2]
Col=[row[4].split(',') for row in Archivo2]
Col2=[r[:3] for x in Col for r in x ]
for i in sorted(set(Col2)):
  print(i+','+str(Col2.count(i)))


