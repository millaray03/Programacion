#ejercicio 5
print()

def es_par(n):
    if n % 2 == 0:
        return n
   
def es_primo(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def es_mayor_a_50(n):
    if n > 50:
        return True
    else:
        return False
    
n = int(input("ingrese un numero: "))

if es_par(n):
    print(f"{n} es un numero par")
else:
    print(f"{n} es un numero impar")

if es_primo(n):
    print(f"{n} es un numero primo")
else:
    print(f"{n} no es un numero primo")

if es_mayor_a_50(n):
        print(f"{n} es mayor a 50")
else:
    print(f"{n} es menor o igual a 50")
print()