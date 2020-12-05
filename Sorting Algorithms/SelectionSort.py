numbers=[0,2,3,4,1,51,1235,235,235,235,67236]

for i in range(0,len(numbers)):
    smallerstpos=i
    for j in range(i,len(numbers)):
        if numbers[smallerstpos]>numbers[j]:
            smallerstpos=j    
    temp=numbers[i]
    numbers[i]=numbers[smallerstpos]
    numbers[smallerstpos]=temp  
print(numbers)