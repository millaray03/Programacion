
a = ["Rojo", "Verde", "Celeste", "Violeta"]
b = ["Osorno", "Puerto Montt", "Puerto Varas", "Valdivia"]

#mas caracteres 
def encontrar_palabra_mas_larga(a):
    palabra_mas_larga = ""
    for palabra in a:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga

a = ["Rojo", "Verde", "Celeste", "Violeta"]
palabra_mas_larga_a = encontrar_palabra_mas_larga(a)
print(palabra_mas_larga_a)

#menos caracteres 
def encontrar_palabra_mas_corta(b):
    palabra_mas_corta = b[0]
    for palabra in b:
        if len(palabra) < len(palabra_mas_corta):
            palabra_mas_corta = palabra
    return palabra_mas_corta

b = ["Osorno", "Puerto Montt", "Puerto Varas", "Valdivia"]
palabra_mas_corta_b = encontrar_palabra_mas_corta(b)
print(palabra_mas_corta_b)

#concatenar listas 
def concatenar_listas(a, b):
    return a + b

a = ["Rojo", "Verde", "Celeste", "Violeta"]
b = ["Osorno", "Puerto Montt", "Puerto Varas", "Valdivia"]
concatenacion = concatenar_listas(a, b)
print(concatenacion)

#transformando a mayuscula 
def convertir_mayusculas(lista):
    lista_mayusculas = []
    for elemento in lista:
        lista_mayusculas.append(elemento.upper())
    return lista_mayusculas

a = ["Rojo", "Verde", "Celeste", "Violeta"]
a_mayusculas = convertir_mayusculas(a)
print(a_mayusculas)

#ordenar listas 
def ordenar_lista(lista):
    lista.sort()
    return lista

a = ["Rojo", "Verde", "Celeste", "Violeta"]
a_ordenada = ordenar_lista(a)
print(a_ordenada)