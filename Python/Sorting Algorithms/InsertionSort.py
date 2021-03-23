numbers=[2341,3,5,26,1,6,2,7]

for i in range(len(numbers)):
    for j in range(0,i):
        if numbers[j]>numbers[i]:
            toinsert=numbers[i]
            del numbers[i]
            numbers.insert(j,toinsert)
print(numbers)