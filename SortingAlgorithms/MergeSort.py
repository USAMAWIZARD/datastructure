numbers=[9,6,3,3]

def MergeSort(numlist):
    global numbers
    if len(numlist)<=2:
        return numlist
    else:
        newlist=numbers[0:len(numlist)//2]
        return MergeSort(newlist)

print(MergeSort(numbers))
