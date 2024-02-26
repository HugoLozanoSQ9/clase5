#Lista de nombre de coders y una lista de edades
koders = [
    "Luis",
    "Benjamin",
    "Juan",
    "Irving",
    "Miren",
    "Miguel",
    "Enrique",
    "Francisco",
    "Rodrigo",
    "Francisco2",
    "Jose",
    "Jesus",
]

edades = [25,24,32,52,25,18,20,39,26,36,27,49]

#Metodo zip (es análogo a un cierre)

lista= tuple(zip(koders,edades))


print('Hola koders la lista completa es:')
for x,y in lista:
    print(f'{x} - {y}')