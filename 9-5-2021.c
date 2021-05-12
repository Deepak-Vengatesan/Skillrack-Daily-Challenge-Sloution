#include<stdio.h>
#include<stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

boundedArray* getThreeOrFourDigits(int SIZE, int arr[])
{
    boundedArray *bArr = malloc(sizeof(boundedArray));
    bArr->arr= malloc(sizeof(int)*SIZE);
    bArr->SIZE = 0;
    for(int index=0; index<SIZE; index++){
        if((getDigitCount(arr[index])) == 3 || (getDigitCount(arr[index])) == 4){
            bArr->arr[bArr->SIZE++] = arr[index];
        }
    }
    return bArr;
}


int main(){
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int index=0; index<N; index++){
        scanf("%d", &arr[index]);
    }
    boundedArray *bArr = getThreeOrFourDigits(N, arr);
    printf("Old Array: ")
    for(int index=0; index<N; index++){
        printf("%d", arr[index]);
    }
    printf("\nNew Array: ");
    for(int index = 0; index < bArr->size; index++){
        printf("%d", bArr->arr[index]);
    }
    return 0;
}
