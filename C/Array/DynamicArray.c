#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
int *ptr;
int last = -1;
int size = 10;

void insert()
{
    int index;
    printf("enter index to insert\n");
    scanf("%d", &index);
    printf("enter the valut to insert\n");
    scanf("%d", ptr + index);
    last++;
}
void at(int index)
{   if(index>size-1){
    printf("\nindex out of bound\n");
    return;
}
    printf("%d\n", *(ptr + index));
}
void pop()
{
    at(last);
    last--;
}
int find()
{
    int tofind;
    printf("enter the element to fild\n");
    scanf("%d", &tofind);
    for (int *i = ptr; i < ptr + 9; i++)
    {
        if (*i == tofind)
        {
            printf("%d is present at inded %u", *(i), i);
            return 0;
        }
    }
}
int sizeofarray()
{
    printf("");
}
int capacity()
{
    printf("%d", size);
}
int resize()
{
    int size;
    printf("enter the resizing values\n");
    scanf("%d", &size);
    ptr = realloc(ptr, size * sizeof(int));
}
int push()
{
    last++;
    printf("enter the value to insert\n");
    scanf("%d", &ptr + last);
}
//int delete(){}
//int remove(){}

void main()
{
    int choice;
    int index;
    int size = 10;
    ptr = (int *)malloc(size * sizeof(int));
    //initialize
    int i = 0;
    while (i != size)
    {
        *(ptr+i)=NULL;
        i++;
    }
    while (1)
    {
        printf("\n 1.insert \n 2.at \n 3.pop \n 4.find \n 5.size \n 6.capacity \n 7.prepend \n 8.remove \n 9.delete \n 10.push \n 11.resize");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            insert();
            break;
        case 2:
            printf("enter the index you want to access");
            scanf("%d", &index);
            at(index);
            break;
        case 3:
            pop();
            break;
        case 4:
            find();
            break;
        case 5:
            sizeofarray();
            break;
        case 6:
            capacity();
            break;
        case 7:
            //   prepend();
            break;
        case 8:
            // remove();
            break;
        case 9:
            //   delete();
            break;
        case 10:
            push();
            break;
        case 11:
            resize();
            break;
        }
    }
}