#print

nombre = "millaray"
print ("hola soy" ,nombre)

nombre = "millaray"
print (f"hola soy {nombre}")

nombre = "millaray"
print ("hola soy " + nombre)

#input 

nombre = input ("cual es tu nombre")
print (f" hola, mi nombre es {nombre}")

#esto es un comentario 

#int: enteros 
#float: punto flotante, numeros reales 
#complex: numeros coplejos 

# int 

#declarando dos variables enteros 
edad = 19
cumpleaños = 2004 

#impresion de variables 
print ("hola tengo", edad, "y naci en el año", cumpleaños, )

#float

#declarando variables tipo reales 
estatura = 1.65 
peso = 70.0 

#imprimiendo variables 
print ("mi estatura es", estatura, "y mi peso es", peso,"kg")

#strings 

asignatura = 'programacion'
carrera = "ingenieria civil en informatica"
descripcion = ''' la asignatura de programacion se imparte en el primer semestre,tiene como objetivo entragar la base logica para cualquier estudiante 
que comienze a familiarizarse con la programacion '''

saludo = "hola mundo"
print (saludo[0])
print (saludo[1]) 

print(saludo[-1]) 
print(saludo[-2])


#concatenar: unir dos o mas cadenas 

frase1 = "hola"
frase2 = "mundo"
resultado = frase1 + " " + frase2 
print (resultado) 

frase1 = "hola"
resultado = frase1 * 4 
print(resultado)

#division de cadenas 
institucion = "univercidad de los lagos"
print(institucion.split())
 
# booleanos

ampolleta = False 
interruptor = True 
print(ampolleta,interruptor)

print(1> 0)
print(10< 5)
print(100 == 100) 

print(bool(0))
print(bool(""))
print(bool([]))
print(bool("false"))
print(bool(1))

#lista 

num = [1,2,3,4,5,6,7]
lenguaje =list(["python","dart"])


estudiantes = ["matias", "marco", "cristobal", "sebastian", "marco"]
print(estudiantes[0])

print(estudiantes.count("marco"))

#tuplas 

newtupla = tuple()

newtupla = ("daniel","cristian",300)

#set 

conjunto_vacio = set()

conjunto_vacio = {}


#diccionario 

paciente = { 
    "nombre" : "alfredo", 
    "edad" : 29,
    "ciudad" : "osorno"
     }

hospital = dict(
        nombre = "hospital san jose",
        direccion = "dr.guillermo buhler 1795",
        ciudad = "osorno"
     )


#inmutabilidad de enteros, flotantes y complejos 

a = 100
print(f'el valor de a es {a}')

b = a 
print(f'el valor de b es {b}')

a = 200
print(f'el valor de a es {a} y el valor de b es {b}')



#ciclo while 

numero = 1 

while numero <= 10 : 
     print(numero)
     numero += 1 

#ciclo for 

#for variable in secuencia: 
     #instrucciones 
     
numeros = [2,3,5,7,11]

for num in numero: 
     print(num) 

#append: agrega un elemento a la lista 
#insert : inserta un elemento en una pocicion espesifica de la lista 
#remove elimina la primera ocurrencia de una lista 
#pop : borra y retorna el ultimo elemento de una lista 
#sort : ordena los elementos de la lista de manera asendente 
#count : devuelve el numero de veces que aparece el valor en la tupla 
#index : devuelve el indice del elemento seleccionado en la tupla 
#sorted : entrega una lista ordenada con los elementos de una tupla 
#item :devuelve una lista de tuplas, donde cada tupla tiene su clave 
#keys : devuelve una lista con todas las claves de un diccionario 
#round : dos decimales 