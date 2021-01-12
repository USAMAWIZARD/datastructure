#genral tree implementation 
class Tree:
    Root=None
    def __init__(self):
        self.Root=Node(int(input("enter the value of root node")))

    def insert(self,value,rootnode):
        address=self.getAddress(rootnode)
        if address==None:
            return
        address.childs.append(Node(value))

    def getAddress(self,tofind):
        address=self.Root
        try:
            for i in range(len(tofind)-1):
                address=address.childs[int(tofind[i+1])]
        except:
            print("no root node exist of address specified")
            return None
        return address

    def delete(self,delloc):
        previousnode=self.getAddress(delloc[:len(delloc)-1])
        if previousnode==None:
            return
        del previousnode.childs[int(delloc[-1])]

    def display(self,childnodes):
        if childnodes==[]:
            return
        childnodesarray=[]
        for i in childnodes:
            print(i.data,end="")
            childnodesarray=childnodesarray+i.childs
        print("")
        self.display(childnodesarray)
class Node:
    data=None
    childs=[]
    def __init__(self,value):
        self.data=value
        self.childs=[]
t=Tree()
t.insert(1,"0")
t.insert(2,"0")
t.insert(3,"0")


while True:
    option=int(input("1.insert\n2.delete\n3.display\n4.exit"))
    if option==1:
        data=int(input("enter data to insert"))
        rootnode=input("enter postion of root node for the node")
        t.insert(data,rootnode)
    if option==2:
        t.delete(input("enter the node location"))
    
    if option==3:
        t.display([t.Root])
    if option==4:
        exit() 
