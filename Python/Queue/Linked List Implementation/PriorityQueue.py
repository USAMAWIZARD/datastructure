class Queue():
	def __init__(self):
		self.head=None
		self.last=None
		
	def insert(self,data,priority):
		address=Node(data)
		if self.head==None:
			self.head=self.last=address
		else:
			address.next=self.head
			self.head=address
		address.priority=priority
		
	def previousaddress(self,address):
		i=self.head
		while(i.next!=address):
			i=i.next
		return i
	def getPriority(self):
		i=self.head
		priority=self.head .priority
		address=self.head
		a=self.head
		while a!=None:
			if a.priority>=priority:
				priority=a.priority
				address=a
			a=a.next
		return address
	def delete(self):
		if self.head==None:
			print("queue is empyty")
			return 
		address=self.getPriority()
		if address==self.head:
			self.head=self.head.next		#delete from begining
		elif self.head ==self.last:
			self.head=self.last=None
		else:
			i=self.previousaddress(address)
			if address==self.last:			
				self.last=i
				i.next=None			#delete from begining last
			else:
				i.next=address.next				#delete from mid
			
	def display(self):
		a=self.head
		while a!=None:
			print(a.data)
			a=a.next
			
class Node():
	def __init__(self,data):
		self.data=data
		self.next=None
		self.priority=None
		
q=Queue()
q.insert(1,1)
q.insert(4,4)
q.insert(3,3)
q.insert(2,2)
q.delete()

q.display()