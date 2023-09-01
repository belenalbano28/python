#Escriba un programa que reciba como entrada dos montos para realizar depósitos y dos tasas de
#interés anual correspondientes.
#El programa debe calcular los intereses generados por los dos depósitos a un año y desplegará el
#interés que será mayor al año de hecho el depósito.
#@author Belen Albano
#Ejemplo de uso:
#Ingrese el primer monto: 1000
#Ingrese el segundo monto:  2000
#Ingrese la primera tasa: 9
#Ingrese la segunda tasa:  4
#El interes mayor es: 90.0, con la tasa=9% y monto=1000

m1 = int(input('Ingrese el primer monto: '))
m2 = int(input("Ingrese el segundo monto:  "))
t1 = int(input('Ingrese la primera tasa: '))
t2 = int(input("Ingrese la segunda tasa:  "))
tasa1=t1
tasa2=t2

if m1==0 or m2==0 or t1==0 or t2==0:
    print('Los numeros no deben ser 0')
else: 
    t1=t1/100
    t2=t2/100
    interes1=m1*t1
    interes2=m2*t2
    interes1=str(interes1)
    interes2=str(interes2)
    m1=str(m1)
    tasa1=str(tasa1)
    m2=str(m2)
    tasa2=str(tasa2)
    if interes1>interes2:
        print('El interes mayor es: '+interes1+', con la tasa='+tasa1+'% y monto='+m1)
    elif interes2>interes1:
        print('El interes mayor es: '+interes2+', con la tasa='+tasa2+'% y monto='+m2)
    else: print('Ambos intereses seran iguales. El valor es: ',interes1)
