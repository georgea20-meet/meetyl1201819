list1 = [2,4,6,8]
def exercise_1(x):
	
	y = x[0]
	z = x[3]
	list2 = [y,z]
	return list2

exercise_1(list1)
list2 = exercise_1(list1)
print(list2)
