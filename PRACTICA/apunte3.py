
#ingresar n notas, mostrarlos en una lista y calcular el producto de todos sus valores 

n = int(input("ingrese la cantidad de notas: "))
lista = []
productos = 1 

for i in range(n) : 
    nota = str (input("ingre la nota :"))
    lista.insert(1,nota)
    producto = (producto * lista[i])
    
print(lista)
print("el producto de los valores ingresados es :", productos)


