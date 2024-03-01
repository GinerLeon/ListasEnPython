texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, diam sit amet dictum sagittis, neque urna sagittis augue, a venenatis ipsum velit eu sem. Ut dictum dictum accumsan. Sed id ligula purus. In dictum turpis erat. Integer feugiat nibh id orci sodales pellentesque. Integer eleifend enim non tincidunt volutpat. Ut quis lacus et urna varius congue in ac metus. Integer at nisl id nisi laoreet malesuada ac id nibh. Mauris euismod sapien id lacus viverra, sed venenatis augue porta.

Sed nisi leo, placerat eu risus quis, vestibulum mollis neque. Aenean eget risus sapien. Aliquam eget velit lacus. Fusce hendrerit nisi quam, euismod tempus dolor sodales ut. Morbi sit amet quam massa. Vivamus pharetra in mi at porta. Etiam ligula tellus, fermentum nec magna sed, facilisis mollis sem. Sed molestie vel orci et blandit. Maecenas aliquam nunc diam, eu viverra velit commodo vitae. Suspendisse augue mauris, volutpat vel dapibus id, feugiat sed odio.

Aenean volutpat turpis nec risus finibus tempor. Phasellus quis viverra urna. Maecenas pulvinar sollicitudin dolor, et vehicula dui maximus eu. Integer aliquam sapien ac eros vehicula, non ultricies odio tempus. Cras commodo, orci sed ullamcorper feugiat, justo libero egestas libero, at cursus leo neque sit amet ex. Cras sem arcu, dignissim sit amet neque quis, ornare ullamcorper nisi. Aenean viverra ullamcorper dui, vel facilisis elit tempor eu. Praesent in tellus venenatis, gravida est a, laoreet felis. Integer felis dolor, interdum in lectus in, egestas vehicula lorem. Nam sit amet mattis justo. Quisque faucibus, mi vel cursus aliquam, sapien augue commodo magna, a mollis lectus arcu in diam. Proin sit amet molestie quam.

Suspendisse potenti. Curabitur sed erat pellentesque, sagittis velit at, gravida lorem. Nullam id ligula tincidunt purus hendrerit placerat nec et nibh. Donec mi orci, commodo nec nulla at, mollis posuere erat. Suspendisse imperdiet vel velit sed euismod. Pellentesque dictum semper mattis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur viverra rhoncus turpis, ut tincidunt nisi elementum nec.

Praesent fermentum viverra arcu. Donec auctor arcu est. Nam placerat condimentum mauris. Nam mattis tempus ex, ac vehicula libero tincidunt nec. Pellentesque facilisis dictum pharetra. Aenean suscipit neque eu sem sollicitudin, non ultrices lacus accumsan. Mauris porttitor, ex posuere sollicitudin malesuada, mauris lacus consectetur lorem, vel congue dolor risus ut neque. Maecenas viverra tortor sed dolor tempus commodo quis id augue. Cras lectus nisi, commodo nec sodales quis, vehicula vel sem. Morbi id scelerisque leo, vel bibendum massa. Ut eleifend ipsum laoreet mauris molestie, quis ultricies eros accumsan."""
letras = ['abcdefghijklmnñopqrstuxywz']
caracteres =['a', 'e','i', 'o','u', ' ', ',' ]
estadisticas = ["total caracteres: ", "total de letras: ", "total de vocales a : ",  "total de vocales e : ",  "total de vocales i : ",  "total de vocales o : ", "total de vocales u : ",  "total de comas : ",  "total de vocales de puntos : ", "total de espacios :"]
totales = [0,0,0,0,0,0,0,0,0,0]

# Total de caracteres
total_caracteres = len(texto)

# Total de letras (incluyendo vocales)
total_letras = 0
for c in texto:
    if c.isalpha():
        total_letras += 1

# Total de vocales y por cada vocal
total_a = 0
total_e = 0
total_i = 0
total_o = 0
total_u = 0

# Convertimos el texto a minúsculas para evitar diferencias entre mayúsculas y minúsculas
texto = texto.lower()

caracteres_lista =['a', 'e','i', 'o','u' ]  
total_vocals = 0
i = 0

while i < len(texto):
    item = texto[i]
    if item in caracteres_lista:
        total_vocals += 1
    i +=  1

# Recorremos cada carácter en el texto
for c in texto:
    if c == 'a' :
        total_a += 1
    elif c == 'e':
        total_e += 1
    elif c == 'i':
        total_i += 1
    elif c == 'o':
        total_o += 1
    elif c == 'u':
        total_u += 1


# Total de espacios
total_espacios =0
for c in texto:
    if c == ' ':
        total_espacios += 1

# Total de comas
total_comas=0
for c in texto:
    if c == ',':
        total_comas = total_comas + 1

# Total de palabras
total_palabras = len(texto.split())

print('Total de caracteres: ' + str(total_caracteres))
print('Total de letras: ' + str(total_letras))
print('Total de vocales: ' + str(total_vocals))
print('Total de vocales a: ' + str(total_a))
print('Total de vocales e: ' + str(total_e))
print('Total de vocales i: ' + str(total_i))
print('Total de vocales o: ' + str(total_o))
print('Total de vocales u: ' + str(total_u))
print('Total de espacios: ' + str(total_espacios))
print('Total de comas: ' + str(total_comas))
print('Total de palabras: ' + str(total_palabras))

