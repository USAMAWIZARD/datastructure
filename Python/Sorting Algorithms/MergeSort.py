numbers=[6,9,3,2,2,1,2,3]
print("len of nubers",len(numbers))
def sortit(low,up):
	if numbers[low]>numbers[up]:
		temp=numbers[low]
		numbers[low]=numbers[up]
		numbers[up]=temp
def mergeit(low,up):
	pass
def MergeSortDivide(up,low):
	if up-low<=1:
		print("sort it",low,up)
		sortit(low,up)
		return up+1
	else:
		lower=MergeSortDivide((up+low)//2,low)
		mergeit=MergeSortDivide(up,lower)	
		mergeit(low,mergeit-1)
		return up+1
print(numbers)
MergeSortDivide(len(numbers)-1,0)
print(numbers)
