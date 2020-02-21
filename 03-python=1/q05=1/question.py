##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima el valor maximo y minimo de la columna
##  2 por cada letra de la columa 1.
##
##  Rta/
##  A,9,1
##  B,9,1
##  C,9,0
##  D,7,1
##  E,9,1
##
##  >>> Escriba su codigo a partir de este punto <<<
##
Archivo= open ("data.csv","r")
Archivo2=[y.strip() for y in Archivo]
Archivo2=[r.split('\t') for r in Archivo2]
LetU1=[]
for i in Archivo2:
  encontrado=0
  for r in LetU1:
    if r==i[0]:
      encontrado=1
  if encontrado==0:
    LetU1.append(i[0])
for i in sorted(LetU1):
  Numeros=[]
  for r in Archivo2:
    if i==r[0]:
      Numeros.append(r[1])
  print(i+","+(max(Numeros))+","+(min(Numeros)))
