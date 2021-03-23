numbers=[6,9,3,2,2,2,1,2,3]
print("len of nubers",len(numbers))
def MergeSortDivide(up,low):
	if up-low<=1:
		print("ss",low,up)
		return up+1
	else:
		print("ww",low,up)
		lower=MergeSortDivide((up+low)//2,low)
		print("asdf",lower,up)
		if up==len(numbers)-1 and up-lower>=1:
			MergeSortDivide(up,lower)
		return up+1

MergeSortDivide(len(numbers)-1,0)

