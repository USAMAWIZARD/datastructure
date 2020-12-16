class Queue():
	def __init__(self):
		self.head=None
		self.last=None
		
	def insert(self,data):
		if self.head==None:
			self.head=self.last=Node(data)
		else:
			address=Node(data)
			address.next=self.head
			self.head=address

		
	def previousaddress(self,address):
		i=self.head
		while(i.next!=address):
			i=i.next
		return i
		
	def delete(self):
		if self.head==None:
			print("queue is empty")
		if self.head==self.last:
			self.head=self.last=None
		else:
			i=self.previousaddress(self.last)
			self.last=i
			i.next=None			#delete from begining last
			
	def display(self):
		a=self.head
		while a!=None:
			print(a.data)
			a=a.next
			
class Node():
	def __init__(self,data):
		self.data=data
		self.next=None
		
q=Queue()
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.delete()
q.delete()

q.display()