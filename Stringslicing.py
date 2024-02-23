message = "Hello world"
modified_msg = message.upper()
modified_lower = message.lower()

message2 = "    Helo world     "

whitespace = message.strip()

print(message[6:11])  # devuelve world solamente
print(message[4:])  # Devuelve o world
print(message[:9])  # Devuelve Hello wor
print(message[-6:])  # Devuelve  world

# Transformación a mayusculas

print(modified_msg, 'método upper')
print(modified_lower, 'método lower')
print(message, 'mensaje original')
print(whitespace, 'metodo strip para quitar los espacios')
print(message2,'mensaje con espacios')

message_replaced = message.replace('Hello','Hola') #se pueden poner palabras completas (todos los caracteres que requieras)
#También se reemplazarán todas los caracteres que coincidan (si hay más de una conicidenca las va a reemplazar)
print(message_replaced, 'mensaje com replace ')