def plata(objeto):
    while True:
        pago=input("¿con cuanto paga?\n")
        try:
            pago=int(pago)
            objeto=int(objeto)
            redondeo=objeto%10
            if redondeo>=5:
                objeto=objeto+(10-redondeo)
            elif redondeo<=4:
                objeto=objeto-(redondeo)
            if pago>=objeto:
                resultado=pago-objeto
                break
            else:
                error=int("A")
        except:
            print("ingrese un pago aceptable")
    return resultado

producto=input("Elija un producto a comprar\n")
while True:
    Valor=input(f"Ingrese el valor de {producto}\n")
    try:
        objeto=int(Valor)
        break
    except:
        print("Ingrese un valor valido")
print("Su vuelto es de $",plata(objeto))

