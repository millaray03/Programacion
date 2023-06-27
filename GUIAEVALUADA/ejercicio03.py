# HACER UN DICCIONARIO CON EL PAGO DE LOS 3 EMPLEADOS.

turno_diurno = 10 * 12000
turno_nocturno = 10 * 16000
DOMdiurno = 10 * 14000
DOMnocturno = 10 * 19000
pago_semanal1= (turno_nocturno * 3)+(turno_nocturno * 2) 
pago_semanal2 = (turno_nocturno * 3)+(DOMdiurno)
pago_semanal3= (turno_diurno * 3)+(turno_nocturno)+(DOMnocturno)

pago = {
    "empleado1": { ("Pago diario: LUN, MAR Y MIE: ", turno_nocturno, "JUE Y VIE: ", turno_diurno), ("Pago semanal: ", pago_semanal1)},
    "empleado2": {("Pago diario: MAR, MIE Y JUE: ", turno_nocturno, "DOM: ", DOMdiurno),("Pago semanal: ", pago_semanal2)},
    "empleado3": {("Pago diario: MIE, JUE Y VIE: ", turno_diurno, "SAB: ", turno_diurno, "DOM: ", DOMnocturno),("Pago semanal: ", pago_semanal3) }    
}

for x in sorted(pago):
    print(x,pago[x])
