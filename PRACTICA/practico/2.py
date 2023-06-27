#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)

a = int(input("digite su edad: "))

for i in range(a) :
    print ( "has cumplido", str (i+1) + "años")
