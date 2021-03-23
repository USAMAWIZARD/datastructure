class Tree:
    tree=100*[None] 
    def __init__(self):
        self.tree[0]=int(input("enter the value of root node "))
    def insert(self,data,rootnode,pos):
        if self.tree[rootnode]==None:
            print("no root node present at this location")
        elif self.tree[(2*rootnode)+pos]!=None:
            print("element already present at this position")
            return
        else:
            self.tree[(2*rootnode)+pos]=data
    def delete(self,elementpos):
        self.tree[elementpos]=None
        if self.tree[2*elementpos+1]!=self.tree[2*elementpos+2]:
            self.tree[2*elementpos+1]=self.tree[2*elementpos+2]=None
            self.delete(2*elementpos+1)
            self.delete(2*elementpos+2)
        else:
            return
    def display(self):
        childnodes=[0]
        newchildnodes=[]
        while childnodes!=[]:
            for i in  childnodes:
                print(i,end="")
                if i=="":
                    print("-",end="")
                else:
                    print(i)
                    if self.tree[2*i+1]:
                        newchildnodes.append(2*i+1)
                    elif self.tree[2*i+2]:
                        newchildnodes.append(2*i+2)
                    else:
                        newchildnodes.append(" ")
            print(" hi")
            childnodes=newchildnodes.copy()
            newchildnodes=[]

t=Tree()
while True:
    option=int(input("1.insert\n2.delete\n3.display\n4.exit"))
    if option==1:
        data=int(input("enter data to insert"))
        rootnode=int(input("enter postion of root node for the node"))
        pos= input("enter R or L")
        if pos=="R"or pos=='r':
            pos=2
        elif pos=='L' or pos=='l':
            pos=1
        t.insert(data,rootnode, pos)
    if option ==2:
        t.delete(int(input("enter the node location")))
    if option==3:
        t.display()
    if option==4:
        exit()