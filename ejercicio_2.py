#Aceptar dos números desde teclado y retornar su suma, multiplicación, división y potencia.
#@author Belen Albano
#tomo como dividendo el primer numero y como divisor el segundo. Por otra parte tomo como base
#de la potencia el primer numero, y como exponente el segundo.
#no permito ingresar el numero 0 para simplificar el programa.

#Ejemplo de funcionamiento: el usuario ingresa 2 y 3. El programa retorna suma: 5, multiplicacion:6;
#division: 0.67 (redondeado a dos decimales), potencia: 8
num1 = int(input('Ingrese el primer número: '))
num2 = int(input("Ingrese el segundo número:  "))

if num1==0 or num2==0:
    print('Los numeros no deben ser 0')
else: 
    suma=num1+num2
    division=num1/num2
    division=round(division,2)
    multiplicacion=num1*num2
    potencia=num1**num2
    print('La suma es: ', suma)
    print('La multiplicacion es: ', multiplicacion)
    print('La division es: ', division)
    print('La potencia es: ', potencia)