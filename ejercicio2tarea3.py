#!/usr/bin/python
print("INSTRUCCIONES: ")
print("-ingrese sus notas para calcular su promedio en base a una escala de 1.1 a 7.0: ")
print("-ingrese sus notas separadas por una (,) ej: 3.4, 4.5")
a=input("ingresar notas: ")
lista=a.split(",")
print(lista)

for i in range(len(lista)): #para hacer la lista de las notas
  
  lista[i] = float(lista[i])
  
 #sacar el promedio en base a las notas ingresadas

suma=0

for i in range(len(lista)):
  suma = suma + lista[i]

print(suma)
print("tu promedio es: ")
#suma/len(lista)
print(suma/len(lista))




if (suma/len(lista)>= 4.0) :
  print("felicitaciones, vas camino a aprobar")
else:
    if(suma/len(lista)>= 3.0):
        print("atención, vas camino a reprobar")
    elif (suma/len(lista)< 3.0):
        print("pocas posibilidades de aprobar") 
