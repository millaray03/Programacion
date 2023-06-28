
def ingresodenumeros():
    numero = 0
    while numero != -1:
        numero = int(input("Ingrese número entero positivo: "))  
        if numero <= 0:
            continue
        numeros.append(numero)
        if numero % 2 == 0:
            numerospares.append(numero)
        else:
            numerosimpares.append(numero)
    return numeros
numeros = []
numerospares = []
numerosimpares = []

def pares(numerospares):
    sumnumerospares = sum(numerospares)
    return sumnumerospares

def impares(numerosimpares):
    sumnumerosimpares = sum(numerosimpares)
    return sumnumerosimpares   

def mayorypromedio(numeros):
    nummayor = max(numeros) 
    print("El número mayor es: ",nummayor)
    op = sum(numeros)/len(numeros)
    print("El promedio es: ", op)
    if nummayor > op:
        print("Es mayor que el promedio")
    elif nummayor < op:
        print("Es menor que el promedio") 
    else:
        print("Es igual al promedio")
    return
    

def sumatotal(numeros):
    sumtotal = sum(numeros)
    return sumtotal


print(ingresodenumeros())
print("La suma total es: ", sumatotal(numeros))
print("La suma de los números pares es: ",pares(numerospares))
print("La suma de los números impares es: ",impares(numerosimpares))
mayorypromedio(numeros)



