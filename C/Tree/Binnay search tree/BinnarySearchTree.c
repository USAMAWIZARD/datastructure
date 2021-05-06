#include <stdio.h>
#include <conio.h>
#include <process.h>
#include <stdlib.h>
struct node
{
    int data;
    struct node *right;
    struct node *left;
};

struct node *Root = NULL;
void initStruct(struct node *ptr)
{
    ptr->right=NULL;
    ptr->left =NULL;
}
void insert(int toinsert)
{
    struct node *i = Root;
    struct node *ptr = (struct node *)malloc(sizeof(struct node));
    initStruct(ptr);
    ptr->data = toinsert;
    if (Root == NULL)
    {   printf("sdfs");
        Root = ptr;
        return;
    }

    while (1)
    {
        printf("%d\n", i->data);
        if (toinsert > i->data)
        {
            i = i->left;
            if (i == NULL )
            {
                printf("left");
                 i = ptr;
                return;
            }

        }
        else
        {
        
            i= i->right;
            if (i == NULL)
            {   printf("right");
                i = ptr;
                return;
            }
        }
    }
}
void display()
{
    printf("%d",Root->right);
}
int main()
{
    int choice;
    int value;
    while (1)
    {
        printf("\n1.insert\n3.display\n4.revse\n5.exits");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("\nenter the value to insert");

            scanf("%d", &value);
            insert(value);
            break;
        case 3:

            display();
            break;
        case 4:

            break;
        case 5:
            exit(0);
        }
    }
}
