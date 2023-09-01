'''Programar una “calculadora” que reciba como entrada un string de la forma “[int1]/[int2]”, realice
la división int1/int2 y despliegue el resultado con hasta dos dígitos decimales. En caso de que el
resultado tenga más de dos dígitos decimales, se debe redondear.'''
#@author Belen Albano

s1 = str(input('Ingrese la division: '))
num=s1.split('/')
n1=int(num[0])
n2=int(num[1])
d=n1/n2
print(round(d,2))