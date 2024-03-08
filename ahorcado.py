import random

palabras=['Perro','Gato','Almoadilla,', 'Agua','Acero','Python','Industrial','calma','Bromo','Oso','Caballo']
palabra=random.choice(palabras)
palabra = palabra.lower()



respuesta  = '_' * len(palabra)

max_errores = 3


print(respuesta)


while max_errores > 0 and respuesta != palabra:
    letra = input('Por favor, introduce una letra: ')
    letra = letra.lower()

    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                respuesta = respuesta[:i] + letra + respuesta[i+1:]
    else:
        max_errores -= 1
        intentos = str(max_errores)
        print('¡Incorrecto! Te quedan ' + intentos + ' intentos.')

    print(respuesta)



if respuesta == palabra:
    print('¡Felicidades, has ganado!')
else:
    print('Lo siento, has perdido. La palabra era ' + palabra)

         
         


