def recusive(input):
	if input<=0:
		return input
	else:
		print("0")
		output=recusive(input-1)
		print(input)
		return output
recusive(3)