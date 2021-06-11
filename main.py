archi=open('Texto.txt','r') 
texto = archi.read() 
archi.close()
 
quitar = ",;:.\n!\"'–‘[]{}()"
for caracter in quitar:
  texto = texto.replace(caracter,"")
texto = texto.lower()

palabras = texto.split(" ")

diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1


def Buscar(palabra1):
  for palabra in diccionario_frecuencias:
      if(palabra1 == palabra):
        frecuencia = diccionario_frecuencias[palabra]
        print(f"La palabra '{palabra}' se repite:  {frecuencia}")

def Mostrar():
  for palabra in diccionario_frecuencias:
      frecuencia = diccionario_frecuencias[palabra]
      if(frecuencia > 2):
        print(f"La palabra '{palabra}' se repite:  {frecuencia}")
  
print("1.-Buscar\n2.-Imprimir palabras que se repiten mas de 2 veces\n")
op = int(input("Opcion: "))
if(op==1):
  palabra1 = input("Escriba la palabra: ")
  Buscar(palabra1)
if(op==2):
  Mostrar()