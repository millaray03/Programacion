print()
ciudad = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
ica= [134, 99, 245, 50]


min=ica.index(min(ica))
print(f"La ciudad de {ciudad[min]}, tiene un ICA de {ica[min]}, BUENO")

max=ica.index(max(ica))
print(f"La ciudad de {ciudad[max]}, tiene un ICA de {ica[max]}, MUY DAÑINA A LA SALUD")
print()
for i in range(len(ciudad)):
    if ica[i] >= 0 and ica[i] <= 50:
        print(ciudad[i],", BUENO")
    elif ica[i] >= 51 and ica[i] <=100:
        print(ciudad[i],", MODERADO")
    elif ica[i] >= 101 and ica[i] <=150:
        print(ciudad[i],", DAÑINA A LA SALUD DE GRUPOS SENSIBLES")
    elif ica[i] >= 151 and ica[i] <=200:
        print(ciudad[i],", DAÑINA A LA SALUD")
    elif ica[i] >= 201 and ica[i] <=300:
        print(ciudad[i],", MUY DAÑINA A LA SALUD")
    else:
        print(ciudad[i],", PELIGROSA")