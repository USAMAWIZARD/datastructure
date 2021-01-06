def Fibonacci(a,b):
	if b>20:
		return
	else:
		print(a+b) 
		return Fibonacci(a+b,a)		
Fibonacci(0,1)