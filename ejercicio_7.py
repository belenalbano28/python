#Sean dos strings, s1 y s2. Escriba un programa que cree un nuevo string s3, compuesto con el
#primer carácter de s1, luego el último carácter de s2, luego, el segundo carácter de s1 y el penúltimo
#carácter de s2 y así sucesivamente. 
#@author Belen Albano
#Ejemplo
#Ingrese una cadena cualquiera: hola
#Ingrese otra cadena cuaquiera:  otracadena
#haonleadacarto
s1 = str(input('Ingrese una cadena cualquiera: '))
s2 = str(input("Ingrese otra cadena cuaquiera:  "))

l1=len(s1)
l2=len(s2)
s2=s2[::-1]
r=''
for a, b in zip(s1, s2): 
    r=r+a+b
if l1<l2:
    r=r+s2[l1:]
elif l2<l1:
    r=r+s1[l2:]
print(r)