class LinkedList():
	def __init__(self):
		self.head=None
		self.last=None
		
	def insert_at_End(self,data):
		if self.head==None:
			self.head=self.last=Node(data)
			self.previous=None
		else:
			print(self.head,self.last)
			address=Node(data)
			self.last.next=address
			address.previous=self.last
			self.last=address


	def insert_at_Begining(self,data):
		if self.head==None:
			self.head=self.last=Node(data)
			self.previous=None
		else:
			address=Node(data)
			self.head.previous=address
			address.previous=None
			address.next=self.head
			self.head=address

	def insert_in_mid(self,after,value):#data=pos element=value to insert
		if self.head==None:
			self.head=self.last=Node(value)
			self.previous=None
		else:
			new=Node(value)
			address=self.search(after)
			new.next=address.next
			address.next=new
			new.previous=address
			new.next.previous=new

		
	def search(self,element):
		i=self.head
		while(i!=None):
			if(i.data==element):
				return i
			i=i.next
	def delete(self,element):
		address=self.search(element)
		
		if self.last==self.head==address:
			self.head=self.hsead=None
		elif self.head==address:
			self.head=self.head.next		#delete from begining
			self.head.previous=None
		else:
			i=address.previous
			if address==self.last:			
				self.last=i
				i.next=None			
			else:
				i.next=address.next				#delete from mid
				address.next.previous=i
			
	def display(self):
		a=self.head
		while a!=None:
			print(a.data)
			a=a.next
			
class Node():
	def __init__(self,data):
		self.data=data
		self.previous=None
		self.next=None
		
ls=LinkedList()
ls.insert_at_Begining(1)
ls.insert_at_Begining(2)
ls.insert_at_Begining(3)
ls.insert_at_End(7)

ls.insert_in_mid(2,4)

print("before deleting")
ls.display()

ls.delete(7)
print("after deletings")
ls.display()
