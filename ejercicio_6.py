tr1 = 'Curso de Python'
print('El string original es:',tr1)
# Obtener el primer caracter
res = tr1[0]
# Obtener largo del string
l = len(tr1)
# Obtener el valor del medio
medio = int(l/2)
# Obtener el carácter del medio y agregarlo al string
res = res + tr1[medio]
# Obtener el último carácter y agregarlo al resultado
res = res + tr1[l-1]
print("Nuevo String:", res)
