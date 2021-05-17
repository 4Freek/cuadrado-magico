m = [[2,4,7],
	[3,5,6],
	[1,9,8]]

ms=[]
nivel=0
dd=[]
di=[]

#Itera y suma las filas y las agrega a la matriz raiz
[ms.append(sum(i)) for i in m]

#Itera y agrega las columnas para sumarlas en la matriz raiz
while nivel <= 2:
	[dd.append(i[nivel]) for i in m]
	ms.append(sum(dd))
	dd=[]
	nivel+=1

#Itera y agraga la diagonal derecha a la matriz raiz
dd.extend([f[i] for i,f in enumerate(m)])
ms.append(sum(dd))

#Itera y agraga la diagonal izquierda a la matriz raiz
di.extend([(f[-i-1]) for i,f in enumerate(m)])
ms.append(sum(di))

print(ms)

if ms.count(15) == len(ms) and len(ms) > 0:
	print("es magico")
else:
	print("no es magico")

print(all(15) in ms)