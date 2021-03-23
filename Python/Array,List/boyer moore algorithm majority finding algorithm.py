array=[int(i) for i in input("enter the element of the array").split()]
count=0
majoritycandidate=array[0]
for i in array:
    if i==majoritycandidate:
        count+=1
    else:
        count-=1
    if count==0:
        majoritycandidate=i
print(majoritycandidate)
count=0
for i in array:
    if i==majoritycandidate:
        count+=1
if count//2:
    print(majoritycandidate,' is the majority element in the array')
else:
    print("there is no majority element in the array")