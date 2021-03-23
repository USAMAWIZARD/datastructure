list=[1,2,3,4,5,6,7]
print(list)
pos=int(input("enter the postion of element you want to delete"))
i=pos
while(i<len(list)-1):
	list[i]=list[i+1]
	i+=1
print(list)