texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod, diam sit amet dictum sagittis, neque urna sagittis augue, a venenatis ipsum velit eu sem. Ut dictum dictum accumsan. Sed id ligula purus. In dictum turpis erat. Integer feugiat nibh id orci sodales pellentesque. Integer eleifend enim non tincidunt volutpat. Ut quis lacus et urna varius congue in ac metus. Integer at nisl id nisi laoreet malesuada ac id nibh. Mauris euismod sapien id lacus viverra, sed venenatis augue porta.

Sed nisi leo, placerat eu risus quis, vestibulum mollis neque. Aenean eget risus sapien. Aliquam eget velit lacus. Fusce hendrerit nisi quam, euismod tempus dolor sodales ut. Morbi sit amet quam massa. Vivamus pharetra in mi at porta. Etiam ligula tellus, fermentum nec magna sed, facilisis mollis sem. Sed molestie vel orci et blandit. Maecenas aliquam nunc diam, eu viverra velit commodo vitae. Suspendisse augue mauris, volutpat vel dapibus id, feugiat sed odio.

Aenean volutpat turpis nec risus finibus tempor. Phasellus quis viverra urna. Maecenas pulvinar sollicitudin dolor, et vehicula dui maximus eu. Integer aliquam sapien ac eros vehicula, non ultricies odio tempus. Cras commodo, orci sed ullamcorper feugiat, justo libero egestas libero, at cursus leo neque sit amet ex. Cras sem arcu, dignissim sit amet neque quis, ornare ullamcorper nisi. Aenean viverra ullamcorper dui, vel facilisis elit tempor eu. Praesent in tellus venenatis, gravida est a, laoreet felis. Integer felis dolor, interdum in lectus in, egestas vehicula lorem. Nam sit amet mattis justo. Quisque faucibus, mi vel cursus aliquam, sapien augue commodo magna, a mollis lectus arcu in diam. Proin sit amet molestie quam.

Suspendisse potenti. Curabitur sed erat pellentesque, sagittis velit at, gravida lorem. Nullam id ligula tincidunt purus hendrerit placerat nec et nibh. Donec mi orci, commodo nec nulla at, mollis posuere erat. Suspendisse imperdiet vel velit sed euismod. Pellentesque dictum semper mattis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur viverra rhoncus turpis, ut tincidunt nisi elementum nec.

Praesent fermentum viverra arcu. Donec auctor arcu est. Nam placerat condimentum mauris. Nam mattis tempus ex, ac vehicula libero tincidunt nec. Pellentesque facilisis dictum pharetra. Aenean suscipit neque eu sem sollicitudin, non ultrices lacus accumsan. Mauris porttitor, ex posuere sollicitudin malesuada, mauris lacus consectetur lorem, vel congue dolor risus ut neque. Maecenas viverra tortor sed dolor tempus commodo quis id augue. Cras lectus nisi, commodo nec sodales quis, vehicula vel sem. Morbi id scelerisque leo, vel bibendum massa. Ut eleifend ipsum laoreet mauris molestie, quis ultricies eros accumsan."""
letras = ['abcdefghijklmnñopqrstuxywz']
caracteres =['a', 'e','i', 'o','u', ' ', ',' ]
estadisticas = ["total caracteres: ", "total de letras: ", "total de vocales a : ",  "total de vocales e : ",  "total de vocales i : ",  "total de vocales o : ", "total de vocales u : ",  "total de comas : ",  "total de vocales de puntos : ", "total de espacios :"]
totales = [0,0,0,0,0,0,0,0,0,0]

for c in texto:
    if c == letras:
        totales[3] = totales[1] 
    print (totales)
