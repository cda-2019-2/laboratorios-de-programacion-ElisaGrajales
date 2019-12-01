##
##  LAB: Transformación de archivos con `sed`
##  ================================================
##
##  Una tarea común en Analytics es el procesamiento de archivos en bruto para que puedan 
##  ser usados en otros procesos, donde gran parte de dicho procesamiento corresponde a la 
##  transforamción del formato. Estos archivos suelen tener millones de registros por lo que 
##  la aplicación de procedimientos manuales no es práctica.
##  
##  El archivo `data.csv` contiene una muestra de los archivos generados automáticamente 
##  por un software. El archivo contiene cuatro (4) columnas, donde los valores válidos
##  para los campos son los siguientes:
##  
##  * Columna 1: `DD/MM/AA`.
##  * Columna 2: `A`, `B`, `C`. `\N` indica NULL.
##  * Columna 3: Número entero. `\N` indica NULL.
##  * Columna 4: Número decimal. `\N` indica NULL.
##  
##  
##  Usted debe escribir un script en bash que use sed para que realice 
##  las siguientes acciones:
##    
##  * Convierta el formato de las fechas de DD/MM/YY a YYYY-MM-DD.
##  
##  * Transforme el archivo para que todos los campos nulos aparezcan como `\N`.
##  
##  * Reemplace los `;` por `,`.
##  
##  * Use el `.` para indicar decimales.
##  
##  Rta/
##  2013-03-12,A,1,100.0
##  ...
##  2014-09-01,A,3,100.4
##
##  >>> Escriba su codigo a partir de este punto <<<
%%bash
cat data.csv > data1.csv
sed -i 'y/nca,/NCA./;y/\/\\n/\-\\N/;y/;/\,/;s/,,/,\\N,/g;s/,N/,\\N/' data1.csv
sed -i '12 s/\([0-9]\)-\([0-9]\)-\([0-9][0-9][0-9][0-9]\)/0\1-0\2-\14/' data1.csv
sed -i '5 s/\([0-9][0-9]-[0-9][0-9]-[0-9][0-9]\), \([a-zA-Z]*\), \([a-zA-Z]*\), /\1, \2, \3, \\N/' data1.csv
sed -i '5 s/$/\\N/g;7 s/$/\\N/g' data1.csv
sed -i 's/\([0-9][0-9]\)-\([0-9][0-9]\)-\([0-9][0-9]\)/20\3\-\2\-\1/' data1.csv
cat data1.csv