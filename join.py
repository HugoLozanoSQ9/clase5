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

nombres =', '.join(koders) #Se separan los elementos de la lista con una , y un espacio pero convierte la lista a un string completo
#colocará el , y espacio a los elementos siempre y cuando no sea el ultimo 

message = f'Hola Koders. Los saludo por sus nombres: {nombres}'

print(message)

