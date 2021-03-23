#include<stdio.h>
#include<conio.h>
#include<process.h>
#include<stdlib.h>
struct  node
{
    int data;
    struct node *next;
    
};


struct node * first=NULL;
struct node * last=NULL;
struct node *getpriviousaddress(struct node *);
int insert(int toinsert){
    struct node * ptr = (struct node*) malloc(sizeof(struct node));
    ptr->data=toinsert;
    if(first==NULL){
        first=last=ptr;
        ptr->next=NULL;
        return 0;
    }
    if(first==last){
        first->next=ptr;
        last=ptr;
        last->next=NULL;
        return 0;
    }
    last->next=ptr;
    last=ptr;
    last->next=NULL;
    
}
void reverse(){
struct  node * i=last;
struct  node  * start=last;
struct  node * end=last;    

while(start!=first)
{

i=getpriviousaddress(start) ; 
start->next=i;
start=i;

}
first=end;
 last=start;
}

struct node * getpriviousaddress(struct node *previousof){
    struct node *i=first;
  
    while (i->next!=previousof)
    {  
        i=i->next; 
    }
  //  printf("%d",i->data);
    return i;
}
void display(){

    struct node *i=first;
    if(first!=NULL)
    while (1)
    {  
        printf("%d",i->data);
        if(i==last )
        break;
        i=i->next;
        
    }
    
}
int main(){
    int choice;
    int value;
    while (1)
    {   printf("\n1.insert\n3.display\n4.revse\n5.exits");
        scanf("%d",&choice);
        switch (choice)
        {
        case 1:
            printf("\nenter the value to insert");
            scanf("%d",&value);
            insert(value);
            break;
        case 3:

            display();
            break;
        case 4:
           
            reverse();
            break;
        case 5:
            exit(0);
    
        }
    }
    

}
