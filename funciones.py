#funciones 

#01-DECLARANDO LA PRIMERA FUNCION 

def mi_primera_funcion(): 
    print("esta es mi primera funcion")

mi_primera_funcion() 

#02-DECLARANDO UNA FUNCION Y UTILIZANDO LISTAS 

def concatenar(lista1,lista2): 
    return lista1 + lista2 

lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar()
print(concatenar(lista1,lista2))

#03-DECLARANDO UNA FUNCION MULTIPLICACION PASANDO PARAMETROS 

def multiplicacion (num1,num2) :
    return num1*num2 

#multiplicacion()
print(multiplicacion(50,50))

#04-EJEMPLO DE UNA FUNCION 

def suma(a,b) : 
    return a+b 

def resta(a,b) : 
    return a-b 

a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))

#se llama a la funcion suma
resultado = suma(a,b)
print("la suma es de:", resultado)

#se llama a la funcion resta 
resultado2 = resta(a,b)
print("la resta es de:", resultado2)

#05-PASANDO PARAMETROS POR VALOR 

def modificar_numero(x):
    x = 10 

x = 5 
print("antes de llamar a la funcion:", x)
modificar_numero(x)
print("despues de llamar a la funcion:", x)


#06-PASANDO PARAMETROS POR REFERENCIA 

#paso por referencia 
def op_lista(lista):
    lista.append(4)

numeros = [1, 2, 3]
op_lista(numeros)
print(numeros)

#paso por nombre de argumento
def saludar(nombre, mensaje): 
    print(mensaje + " " + nombre)

saludar(mensaje = "hola", nombre = "juan")
