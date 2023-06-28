#guia rapida de operadores de python 

#01-OPERADORES ARITMETICOS

#declarando variables de tipo entero 
a = 20
b = 5
c = 4 
d = 20 

#operadores comunes 
print("suma entre a + b es : ", a+b)
print("resta entre a - b es : ", a-b) 
print("multiplicacion entre a* b es : ", a*b)
print("division entre a / b es : ", a/b)
print("el modulo entre a y b es : ", a%b)
print("el cociente entre b / c es : ", b//c)
print("el resultado de b elevado a c (5^4):", b ** c, "\n")

#declarando variables de tipo flotantes
t = 5.39 
g = 9.81 

#operacion aritmeticas con flotantes 
v = g*t 

print(f"la velocidad del objeto en caida libre es de: {v} m/s")
print("la velocidad del objeto en caida libre es de: {:2f}".format(v))
print(f"la velocidad del objeto en caida libre es de: {v:.2f}")
print("la velocidad del objeto en caida libre es de:","%.2f" % v)
print("\n")

#declarando variables de tipo complejo 
c1 = 4 + 3j
print(type(c1))

#creando un numero complejo con complex 
c2 = complex(3, -5)

print("el numero complejo es:",c2)

print(c2.real)
print(c2.imag)

#se puede realizar esta operacion? multiplicar un string por un entero 
print("hola" * 5)

#esta operacion un poco mas elaborada 
print("hola" * (int((10 * 2) / 5)), "\n")


#02- OPERADORES DE COMPARACION 
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(c >= d)
print(c <= d)

#comparando cadenas de caracteres 
animal_domestico = "gato"
animal_salvaje = "leopardo"
print("\n comparando cadenas de caracteres")
print(animal_domestico == animal_salvaje)
print(animal_domestico != animal_salvaje)
print(animal_domestico > animal_salvaje)
print(animal_domestico < animal_salvaje)
print(animal_domestico >= animal_salvaje)
print(animal_domestico <= animal_salvaje)

#03-OPERADORES LOGICOS

bencina = True
encendido = False
edad = 19 

#utilizando el operador AND 
if bencina and encendido: 
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")

#utilizando el operador OR 
if not bencina or encendido:
    print("utilizando NOT Y OR: el vehiculo puede avanzar")
else: 
    print("el vehiculo no puede arrancar")

#utilizando el operador NOT junto al AND y OR 
if not bencina or (encendido and edad >= 18):
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")
    