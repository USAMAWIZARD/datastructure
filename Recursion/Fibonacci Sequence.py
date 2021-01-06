fibonacci=[]
a=0
b=1
for i in range(10):
	seq=a+b
	print(seq)
	b=a
	a=seq
	