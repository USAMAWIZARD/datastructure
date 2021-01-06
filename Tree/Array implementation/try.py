def recurse(i):
    if i==10:
        return i
    i+=1
    recurse(i)
    print(i)
recurse(1)