"""guia rapida """

#este es un comentario de linea 

""" este
es un comentario
multilinea """

# un print 
print("hola soy constanza")

#01- DECLARANDO VARIABLES TIPO CADENAS 
nombre = "constanza"
name = "victor"

#02- IMPRESION DE UNA VARIABLE 
print(name)
print("holas soy", name)

#declarando una variable de tipo numerico
edad = 29 

#03- IMPRESION DE TEXTO + VARIABLE 
print("mi edad es de", edad)

#04- IMPRIMIENDO DOS VARIABLES EN UNA MISMA LINEA 
print ('hola mi nombre es',nombre, "y tengo", edad) #impresion separada con comas
print ("hola mi nombre es"+" "+name+""+"y tengo"+str(edad)) #concatenacion con signo
print (f"hola mi nombre es {nombre} y tengo,{edad} años") #formato de cadenas literales

#05- ACTUALIZANDO LA VARIABLE NOMBRE 
nombre = "diego"
name = "benjamin"
print("hola mi nuevo nombre es", nombre)
print("hola mi nombre nuevo nombre es", name)

#06- VARIABLES EN UNA SOLA LINEA 
ciudad, region, pais, year = "puerto montt", "los lagos", "chile", 2010 
print ("yo naci en la ciudad de", ciudad, "region de", region,pais, "el año",int(year))

#07- UTILIZANDO LA INSTRUCCION INPUT 
nombre1 = input("¿cual es tu nombre?\n") 
edad1 = input("¿cual es tu edad? \n")

print ("tu nombre es:", nombre1, "y tu edad es:", edad1)

#08- ACOTACION CONSTANTES
pi = 3.14
ciudad = "osorno"