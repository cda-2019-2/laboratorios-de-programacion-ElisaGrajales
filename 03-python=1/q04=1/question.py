##
##  Programación en Python
##  ===========================================================================
##
##  La columna 3 del archivo `data.csv` contiene una fecha en formato 
##  `YYYY-MM-DD`. Imprima la cantidad de registros por cada mes separados
##  por comas, tal como se muestra a continuación.
##
##  Rta/
##  01,3
##  02,4
##  03,2
##  04,4
##  05,3
##  06,3
##  07,5
##  08,6
##  09,3
##  10,2
##  11,2
##  12,3
##
##  >>> Escriba su codigo a partir de este punto <<<
##
Archivo= open ("data.csv","r")
Archivo2=[y.strip() for y in Archivo]
Archivo2=[r.split('\t') for r in Archivo2]
Mes=[[row[2][5:7]] for row in Archivo2]
MesU1=[]
MesU2=[]
for i in Mes:
  encontrado=0
  for r in MesU1:
    if r==i[0]:
      encontrado=1
  if encontrado==0:
    MesU1.append(i[0])
    MesU2.append(i[0] +",0")
for i in sorted(MesU2):
  cont = 0
  for r in Mes:
    if i[0:2] == r[0]:
      cont = cont + 1
  print(i[0:2]+","+str(cont))
