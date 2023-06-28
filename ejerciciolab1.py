
pacientes =[ ["pedro", 1.78], ["constanza", 1.56], ["Amanda", 1.62] , ["Dario", 1.89],
["Fernanda", 1.67] ]

#estatura minima 
def estatura_minima(pacientes):
    min_estatura = min(pacientes, key=lambda x: x[1])[1]
    return round(min_estatura, 1)

#nuevo elemento 
def insertar_paciente(pacientes, nuevo_paciente):
    pacientes.append(nuevo_paciente)

#encontrar elemento 
def buscar_paciente(pacientes, nombre_paciente):
    for paciente in pacientes:
        if paciente[0] == nombre_paciente:
            return paciente[1]
    return "No se encuentra el paciente"

#invocar las funciones 
estatura_minimaa = estatura_minima(pacientes)
print("La estatura menor entre todos los pacientes es:", estatura_minimaa)

nuevo_paciente = ["Ricardo", 1.71]
insertar_paciente(pacientes, nuevo_paciente)
print("La lista de pacientes actualizada es:", pacientes)

estatura_dario = buscar_paciente(pacientes, "Dario")
if estatura_dario != "No se encuentra el paciente":
    print("La estatura de Dario es:", estatura_dario)
else:
    print("No se encuentra el paciente Dario")