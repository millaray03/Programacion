'''GUIA RAPIDA TIPO DE DATOS'''

#01- DATOS DE TIPO NUMERICO
edad = 29 
estatura = 1.71
peso = 70.5 
complejo = 1 + 4j 

print(f"mi estatura es de {estatura} y mi peso es de {peso}")
print("impresion de un numero complejo:", complejo, "\n")

#transformamdo un valor real a entero 
print(peso)
print("transformando un valor real a entero:",int(peso))

#transformando entero a real 
print("transformando un valor entero a real:",float(edad))

#operacion aritmetica 
imc = peso / (estatura**2)
print(f"mi IMC es de:{imc}\n")

print("mi imc es de: {:.2f}".format(imc),"\n")

#02- DATOS DE TIPO CADENA DE CARACTERES 
asignatura = 'programacion'
carrera = "ingenieria civil en informatica "
descripcion = '''la asignatura de programacion se imparte 
en el primer semestre'''

print("la asignatura de", asignatura, "corresponde a la carrera de" ,
carrera)  
print(descripcion[12])

#utilizando la funcion len 
print("la cantidad de caracteres de la palabra", asignatura, "es de:",len(asignatura),"\n")
print("la cantidad de caracteres de la palabra", carrera, "es de:",len(carrera),"\n")

#03- VALORES BOOLEANOS 
ampolleta = False 
interruptor = True 

print(ampolleta,interruptor)
print("la variable ampolleta es de tipo:",type(interruptor),"\n")

#podemos transformar cualquier valor a booleano 
print(bool(0))
print(bool(""))
print(bool([]))
print(bool("False"))
print(bool(1))
print("\n")

#04- DATOS TIPO LISTA

#inicializando listas de dos maneras
nueva_lista = list()
otra_lista = []
print("esta es una lista vacia", nueva_lista)
print("esta es otra lista vacia",otra_lista)
print(type(otra_lista))

#declarando tres listas diferentes 
estudiantes = ["matias","marco","cristobal","sebastian","marco"]
num = [1,2,3,4,5,6,1]
lenguaje = list(["python","dart"])

#lista de datos compuestos 
data = ['osorno', {'uv': 'nivel bajo', 'temp°' :15}, (-40.5725,-73.1353)]
listamixta = ['felipe', 100, True] 

print("lista de cadena de caracteres:",estudiantes)
print("lista de numeros:",num)
print("lista de un elemento",lenguaje)
print("esta es una lista mixta:", listamixta)
print("esto igual es una lista", data)
print(len(listamixta))
print(estudiantes.count ("marco"))
print(num.count(5000))

lenguaje = ["javaScript"]
print("nuevo valor del arreglo de un elemento",lenguaje)

#como accedo a un elemento especifico de la lista
print(estudiantes[0])
print(estudiantes[1])
print(("posicion -2 de la lista estudiantes",estudiantes[-2]))

#reasignando el valor de la 3° posicion de la lista 
estudiantes [ 3 ] = "gabriela"
print( "el nuevo arreglo de estudiantes es:", estudiantes)

#iniciando otra lista de datos mixtos 
data_asig = [ 10023, "programacion", 1 , "verdadero" ]

#¿que hace este codigo? #desempaquetado elementos de la lista

cod, ramo, semestre, estado = data_asig 
print ( )

#¿se pueden sumar listas? 
print ("suma de listas:", estudiantes + num)

#¿que hacen estas funciones? 
print (list ("python"))
print (list(range(10)))
print("\n")

# > en el fichero de listas se mostraran mas funciones 

#05- TUPLAS - (No mutables)
newtupla = tuple()
grupo1 = ("daniel","cristian","felipe",200,100, "daniel")
print(type(grupo1))

#accediendo al primer elemento de la tupla
print( grupo1[0] )

#consultando el elemento "daniel" cuantas veces se encuentra en la tupla
print("el elemento se repite",grupo1.count("daniel"))

#muestra el indice del primer elemento buscado
print("indice del elemento",grupo1.index ("daniel"))

#reasignando el primer elemento de la tupla 
grupo1[0] = "constanza"
print(grupo1)

#¿se pueden sumar las tuplas?


#obteniendo un trozo de la tupla 
grupo2 = ("pedro",100,"felipe","diego",2020,"alejandra")
print("trozo de la tupla",grupo2[0:3])

#¿entonces como no puedo modificar una tupla, que puedo hacer?
grupo1 = list(grupo1)
print("la tupla ahora es de tipo:", type(grupo1),"\n")
print("\n")

#06 - SETS (conjuntos) - estructura fija 
conjunto_vacio = set()
conjunto_vacio1 = {} 
print(type(conjunto_vacio1))
conjunto_colores = set({"azul","rojo","verde"})
conjunto_animales = {"gato","perro","loro"}

print(type(conjunto_colores))
print(type(conjunto_animales))
print("el primer set contiene los siguientes colores:",conjunto_colores)
print("el segundo set contiene los siguientes animales",conjunto_animales)

#print(conjunto_animales[0]) #accediendo al primer elemento del set
conjunto_colores.add("celeste")
print("el set de colores lo conforman",conjunto_animales,"\n")


#07 - DICCIONARIOS 

diccionario1 = dict()
diccionario2 = {}

datos_personales = {  
    "nombre" : "victor", 
    "institucion" : "ulagos",
    "edad" : 29 
      }

print(datos_personales)

datos_personales = {  
    "nombre" : "victor",
    "institucion" : "ulagos", 
    "edad" : 29, 
    "asignaturas" : {"estructura de datos","programacion"}
    }

print("diccionario inicial:",datos_personales)

#consulta la cantidad de elementos del diccionario 
print(len(datos_personales))

"es facilmente accesible a los elementos dentro de un diccionario"
print(datos_personales["institucion"])

#¿como actualizamos el valor de una clave dentro de un diccionario?
datos_personales["institucion"] = "USS"
print("diccionario actualizado",datos_personales)

#agregando un nuevo clave al diccionario 
datos_personales["ciudad"] = "osorno"
print(datos_personales)
print("diccionario con el campo eliminado", datos_personales)

#eliminando un campo del diccionario
del datos_personales["ciudad"]
print("diccionario con el campo eliminado", datos_personales)

hospital = dict( 
    nombre = "hospital san jose", 
    direccion = "dr. guillermo buhler 1765",
    ciudad = "osorno"
)