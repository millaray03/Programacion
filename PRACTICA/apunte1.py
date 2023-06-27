#calcular la suma de todos los numeros enteros ingresados, la suma de los pares y la suma de los impares

cantidad = int(input("ingrese la cantidad de numeros: "))
suma = 0
par = 0 
impar = 0 

for i in range(1,cantidad+1) : 
    num = int(input(f"digite el numero :"))
    suma = suma+num
    if num% 2 == 0 : 
        par = par+num
    else : 
        impar = impar + num 

print("la suma de todo los numeros es :", suma)
print("la suma de los numeros pares :", par)
print("la suma de los numeros impares :", impar)  