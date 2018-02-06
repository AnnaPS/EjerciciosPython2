#-*- coding: UTF-8 -*-
#Ejercicio 1
print("MAÑÁ")
listado=[]

for numero in range (100):
    listado=[numero+1]
    print (listado)

#Ejercicio 2
meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
num=int(input("Inserte un numero: "))-1
if  num <= len(meses) and num>=0:
   print(meses[num]) 
else: 
    print("Error, el numero es mayor que la lista")
    
#Ejercicio 3
multi=int(input("Mostrar tabla de multiplicar del numero: "))
listaMulti=[]
x = 1
while x <= 10:
    listaMulti.append(multi*x)
    print(listaMulti[x-1])
    x += 1
    
#Ejercicio 4
num=(int(input("Inserte un numero: ")))
listaNumeros=[]
while num !=0:
    listaNumeros.append(num)
    num=(int(input("Inserte un numero: ")))
    
print(sorted(listaNumeros))

#Ejercicio 5
num=(int(input("Inserte un numero: ")))
listaNumeros=[]
while num !=0:
    listaNumeros.append(num)
    num=(int(input("Inserte un numero: ")))
    
print(sorted(listaNumeros,reverse=True))

#Ejercicio 6
cad=input("Inserte una frase: ")
cadenaSinEspacios=cad.replace(' ','')
listaCadena=[cadenaSinEspacios]
print(listaCadena)

#Ejercicio 7
cad=str(input("Inserte una frase: "))
lista=[]
for x in cad:
    if x not in lista:
        lista.append(x)
#Para no introducir espacios en la lista
#Comprueba si la lista contiene un espacio
if lista.__contains__(' '): 
    lista.remove(' ')
print(lista)

#Ejercicio 8
tuplaNumeros=(1,3,5,6,2,8,6,3,2,1,5,7,8,3,2)
cont=0
numero=(int(input("Inserte un numero: ")))
for x in tuplaNumeros:
    if x==numero:
        cont=cont+1
print('El numero '+str(numero)+' esta en la lista '+str(cont)+' veces')

#Ejercicio 9
tuplaNumeros = (10,5,7,60,70,15,9,7,2)
print('El numero mayor es: ',max(tuplaNumeros))
print('El numero menor es: ',min(tuplaNumeros))

#Ejercicio 10
listinTelefonico={"Ana":916854589,"Ivan":917548565}
print(listinTelefonico["Ana"])

#Ejercicio 11
numeros=(1,2,3,4,5,6,7,8,9,10)
num=int(input("Introduce un indice: "))-1
if num <=len(numeros):
    print(numeros[num])   
else:
    print("error")