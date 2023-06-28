#determinar la estacion del año segun el mes 

mes = str(input("escriba un mes:"))

estacion1 = 'verano'
estacion2 = 'otoño'
estacion3 = "invierno"
estacion4 = "primavera"

def estaciones_del_año(mes): 

    if mes  in ('enero', 'febrero', 'marzo'):
        print("corresponde a la estacion uno:",estacion1) 

    elif mes  in ('abril', 'mayo', 'junio'):
        print("corresponde a la estacion dos:",estacion2)

    elif mes  in ('julio', 'agosto', 'septiembre'):
         print("corresponde a la tercera estacion:",estacion3)

    else: 
        mes  in ('octubre', 'noviembre', 'diciembre')

        print("corresponde a la cuarta estacion del año:",estacion4)
         