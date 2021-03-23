class Tree:
    tree=100*[None] 
    tree=[1,2,3,4,5,None,None,None,None,9,10,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
    def __init__(self):
        #self.tree[0]=int(input("enter the value of root node "))
        pass
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
    
            childnodes=newchildnodes.copy()
            newchildnodes=[]
    def postordertraversal(self,pos,wnode):
        if (pos*2)+1<=len(self.tree):
            if self.tree[(pos*2)+1]!=None: 
                pos=self.postordertraversal((pos*2)+1,'l')
                #area
                #print("asfsdf",self.tree[pos])
                if (pos*2)+2<=len(self.tree):
                    if self.tree[(pos*2)+2]!=None: 
                        pos=self.postordertraversal((pos*2)+2,'r')
                        print(self.tree[pos])
                if wnode=='r':
                    return (pos-2)//2
                else:
                    return (pos-1)//2    
                #area
                
            else:
                print(self.tree[pos])
                if wnode=='l':
                    return (pos-1)//2    
                else:
                     return (pos-2)//2   



        


t=Tree()



while True:
    option=int(input("1.insert\n2.delete\n3.display\n4.post order traversal\n5.exit"))
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
        t.postordertraversal(0,'n')
    if option==5:
        exit()