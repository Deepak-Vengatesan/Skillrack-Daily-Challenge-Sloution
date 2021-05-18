#include<stdio.h>
#include<stdlib.h>

typedef struct  BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

boundedArray* integerToArray(int N){
    boundedArray *bArr = malloc(sizeof(boundedArray));
    bArr->arr = malloc(sizeof(int)*101);
    bArr->SIZE = 0;
    char num[101];
    int index = 0;
    sprintf(num,"%d",N);
    if(num[0] == '-') 
        index=1;
    for(; index<strlen(num); index++){
        bArr->arr[bArr->SIZE++]=num[index]-'0';
    }
    return bArr;

}

int main(){
    int N;
    scanf("%d",&N);
    boundedArray *bArr = integerToArray(N);
    printf("Array: ");
    for(int index=0; index<bArr->SIZE; index++){
        printf("%d ",bArr->arr[index]);
    }
    return 0;
}
