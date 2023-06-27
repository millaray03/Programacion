
numero = int(input("digite un numero:"))
impar = (numero*(numero-1)) + 1 
acum = 0

for i in range(numero) : 
    acum = acum + impar 
    if i == (numero-1):
        break 
    impar = impar + 2
    print(impar)
print(f"el cubo de {numero} es: {acum}")




