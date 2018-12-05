def exercise01(x):
	z = x[0]
	y = x[3]
	list01 = [z,y]
	return list01

list02 = [1,2,3,4]

exercise01 (list02)
list01 = exercise01(list02)
print (list01)

A = [1,1,2,3,5,8,13,21,34,44,89]

def exercise02(g):
	for i in g :
		if i  < 5 :
			print (i)

exercise02(A)

r = [1,1,2,3,5,8,13,21,34,55,89]
z = [1,2,3,4,5,6,7,8,9,10,11,12,13]
g = []

for ir in range(len(r)):
	for iz in range(len(z)):
		if z[iz] == r[ir]:
			g.append(r[ir])

print(g)