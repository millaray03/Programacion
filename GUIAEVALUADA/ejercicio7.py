num = int(input("Ingrese número: "))

def factorial(num):
    if num > 0:
        num = num * factorial(num-1)
    elif num < 0:
        num = None
    else:
        num = 1
    return num
f = factorial(num)
print(f)
 
 
