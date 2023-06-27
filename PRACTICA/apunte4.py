
#mostrar la suma de los numeros multiplos de 5 menores a 50 
# 5+10+15......+45 
#del ejercicio anterior, solicitar el numero limite a calcular 

a = 0 
suma = 0

numero_maximo = int(input("ingrese el numero maximo"))

while a < numero_maximo : 
    suma += a
    a += 5 
print("la suma es :", suma)
