
#definir funcion 

def funcion(frase): 
    palabras = frase.split()
    longitudes = map(len, palabras)
    
    return dict(zip(palabras, longitudes))

print(funcion(input("escriba una palabra")) )
