#GUIA RAPIDA BUCLES 

from colorama import init, Fore 
init(autoreset = True)

#01-WHILE 
edad = 15
num = 0 

#que hace este bucle? 
print(Fore.YELLOW + '\n>>> impresion de numeros de 0 al 100 (incremento de 2 en 2)')

num = 0 
while num <= 100:
    print(num)
    num += 2 
print(Fore.RED + "primer bucle terminado!\n")

#combinando while y else 
print(Fore.YELLOW + '\n>>> impresion de numeros de 100 al 200')

while num <= 200: 
    print(num)
    num += 2 
else: 
    print("mi condicion es igual o mayor a 200 ")
print(Fore.RED + "segundo bucle terminado!")

#combinando while y if 
print(Fore.YELLOW + '\n>>> impresion de numeros de 200 al 300')

while num <= 300: 
    print(num)
    num += 2 
    if num == 250: 
        print("mi condicion es igual a 250")
print(Fore.RED + "tercer bucle terminado!\n")

#utilizando el break 
print(Fore.YELLOW + '\n>>> impresion de numeros de 300 al 400')

while num <= 400: 
    print(num)
    num += 2
    if num == 350: 
        print(Fore.MAGENTA + "se define la ejecucion")
        break 
print(num)
print(Fore.RED + "cuarto bucle terminado!\n")

#utilizando el continue 
print(Fore.YELLOW + '\n>>> impresion de numeros de 0 al 50')
num = 0
while num <= 50: 
    num += 1 
    if num == 40: 
        continue
    print(num)


