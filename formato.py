message = "Hello {0} world, Estoy equivocado, somos {1}, {2}, lista random {3},tupla para probar{4}, set para sacar las dudas {5}" 
#el par de llaves sirve para concatenar str con números
print(message.format(12,10, 'saludos banda', [10.2,5,6,7,6.654,7,'hola'],(5,2), {1,2,3,'ojo'})) 
#Respetan un patrón en específico a menos de que se le indique el elemento dentro de la llave (se controla con el número en la llave)
# puede tener cualquier tipo de dato (int, float, lista, tupla, set etc...)

#También es posible manejarlo de esta forma 
message1 = "Hello {second_number} world, Estoy equivocado, somos {first_number}"

print(message1.format(first_number=12, second_number = 10 ))
