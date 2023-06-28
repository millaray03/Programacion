def nombres():
    a=[]
    while True:
        nombre=input("Ingrese un nombre o SALIR para salir\n")
        if nombre == "SALIR":
            break
        else:
            a.append(nombre)
    return a

    
def letras(list):
    listas=[]
    for i in range(0,len(list)):
        listas.append(len(list[i]))
    return(listas)

def mostrar(nombre,lista):
    print("los nombres ingresados son")
    for i in range(0,len(nombre)):
        print("Nombres",nombre[i],"    ","Letras",lista[i])
    print(sum(lista))
   
listas1=nombres()
mostrar(listas1,letras(listas1))