#guia rapida condicionales 

from colorama import init, Fore 
init()

licencia = False
edad = 19 
automovil = False 

#estara correcto este codigo? 
print(Fore.YELLOW + '\n>>> testeando los comparadores y el IF')
if licencia: 
    print(Fore.wite + 'puedo conducir porque tengo licencia')
else: 
    print(Fore.WITE + 'no tengo licencia de conducir')

#se debe asignar directamente 

print(Fore.YELLOW + '\n>>> utilizando el primer condicional IF')
if licencia: 
    print(Fore.WHITE + 'puedo conducir porque tengo licencia\n')
else: 
    print(Fore.WHITE + 'no tengo licencia para conducir\n')
print("este print esta fuera del else")


print(Fore.YELLOW + '>>> utilizando el segundo condicional IF')
if edad:
    print(Fore.WHITE + 'puedo conducir porque soy mayor de edad\n')
else: 
    print(Fore.WHITE + 'no puedo conducir soy menor de edad\n')


