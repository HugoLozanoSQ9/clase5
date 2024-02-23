message = "Hello world, Hola mundo, Bye wolrd, Adios world, Otro texto, Otro mensjaje "
modified_msg = [msg.strip() for msg in message.split(',') ]
#Se estaría ocupando la ',' como separador se puede poner un espacio para contemplar
#El espacio que se pone por defecto al momento de escribir

#print(modified_msg,'Usando el método .split') #Va a guardar todo el texto despues de la ',' incluyendo los espacios
#print(message )

x=0

for i in modified_msg:
    x += 1
    print(i,'Elemento en posición',x)


