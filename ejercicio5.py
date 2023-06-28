#definir asignatura 

ramo = "programacion" 
print("Las notas corresponden al ramo:",ramo)

n1 = float(input("ingrese la primera nota"))
n2 = float(input("ingrese la segunda nota"))
n3 = float(input("ingrese la tercera nota"))

ponderacion= float(n1*0.3 + n2*0.4 + n3*0.3)
print ("su promedio es :",ponderacion)

if ponderacion < 4.0 :
    print ("El estuadiante reprobo")
if ponderacion > 4.0 :
    print ("el estudiante aprobo") 
if ponderacion > 6.0 :
    print ("el estudiante aprobo con distincion")




