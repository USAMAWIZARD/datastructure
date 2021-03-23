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
struct node * getpriviousaddress(int);
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

int delete(int todelete){
    struct node *i=first;
    if(first==last){
    first=last=NULL;
    return 0;
    }
    if(first->data ==todelete){
       first=first->next;
       return 0;
    }
    i=getpriviousaddress(todelete);
    if(i==last){
        printf("element not presenet in the linked list");
        return 0;
    }
    if(i->next ==last){
        last=i;
        return 0;
    }
    i->next=i->next->next;



}
struct node * getpriviousaddress(int todelete){
    struct node *i=first;

    while (i->next->data!=todelete)
    {  
        i=i->next; 
    }
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
    {   printf("\n1.insert\n2.delete\n3.display\n4.exit");
        scanf("%d",&choice);
        switch (choice)
        {
        case 1:
            printf("\nenter the value to insert");
            scanf("%d",&value);
            insert(value);
            break;
        case 2:
            printf("\nenter the value to delete\n");
            scanf("%d",&value);
            delete(value);
            break;
        case 3:
            display();
            break;
        case 4:
            exit(0);
    
        }
    }
    

}
