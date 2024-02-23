# Strings Manipualción y formato 

## Declaración 

La cadena de caracteres será delimitada por un par de comillas dobles o comillas simples '  ' "  "

## Cadenas multilinea 
 
Con el siguiente formato (3 comillas dobles) se respeta la integridad del texto escrito 

message = """ Hello world 
¿Cómo están? """

## String slicing

Las cadenas de texto también pueden ser consideradas como iterables, lo que nos da acceso a utilizar la notación de slices como en las listas 

Se puede ocupar parte de los caracteres de un string con el silicing 
var[inicio : final] 

-Cabe destacar que ambién comienzan en 0 (como las listas)
-También es inlcuyente y excluyente por decir [ 3:10 ] el resultado real serán todos los caracteres de la posición 3 a la 9
-Se puede hacer como el slicing general 
    var[:5] (Desde el inicio al 4)
    var[6:] Hasta el final desde el 6 al ultimo 
    var[-6:-3] Indexado negativo 
    
## Transformación a máyusculas .upper() permite transformar todos los caracteres de la cadena original a minúsculas

Se puede anexar a cadenas como: print('Hola'.upper())
NO modifica la lista original 
## Transformación a minúsculas .lower()

Se puede anexar a cadenas como: print('Hola'.lower())
NO modifica la lista original 

## Eliminar whitespace .strip()
Se utiliza para referirse a los espacios que pueden existir antes y despues de la cadena de texto útil 
se eliminan con el método .strip()

## Reemplazar cadenas de texto .replace()
Es posible reemplazar cadenas de texto, dentro de otras cadenas de texto con el método .replace()

## Separar cadenas de texto
El método .split() permite separar cadenas de texto, mediante un delimintador, devolviendo una lista de elementos con las cadenas resultantes

## Concatenación  + 

Se refiere a combinar 2 o más cadenas de texto, para esto se ocupa el operador + 
Solo se puede concatenar cadenas de texto con cadenas de texto

## Formato de texto con .format()

Es posible combinar strings con otros tipos de dato, por medio del método .format()

Todos los argumanetos que reciba este método, son formateados y reemplazarán caracteres {} dentro de la cadena de texto

3 formas de funcionar 

-Por orden indexado (en el .format(10,12,15)) se mete la info (dejando {} vacío)
-Por control de argumentos en el {n} donde n es el indice de la lista
-Por 'variables' .format(num=10, num2=20) {num} {num2}
