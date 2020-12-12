
class Queue:

	def __init__(self):
		self.QueueLen=5
		self.queue=[None]*self.QueueLen
		self.front=-1
		self.rear=-1
	
	def insert(self,element):

		if self.rear==self.QueueLen-1:
			print("queue is full")
			return
		self.rear+=1
		if self.front==-1:
			self.front=0

		self.queue[self.rear]=element
	
	def delete(self):
		if self.front!=-1 and self.rear==self.front:
			self.front=self.rear=-1
			return
		if self.front==-1 and self.rear==-1:
			print("queue is embty")
			return
		self.front+=1

	def display(self):
		if self.front==-1: 
			print("empyt")
			return
		for i in range(self.front,self.rear+1):
			print(self.queue[i])



q=Queue()
	
while True:
	i=int(input("1.insert \n2.delete \n3.display \n0.exit "))
	if i==1:
		element=int(input("enter element to insert in the queue"))
		q.insert(element)
	elif i==2:
		q.delete()
	elif i==3:
		q.display()
	elif i==0:
		break

