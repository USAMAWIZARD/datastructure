
class Queue():
	def __init__(self):
		self.head=None
		self.last=None
		
	def insert(self,data):
		if self.head==None:
			self.next=self.head=self.last=Node(data)
		else:
			address=Node(data)
			address.next=self.head
			self.head=address
			self.last.next=address
		
	def previousaddress(self,address):
		i=self.head
		while(i.next!=address):
			i=i.next
		return i
	def delete(self):
		if self.head==None:
			print("queue is empty")
		elif self.head ==self.last:
			self.head=self.last=None
		else:
			i=self.previousaddress(self.last)		
			self.last=i
			i.next=None			#delete from begining last
			
	def display(self):
		a=self.head
		while a:
			print(a.data)
			if a==self.last:
				break
			a=a.next
		
		
			
class Node():
	def __init__(self,data):
		self.data=data
		self.next=None
		
Q=Queue()
Q.insert(1)	
Q.insert(2)
Q.insert(3)
Q.insert(4)
Q.delete()
Q.delete()
Q.delete()
Q.delete()
Q.delete()

Q.display()