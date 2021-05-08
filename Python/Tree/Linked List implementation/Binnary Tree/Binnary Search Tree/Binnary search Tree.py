#genral tree implementation 
class Tree:
    Root=None
    toSearch=None
    locy=0
    def __init__(self):
        self.Root=Node(int(input("enter the value of root node")))

    def insert(self,value,i):
        if self.Root==None:
            self.Root=Node(value)
            return
        while True:
            print(i.data,value)
            if value>i.data:
                if i.left==None:
                    print("aaya")
                    i.left=Node(value)
                    return
                else:
                    self.insert(value,i.left)
                    return
            else :
                print("ldd")
                if i.right==None:
                    i.right=Node(value)
                    return
                else:
                    self.insert(value,i.left)
                    return


 

    def delete(self,delloc):
        previousnode=self.getAddress(delloc[:len(delloc)-1])


    def display(self,childnode):
        print(childnode.data)
        if childnode.right!=None:
            self.display(childnode.right)
        else:
            return childnode
        if childnode.left!=None: 
            self.display(childnode.left)
        else:
            return childnode

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
        t.insert(data,t.Root)
    if option ==2:
        print(t.Root.right,t.Root.left)
        #t.delete(int(input("enter the node location")))
    if option==3:

        t.display(t.Root)
    if option==4:
        exit()
