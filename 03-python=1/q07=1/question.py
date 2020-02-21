##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, genera una lista de tuplas que asocien las 
##  columnas 0 y 1. Cada tupla contiene un valor posible de la columna 2 y una
##  lista con todas las letras asociadas (columna 1) a dicho valor de la 
##  columna 2.
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##  ('2', ['A', 'E', 'D'])
##  ('3', ['A', 'B', 'D', 'E', 'E'])
##  ('4', ['E', 'B'])
##  ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##  ('6', ['C', 'E', 'A', 'B'])
##  ('7', ['A', 'C', 'E', 'D'])
##  ('8', ['E', 'E', 'A', 'B'])
##  ('9', ['A', 'B', 'E', 'C'])
##
##  >>> Escriba su codigo a partir de este punto <<<
##
Archivo= open ("data.csv","r")
Archivo2=[y.strip() for y in Archivo]
Archivo2=[r.split('\t') for r in Archivo2]
ValU1=[]
for i in Archivo2:
  encontrado=0
  for r in ValU1:
    if r==i[1]:
      encontrado=1
  if encontrado==0:
    ValU1.append(i[1])
for i in sorted(ValU1):
  Letras=[]
  for r in Archivo2:
    if i==r[1]:
      Letras.append(r[0])
  print((i,Letras))
