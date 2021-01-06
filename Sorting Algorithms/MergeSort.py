numbers=[6,9,1,3]


def MergeSort(numlist,up,lower):
	global numbers
	upper=up
	if upper-lower<=2:
		numlist.sort()
		return upper
	else:
		print(lower,upper)
		lower=MergeSort(numbers[lower:upper+1],len(numlist)//2,lower)
		if(lower<len(numbers)):
			MergeSort(numbers[lower:upper+1],lower,upper)

print(MergeSort(numbers,len(numbers),0))
print(numbers)