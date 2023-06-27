
numeros = []
import random 

for i in range(20):
    n = random.randrange(40,350)
    numeros.append(n) 
    print(n)
    
a = input("escoge un numero del 40 al 350 \n")
a = int(a)
b = numeros.count(a)
print ("el numero", a , "se repite", b , "veces")  