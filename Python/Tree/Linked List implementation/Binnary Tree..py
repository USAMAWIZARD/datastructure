 #genral tree implementation 
class Tree:
    Root=None
    toSearch=None
    locy=0
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
        
    def breadthFirstSearch(self,childnodes):
        if childnodes==[]:
            self.locy=0
            return
        childnodesarray=[]
   
        for i in childnodes:
            if i.data==self.toSearch:
                print("element ",self.toSearch," found at tree depth : ",self.locy)
                self.locy=0
            childnodesarray=childnodesarray+i.childs
        self.locy+=1
        self.breadthFirstSearch(childnodesarray)
class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
t=Tree()


while True:
    option=int(input("1.insert\n2.delete\n3.display\n4.Breadth First Search \n5.exit"))
    if option==1:
        data=int(input("enter data to insert"))
        rootnode=input("enter postion of root node for the node")
        t.insert(data,rootnode)
    if option==2:
        t.delete(input("enter the node location"))
    if option==3:
        t.display([t.Root])
    if option==4:
        t.toSearch= int(input("which element do you want to search"))
        t.breadthFirstSearch([t.Root])
    if option==5:
        exit() 
