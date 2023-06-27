
# ingresar 4 notas por consola, mostrarlos en una lista y calcular el promedio 

lista = [ ]
suma = 0 

for i in range(4) :
    nota = float (input("ingrese la nota"))
    lista.insert(i, nota)
    suma = suma + lista[i]
promedio = suma/4 

print(lista)
print("el promedio es:", promedio)
    