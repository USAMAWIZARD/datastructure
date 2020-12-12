array1=[[1,2,3],[1,2,3],[1,2,3]]
array2=[[1,2,3],[1,2,3],[1,2,3]]
array3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(array1)):
	for a in range(len(array2)):
		for b in range(len(array2)):
			array3[i][a]=array3[i][a]+array1[a][b]*array2[b][a]
print(array3)