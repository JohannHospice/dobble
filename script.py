def	intToBin(x, n):
	if x >= pow(2, n):
		raise Exception()
	c = [0] * n
	for j in reversed(range(0, n)):
		nx = x - pow(2, j)
		print(nx)
		if nx >= 0:
			x = nx
			c[j] = 1
	return c

a = intToBin(3, 2)

print(a)