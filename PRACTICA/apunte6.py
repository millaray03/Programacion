#mostrar la suma y la cantidad de numeros pares comprendidos entre dos numeros ingresados por teclado

#5 y 10 

#6
#8
#2numero

numero_inicial = int(input("introdusca el numero inicial:"))
numero_final = int(input("introdusca el numero final:"))
cantidad = 0 

while numero_inicial <= numero_final:
    if numero_inicial % 2 ==0: 
        print(numero_inicial)
        cantidad += 1 
    numero_inicial += 1 
    
print("hay",cantidad,"numeros pares")