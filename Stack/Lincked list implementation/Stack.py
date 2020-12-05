class Stack():
	def __init__(self):
		self.head=None
		self.last=None
		self.stackSize=5
		
	def push(self,data):
		if self.head==None:
			self.head=self.last=SNode(data)
		else:
			address=SNode(data)
			self.last.next=address
			self.last=address
		return i
	def previousaddress(self,address):
		i=self.head
		while(i.next!=address):
			i=i.next
		return i
	def pop(self):
		if self.head==None:
			print("Stack underflow")
			return
		if self.head==self.last:
			print(self.head.data," poped out of stack")
			self.head=self.last=None
			return
		print(self.last.data," poped out of stack")
		i=self.previousaddress(self.last)		
		self.last=i
		i.next=None			
		
	def display(self):
		a=self.head
		while a!=None:
			print(a.data)
			a=a.next

class SNode():
	def __init__(self,data):
		self.data=data
		self.next=None
		
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

s.display()