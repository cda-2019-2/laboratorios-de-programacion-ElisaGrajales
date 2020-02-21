##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 para cada 
##  letra de la columna 4, ordnados alfabeticamente.
##
##  Rta/
##  a,114
##  b,40
##  c,91
##  d,65
##  e,79
##  f,110
##  g,35
##
##  >>> Escriba su codigo a partir de este punto <<<
##
Archivo= open ("data.csv","r")
Archivo2=[y.strip() for y in Archivo]
Archivo2=[r.split('\t') for r in Archivo2]
Col=[[c[1],c[3].split(',')] for c in Archivo2]
suma={}
for fila in Col:
  for num in fila[1]:
    if num not in suma.keys():
         suma[num] = [int(fila[0])] 
    else:
         suma[num].append(int(fila[0]))
for x in sorted(suma.keys()):
  print(x+","+str(sum(suma[x])))