#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int val;
    struct Node *prev, *next;
};

struct Node* getBinaryRepresentation(int N)
{
    int arr[101], arrLen = 0;
    while(N>0)
    {
        arr[arrLen++] = N%2;
        N /= 2;
    }
    struct Node *head = NULL, *tail = NULL;
    for(int ctr= arrLen-1; ctr >= 0; ctr--){
        struct Node *newnode = (struct Node*)malloc(sizeof(struct Node));
        newnode->next = NULL;
        newnode->prev = NULL;
        newnode->val = arr[ctr];
        if(head == NULL)
        {
            head = newnode;
            tail = newnode;
        }
        else{
            newnode->prev = tail;
            tail->next = newnode;
            tail = tail->next;
        }
    }
    return head;

}

void display(struct Node *head)
{
    struct Node *ptr = head;
    while(ptr != NULL)
    {
        printf("%d",ptr->val);
        ptr = ptr->next;
    }
}

void displayReverse(struct Node *head)
{
    struct Node *ptr = head, *prev;
    while(ptr != NULL)
    {
        prev = ptr;
        ptr = ptr->next;
    }
    ptr = prev;
    while(ptr != NULL)
    {
        printf("%d", ptr->val);
        ptr = ptr->prev;
    }
}

int main(){
    int N;
    scanf("%d",&N);
    struct Node *head = getBinaryRepresentation(N);
    printf("DLL: ");
    display(head);
    printf("\nReverse DLL: ");
    displayReverse(head);
    return 0; 
}