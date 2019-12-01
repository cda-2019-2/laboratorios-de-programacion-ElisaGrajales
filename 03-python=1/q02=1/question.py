##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la cantidad de registros por letra para la primera columna del 
##  archivo `data.csv`, ordenados alfabeticamente por la letra.
##
##  Rta/
##  A,8
##  B,7
##  C,5
##  D,6
##  E,14
##
##  >>> Escriba su codigo a partir de este punto <<<
## 

Archivo= open ("data.csv","r")
Archivo2=[y.strip() for y in Archivo]
Archivo2=[r.split('\t') for r in Archivo2]
Col1=[]
Col2=[]
for i in Archivo2:
  encontrado=0
  for r in Col1:
    if r==i[0]:
      encontrado=1
  if encontrado==0:
    Col1.append(i[0])
    Col2.append(i[0] +",0")
for i in sorted(Col2):
  ocurr = 0
  for r in Archivo2:
    if i[0] == r[0]:
      ocurr = ocurr + 1
  print(i[0]+","+str(ocurr))

