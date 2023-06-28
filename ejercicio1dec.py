#definiendo variable 
cantidad = 0
numeross = []
def cantidad_numeros(cantidad):  
 

 for i in range(1,cantidad +1) : 
     numero = int(input(f"digite el numero:"))
     numeross.append(numero)

def sumatotal(numeros): 
 suma = sum(numeros)
 return suma 
    
def sumapares(numeros): 
 pares = [i for i in numeros if  i % 2 == 0]
 suma = sum(pares)
 return suma 

def sumaimpares(numeros): 
    impares = [i for i in numeros if i % 2 != 0]
    suma= sum(impares)
    return suma

numeros_ingresados = int(input("ingrese la cantidad de numeros :"))
numeros = cantidad_numeros (numeros_ingresados)

print(f"la suma de la cantidad de numeros totales es: {sumatotal(numeross)}")
print(f"la suma de los numeros impares: {sumaimpares(numeross)}")
print(f"la suma de los numeros pares: {sumapares(numeross)}")

  




