
num1 = int(input("escriba el primer numero:"))
num2 = int(input("escriba el segundo numero:"))
num3 = int(input("escriba el tercer numero:"))

if num2 < num1 >= num3 :
  print("el numero mayor es el primer numero. numero:",num1)
  print("el numero menor es el segundo numero. numero:",num2)

if num3 < num2 >= num1 :
    print("el numero mayor es el segundo numero. numero:",num2)
    print("el numero menor es el tercer numero. numero:",num3)

if num1 < num3 >= num2 :
    print("el numero mayor es el tercer numero. numero:",num3)
    print ("el numero menor es el primer numero. numero:",num1)

else: 
    print("todos los numeros son iguales") 

    