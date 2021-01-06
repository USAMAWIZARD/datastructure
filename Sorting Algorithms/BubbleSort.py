numbers=[9,6,24,1,412,41,4]




for i in range(0,len(numbers)):
    for j in range(0,len(numbers)-i-1):
        if numbers[j]<numbers[j+1]:
            temp=numbers[j]
            numbers[j]=numbers[j+1]
            numbers[j+1]=temp
print(numbers)
