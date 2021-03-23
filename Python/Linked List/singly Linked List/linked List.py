class LinkedList():
	def __init__(self):
		self.head=None
		self.last=None
		
	def insert_at_End(self,data):
		if self.head==None:
			self.head=self.last=Node(data)
		else:
			print(self.head,self.last)
			address=Node(data)
			self.last.next=address
			self.last=address

	def insert_at_Begining(self,data):
		if self.head==None:
			self.head=self.last=Node(data)
		else:
			address=Node(data)
			address.next=self.head
			self.head=address

	def insert_in_mid(self,data,element):
		if self.head==None:
			self.head=self.last=Node(data)
		else:
			new=Node(data)
			address=self.search(element)
			previous=self.previousaddress(address)
			previous.next=new
			new.next=address
	def search(self,element):
		i=self.head
		while(i.data!=element):
			i=i.next

		return i
	def previousaddress(self,address):
		i=self.head
		while(i.next!=address):
			i=i.next
		return i
	def delete(self,element):
		address=self.search(element)
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
		
ls=LinkedList()
ls.insert_at_Begining(1)
ls.insert_at_Begining(2)
ls.insert_at_Begining(3)
ls.insert_at_Begining(4)
ls.display()
ls.insert_in_mid(8,2)

ls.display()