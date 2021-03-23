Array1 =[[1,2,3],[1,2,3],[1,2,3]]
Result =[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(Array1)):
	for j in range(len(Array1)):
		Result[i][j]=Array1[j][i]
print(Result)