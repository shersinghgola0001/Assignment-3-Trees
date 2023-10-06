def SumNodes(l):
	leafNodeCount = pow(2, l - 1)
	vec = [[] for i in range(l)]
	for i in range(1, leafNodeCount + 1):
		vec[l - 1].append(i)
	for i in range(l - 2, -1, -1):
		k = 0
		while (k < len(vec[i + 1]) - 1):
			vec[i].append(vec[i + 1][k] +
						vec[i + 1][k + 1])
			k += 2
	Sum = 0
	for i in range(l):
		for j in range(len(vec[i])):
			Sum += vec[i][j]
	return Sum
if __name__ == '__main__':
	l = 3
	print(SumNodes(l))
 
