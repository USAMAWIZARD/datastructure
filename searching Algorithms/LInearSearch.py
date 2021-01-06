numbers=[1,9,4,9,2,5]

toserarch=int(input("which number to search"))	
for i in range(len(numbers)):
	if numbers[i]==toserarch:
		print("number ",toserarch,"found at",i,"position")
		break

if i==len(numbers)-1:
	print("element not present in the list")
