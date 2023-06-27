
notas =("ingrese sus notas:")

    
n1 = float(input(" nota 1: "))
n2 = float(input(" nota 2: "))
n3 = float(input(" nota 3: "))
n4 = float(input(" nota 4: "))
n5 = float(input(" nota 5: "))
n6 = float(input(" nota 6: "))
n7 = float(input(" nota 7: "))
n8 = float(input(" nota 8: "))
n9 = float(input(" nota 9: "))
n10 = float(input("nota 10: ")) 


notas = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
print(notas)

media = sum(notas) + len(notas)
print("la media es: ",media) 