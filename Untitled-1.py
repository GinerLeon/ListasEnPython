# while 
print("While")
print("Elementos de la list2")
list2 = ["Pantalla", "Teclado","Bocinas","mouse","USB","CD","Quemador","impresora","webcam","microfono","cargador"]


#Recorrer la lista con while


i = 0
while i < len(list2):
    print(list2[i]) 
    i = i+1


#Acceder a los elementos de list2 por medio de indices 

print("la list2 tiene ", len(list2), "elementos")
print("todos los elementos 0-9", list2[0:10], "elementos")
print("Elementos del 2-6", list2[2:7], "elementos")
print("Elemntos desde el 5 hasta el ultimo", list2[5:], "elementos")
print("Imprimir los primeros 4 elementos del ", list2[:3], "elementos")


# Realizar los siguientes ejercicios
# 1. Extraer 'mouse', 'usb', 'cd', 'quemador', 'impresora' con indices
# 2. extraer   'mouse', 'usb', 'cd', 'quemador', 'impresora', 'microfono', 'webcam'
# 3. extraer 'pantalla', 'teclado', 'bocinas', 'mouse', 'usb', 'cd', 'quemador', 'impresora'
# 4. Programar para extraer 'pantalla', 'bocinas',  'usb', 'quemador', 'microfono'
# 5. Programar para extraer de la list2, la sublista equipo = ['mouse', 'cd', 'microfo', 'cargador'] con su numero de indice de cada uno
    
print(list2[3:8])
print(list2[3:9])
print(list2[0:8])

i = 0
while i < len(list2)-2 :
    print(list2[i]) 
    i = i+2
    
print(list2[9]) 



list2 = ["Pantalla", "Teclado","Bocinas","mouse","USB","CD","Quemador","impresora","webcam","microfono"]
equipo = ['mouse', 'CD', 'microfono', 'cargador']
var1 = ""
var2 = ""

i = 0
while i < len(equipo):
    item = equipo[i]
    if item in list2:
        print("Indice " + str(list2.index(item)) + " : " + item)
    else:
        print(item + " NO encontrado en lista2")
    i += 1


    

    

    





    