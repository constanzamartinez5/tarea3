#!/usr/bin/python
print("ingresar los datos que se quieren dividir a continuaciòn: ")
a=int(input("poner el valor a: "))
b=int(input("poner el valor b: "))
sol= (a//b) #son 2 // para dividir
print(sol)
resto= a-b*(a//b) #para ver si divide bien o no
det= (a//b)
if (resto==0):
  print("B si divide a A en forma exacta")
else:
  print("B no divide a A en forma exacta")
  
