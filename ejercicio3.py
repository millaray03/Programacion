#definir si un triangulo es equilatero,isoseles o escaleno 

lado1 = int(input("digite medida del lado uno"))
lado2 = int(input("digite medida del lado dos")) 
lado3 = int(input("digite medida del lado tres"))

def tipo_triangulo(a,b,c):
    if a == b and a==c :
        return 'equilatero'
    elif a != b and a!= c :
        return 'escaleno'
    elif a ==b and a != c : 
        return 'isoseles'
    
def area_triangulo(a,b,c): 
    if tipo_triangulo(a,b,c):
        s = (a+b+c)/2
        heron_area =s (s*(s-a)*(s-b)*(s-c))
        return heron_area
    else:
        return 'no es un triangulo'   

print(tipo_triangulo(lado1,lado2,lado3))



