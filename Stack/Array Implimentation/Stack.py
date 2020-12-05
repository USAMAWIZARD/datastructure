
class Stack:
	stack=[None]*5
	pos=-1
	def push(self,element):
		if self.pos==4:
			print("stack overflow")
			return 
		self.pos+=1
		self.stack[self.pos]=element
		
	def pop(self):
		if self.pos==-1:
			print("stack underflow")
		else:
			print("pos",self.pos)
			print(self.stack[self.pos]," poped out from the stack")
			poped=self.stack[self.pos]
			self.stack[self.pos]=None
			self.pos-=1
		 
			
		
	def display(self):
		for element in self.stack:
			print(element)
s=Stack()
while True:
	i=int(input("1.push \n2.pop \n3.display \n0.exit "))
	if i==1:
		element=int(input("enter element to push in the stack"))
		s.push(element)
	elif i==2:
		s.pop()
	elif i==3:
		s.display()
	elif i==0:
		break
		
