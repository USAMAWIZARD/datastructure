numbers=[6,4,2,1]

def QuickSort(intial,end):
    global numbers
    if intial-end==0:
        return 1

    pivot=numbers[len(numbers[intial:end])]
    pivotpos=len(numbers[intial:end])
    i=intial
    while i<=end:
        print(numbers)
        print(intial,end)
        print("pivot",pivot)
        print("pivotpos",pivotpos)
        print("****************************")
        if numbers[i]>pivot:
            topush=numbers[i]
            del numbers[i]
            numbers.append(topush)
            pivotpos-=1
            i-=1
        i+=1

    print("this loop is over ",pivotpos-1)
    QuickSort(0,pivotpos-1)

QuickSort(0,len(numbers)-1)
