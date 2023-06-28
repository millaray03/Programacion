
def elementos_comunes(lista_1,lista_2): 
    grupo1 = set(lista_1)
    grupo2 = set(lista_2)

    return set (grupo1 & grupo2)

grupo1 = {"marcos","gabriela","benjamin","matias"}
grupo2 = {"marcos","nicolas","diego","matias"}

resultado = elementos_comunes(grupo1, grupo2)

print (resultado)
