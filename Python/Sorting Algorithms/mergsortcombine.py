numbers=[6,9,3,2,2,2,1,2,3]

def MergeSortCombine(up,low):
    if up-low<=1:
        print("ss",up,low)
        return up
    else:
        lower=MergeSortCombine((up+low)//2,low)
        print("asdf",lower,up)
        if up==len(numbers)-1 and up-lower>=1:
            MergeSortCombine(up,lower)
        return up	
MergeSortCombine(len(numbers)-1,0)
