#include <stdio.h>
#include <stdlib.h>

char* getCommaSeparatedValues(int SIZE, int arr[])
{
    char* str = malloc(sizeof(char)*100);
    strcat(str,"");
    for(int i=0; i<SIZE; i++){
        char num[10];
        sprintf(num,"%d",arr[i]);
        strcat(str,num);       
        if(i!=SIZE-1){
            strcat(str,",");
        }
    }
    return str;
}

int main(){
    int N;
    scanf("%d",&N);
    int arr[N];
    for(int index=0; index<N; index++){
        scanf("%d",&arr[index]);
    }
    char *ptr = getCommaSeparatedValues(N, arr);
    printf("CSV: %s", ptr);
    return 0;
}