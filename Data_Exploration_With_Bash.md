### EXPRESIONES REGULARES 

#### Fechas

([0-2]\d|3[0,1])\/(0\d|1[0,1,2])\/(20[0-2]\d)  ------> 09/03/2019

(20[0-2]\d)\-(0\d|1[0,1,2])\-([0-2]\d|3[0,1]) ------> 2019/12/24

^(20[0-2]\d)\-(0\d|1[0,1,2])\-([0-2]\d|3[0,1]) \d{2}\:\d{2}\:\d{2}\.\d{6}   -----> 2019-12-24 23:45:34.675434

**********************************************************
### COMANDO AWK
Imprimir las primeras 10 lineas de un archivo
```
awk 'NR < 11' archivo.csv
```
El comando awk se usa para separar columnas. Usas 
```
awk '{print $1}' FS="|" archivo.txt 
```
Para imprimir la primera columna dentro de un archivo separado por pipes. 
Si además quieres ver el número de fila en el que está o la longitud escribes NR y length adentro del print.
Quedaría 
```
awk '{print NR, $1, length}' FS="|" archivo.Txt
```
Eso además le puedes aplicar un grep para que del resultado que te dio te lance las filas que sigan cierto patrón. Con ver si tienen letras. Esos es grep [Aa-Zz]
Si quieres buscar todos los que NO cumplen con el patrón pones un -v
Entonces todo junto es 
```
awk '{print NR, $3}' FS="|" archivo.txt | grep -P [aA-zZ]
```
Esto te muestra todas las filas de la Columna 3 que tienen letras.

### Comandos

#### Para solo números
```
awk '{print NR, $3}' FS="|" archivo.txt | grep [0-9]
```
#### Para solo decimales
```
awk '{print NR, $3}' FS="|" archivo.txt | grep -Eo "[0-9]+\.[0-9]+"
```
#### Para solo 4 caracteres
```
awk '{print $2}' FS="," archivo.csv | grep -P '[A-Za-z]{4}' -v
```
#### Para vacios
```
 awk '{print $6}' FS="," archivo.csv | grep "" -v
```
#### Para numericos donde viene letras
```
awk '{print $7}' FS="," archivo.csv | grep -P '[A-Za-z]' -v
```
#### Para numericos NO vienen 1 o 3 numeros
```
awk '{print $8}' FS="," archivo.csv | grep -P '[0-9]{0,3}' -v
```
#### Para fechas que no cumplen la forma dMMyyyy
```
awk '{print $2}' FS=";" *.csv | grep -P '(\d|[1-2]\d|3[0,1])(0\d|1[0,1,2])(20[0-2]\d)' -v
```
#### Para campos que tengan alfanumericos
```
 awk '{print $10}' FS="," archivo.csv | grep -P '[A-Za-z0-9]' -v
```
#### Para campos que tengan mas de 500 alfanumericos
```
awk '{print $11}' FS="," archivo.csv | grep -P '[A-Za-z0-9]{0,500}' -v
```
#### Longitud 0 o diferente de 0
```
awk '{print $5}' FS='|' archivo.csv | awk '{print NR, length}'| grep '0' -w -v
```
#### Cuando viene el problema de muchos formatos de fechas y campos nulos

1. Buscar por Git Bash que campos son nulos: ```awk '{print NR, $5}' FS="," seguros.csv | grep [aA-zZ] -v```
2. Quitarlos manualmente.
3. Ir al excel añadir una fila al inion y pasarle un fitro para ver que columnas son de diferentes formato

