##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la suma de la segunda columna del archivo `data.csv`.
##
##  Rta/
##  190
##
##  >>> Escriba su codigo a partir de este punto <<<
## 
Archivo= open ("data.csv","r")
Archivo2=[y.strip() for y in Archivo]
Archivo2=[z.replace('\t', '') for z in Archivo2]
suma=0
for i in Archivo2[0:]:
  suma=suma + int(i[1])
print(suma)