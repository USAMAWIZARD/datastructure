numbers=[1,2,3,4,5]
tosearch=int(input("which number to search"))
high=len(numbers)
low=0


while(low!=high):
	mid=(low+high)//2
	if numbers[mid]==tosearch:
		print("element ",tosearch,"found at", mid)
		break
	if tosearch>mid:
		low=mid+1
	else:
		high=mid-1
	print("i")


if low==high:
	print("element not present in the list")