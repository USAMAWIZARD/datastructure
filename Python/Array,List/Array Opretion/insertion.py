list=[1,2,3,4]
pos=int(input("at which position you want to insert an element"))
element=int(input("what element you want to insert at positon "+str(pos)))
i=len(list)-1
list.append(None)
while(pos<=i):
	list[i+1]=list[i]
	i-=1
list[pos]=element
print(list)
