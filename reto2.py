nombre = input ("ingrese el nombre del estudiante:")
print()
asignatura = input ("ingrese nombre de la asignatura:")
print()
notalab1 = float (input("ingrese nota laboratorio n°1:"))
print()
notalab2 = float (input("ingrese nota laboratorio n°2:"))
print()
ponderacion =float(notalab1*0.03 + notalab2*0.70)
print()
ponderacion = { 
    "nombre" : nombre,
    "asignatura" : asignatura,
    "notalab1" : notalab1, 
    "notalab2" : notalab2, 
    "ponderacion" : ponderacion,
     }
print (ponderacion)
