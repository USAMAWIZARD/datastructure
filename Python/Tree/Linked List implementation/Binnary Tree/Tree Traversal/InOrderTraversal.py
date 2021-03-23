 #genral tree implementation 
class Tree:
    Root=None
    toSearch=None
    locy=0
    def __init__(self):
        self.Root=Node(int(input("enter the value of root node")))

    def insert(self,value,rootnode,pos):
        address=self.getAddress(rootnode)
        if address==None:
            return
        if pos=="R"or pos=='r':
            address.right=Node(value)
        elif pos=='L' or pos=='l':
            address.left=Node(value)


    def getAddress(self,tofind):
        address=self.Root
        try:
            for i in range(len(tofind)-1):
                if int(tofind[i+1])=='l' or int(tofind[i+1])=='L':
                    address=address.left
                if int(tofind[i+1])=='r' or int(tofind[i+1])=='R':
                    address=address.right          
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
        address=address.right
        if childnodes==None:
            return      
            print(i.data,end="")
            childnodesarray=childnodesarray+i.childs
        print("")
        self.display(address)
        
class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None
t=Tree()


while True:
    option=int(input("1.insert\n2.delete\n3.display\n4.exit"))
    if option==1:
        data=int(input("enter data to insert"))
        rootnode=input("enter postion of root node for the node")
        pos= input("enter R or L")
        t.insert(data,rootnode, pos)
    if option ==2:
        t.delete(int(input("enter the node location")))
    if option==3:
        t.display()
    if option==4:
        exit()
