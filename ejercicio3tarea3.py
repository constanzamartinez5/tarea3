#!/bin/python3
print("Por favor a continuaci�n ingrese la fecha que desea ")


meses = [1,2,3,4,5,6,7,8,9,10,11,12]
nombremes = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto",
             "septiembre","octubre","noviembre","diciembre"]

#termine cambiando la forma de ver los meses para no enredarme mas la cabeza :)



print("Por favor ingrese de forma n�merica el mes que desea: ")
a=int(input())
print(nombremes[a-1])

print("Por favor ingrese el a�o:")
b=int(input("ingresar a�o: "))

#calcular si el a�o dado es, o no, bisiesto


bis=0 #a�o bisiesto 1=es 0=no es
if b % 4 != 0: #no divisible por 4
  print("el a�o no es bisiesto")

elif b % 4 == 0 and b % 100 !=0: #es divisible por 4 y no entre 100 o 400
  print("el a�o es bisiesto")
  bis = 1
elif b % 4 == 0 and b % 100 == 0 and b % 400 != 0: #divisible entre 4 y 100 y no entre 400
  print("el a�o no es bisiesto")

elif b % 4 == 0 and b % 100 == 0 and b % 400 == 0: #divisible entre 4, 100 y 400

  print("el a�o es bisiesto")
  bis = 1
    
#calcular el n�mero de d�as transcurridos desde el principio del a�o dado
print("Por favor ingrese el d�a")

c=int(input("ingresar dia: "))

 # D�as restante primer a�o
 
 
diasmes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

s= a -2

#cd: cantidad de dias 
 
cd = 0 # suma de los dias de todos los meses
while s >=0:
    cd = cd + diasmes[s]
    s = s-1

total = cd + bis + c #total: total de dias en el a�o transcurridos

if total >4:
    natalicio = 365+bis+4-total

if total <=4:
    natalicio = 4-total
    
print (" ")
print (c ," de ", nombremes[a-1] ," del ",b)
print (" ")
print ("Los dias que an transcurrido desde el prinsipio del a�o son: ",total)
print (" ")
print ("Estamos a ",natalicio," dias del natalicio de Isaac Newton")