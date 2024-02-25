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

koder = [k for k in koders]
edad = [e for e in edades]

koders_edades=(koder,edad)
print(koders_edades)

#nombres = ', '.join(koders_edades)

#print(f'Hola koders la lista completa es: {nombres}')

"""
Hola Koders. La lista completa es: 
Luis - 25
Benajmin -32
Enrique - 25

"""