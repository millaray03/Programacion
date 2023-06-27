#definir diccionario

regiones =  { 

"nombre1" : "biobio",
"id1" : "8",
"superficie1" : "23890",
"habitantes1" : "828708",
"nombre2" : "los lagos",
"id2" : "10",
"superficie2" : "48583",
"habitantes2" : "828708",

   }

print (regiones)


regiones["densidad del biobio"] = "65.0"
regiones["densidad de los lagos"] = "17.0"

densidadbiobio = float (1556805 // 23890 )
print ("la dencidad de la region del biobio es:", densidadbiobio)

densidadloslagos = float  (828708 // 48583) 
print ( "la densidad de la region de los lagos es:", densidadloslagos) 

regiones["capitalbiobio"] = ('concepcion')
regiones["capitalloslagos"] = ('puerto montt')

regiones["comunas biobio"] =  ('lota', 'lebu', 'los angeles')
regiones["comuna loslagos"] = ('castro','puerto varas', 'purranque') 

regiones["provincia biobio"] =  ('biobio','arauco','concepcion')
regiones["provincia loslagos"] =  ('osorno','llanquihue','chiloe','palena')

print(regiones)


