#mostrar la tabla de multiplicar del numero 7 
# 7*1
#7*2
# del ejercicio anterior, solicitar el numero de la tabla a  ultiplicar 

tabla = int(input("introdusca la tabla de multiplicar"))
inicio = 1

while inicio <= 10: 
    resultado = tabla * inicio 
    print(tabla,"*",inicio,"=",resultado)
    inicio += 1 