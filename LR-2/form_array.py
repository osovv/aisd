n = int(input('Enter n: '))

array = [1]
a = 1
for i in range(1, n+1):
	a  = a * 2/3 * i
	array.append(a)
print(array)