# Lista de nombre de coders y una lista de edades
#Versión correcta madafakers
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

edades = [25, 24, 32, 52, 25, 18, 20, 39, 26, 36, 27, 49]

lista = []

for i in range(len(edades)):
    lista.append((koders[i], edades[i]))

print('Hola koders la lista completa es:')
for x,y in lista:
    print(f'{x} - {y}')

""" 

El profe hizo:

message = 'Hola koders \n La lista completa es: \n'

for pair in koder_ages : (koder ages en este momento sería nuestra lista llamada lista)
    message += f'{pair[0} - {pair[1]} \n

"""
