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

## f strings
Al agregarle una f al inicio de una cadena, se puede hacer referencia a realizar un casteo de las variables numericas incluidas en el string completo. 

En pocas palabras sirven para mantener variables y string en conjunto 

## Métodos de string 

capitalize () --> Convierte el primer caracter en mayuscula  variable.capitalize() 

casefold() --> convierte todos los caracteres en minúsculas. es más agresivo que lower(), se dice esto por que casfold sirve para cualquier tipo de alfabeto. (se ocupan más en traducciones)

center() --> Devuelve un string centrado (sirve para los mensajes impresos en terminal)

count() --> Devuelve el número de veces que aparece un caracter en la cadena 

encode() --> Regresa una versión codificada de la cadena (Por defecto la estandart es la UTF-8) (Se suele ocupar cuando se consultan datos en bases de datos que fueron guardadas en una codificación diferente al estándart, en caso de que no se recupere de forma correcta el mensaje estará mal escrito) Puede tener un argumento llamado encoding=decorificador 
.encode(encoding='ascii')

endswith() --> Se le puede preguntar si una cadena termina con ciertos caracteres y devolverá un true o false

expandtabs() --> Nos va apermitir especificar el tamaño de los tabuladores (por defecto llevan 8 espacios pero los puedo hacer que tengan más) recibe como argumento un número entero 

find() -->  Me va a permitir buscar en el string un valor especificado, es similar al método index() dado que me va a devolver la posición en la que se ubica ese strign

## Is --> type

isnumeric() --> Nos permite hacer ciertas validaciones con el usuario al momento de solicitarle un dato, por decir si su dato es un string y se solicitaba un dato numerico se puede indicar que es un mensaje invalido  (No considera números negativos ni decimales estos datos arrojarían falso)

isalunum() --> verdadero si todos los caracteres son alfanumericos ocease del 0-9 A-z 

isalpha() --> verdadero si todos los caracteres son alfabéticos  A-z

isascii() -->Verdadero si todos los caracteres son caracteres ascii

isdecimal() --> Verdadero si todos los caracteres son decimales (verdadero con un 2.5) 

isdigit() --> Verdadero si todos los caracteres son digitos (Falso con un 2.5 por que el . no es un digito ) evalua que todos los caracteres del string sea númerico

islower() --> Verdadero si todos los caracteres son minuscula

isupper() --> Verdadero si todos los caracteres son mayusculas

isnumeric() --> Verdadero si todos los caracteres son numericos

isprintable() --> Verdadero si todos los caracteres se pueden imprimir (cualquier caracter que se pueda ver en una hoja de papel) recordemos que un espacio si es imprimible (verdadero), pero tabuladores y saltos de lina retornarán un falso, suele ser util cuando se leen archivos en excel, se suele hacer un recorrido de los las casillas que tienen elementos imprimibles para que solamente los que son verdaderos se almacenen en la base de datos o lo que se solicite 

isspace() --> Verdadero si todos los caracteres son espacios en blanco 

istilde() --> Verdadero si todos los caracteres siguen la regla de títulos (que la primera letra sea mayuscula) *(Titulo)

## Método join()

join() se comienza con un string vacío print(' '.join(iterable)) el iteralble puede ser lista, tupla etc... y me va a devolver un string con todos los elementos concatenados, se le puede especificar un separador por decir una coma

