#eliminando elemento de una lista 

numeros = [4,3,8,12,6,10,14,3,6]
#indice = [0 , 1, 2 ,3 ,4, 5, 6, 7, 8,]

del numeros[8]
print (numeros)
 
#añadiendo un elemento a la lista 

numeros.insert(0,'2')
print(numeros)

#eliminando elementos repetidos de una lista 

numeros =[4,3,8,12,6,10,14,3,6]
print("contenido actual de la lista",numeros)
print("cantidad actual de la lista numeros:", len(numeros))

print()
numeros_sin_repetir = []

for n in numeros:
      if n not in numeros_sin_repetir:
        numeros_sin_repetir.append(n)


print("contenido actual de la lista 'numeros_sin_repetir':",numeros_sin_repetir)
print("cantidad actual de la lista 'numeros_sin_repetir':",len(numeros_sin_repetir))


#obtener la media y la mediana 

media = sum(numeros) / len(numeros)
print ("la media es :",media)

mediana = sorted(numeros) [len(numeros)//2]
print ("la mediana es : ", mediana)
