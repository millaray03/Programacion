#Crear un algoritmo que permita saber si un año es bisiesto (calendario gregoriano) desde el año 0 en adelante.


def bisiesto(a): 
    if a<0: 
        print("el año",a, "no existe")
    elif (a % 4==0 and a % 100 !=0) or a % 400==0:
        print("el año",a, "es bisiesto")
    else: 
        print("el año", a, "no es bisiesto")

año= int(input("ingrese el año \n")) 
bisiesto(año)