##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 por cada letra 
##  de la primera columna, ordneados alfabeticamente.
##
##  Rta/
##  A,37
##  B,36
##  C,27
##  D,23
##  E,67
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
  suma = 0
  for r in Archivo2:
    if i[0] == r[0]:
      suma = suma + int(r[1])
  print(i[0]+","+str(suma))
