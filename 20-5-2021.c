#include<stdio.h>
#include<stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

boundedArray* getArrayFromMatrix(int R, int C, int matrix[][C])
{
    int arr[10001],len=0;
    for(int i=R-1; i>=0; i--){
        for(int j=C-1; j>=0; j--){
            arr[len++] = matrix[i][j];
        }
    }
    boundedArray bArr,*ptr  = &bArr;

    bArr.SIZE = len;
    bArr.arr = arr;
   
    return ptr; 
}

int main(){
    int R,C;
    scanf("%d %d",&R,&C);
    int matrix[R][C];
    for(int row=0; row<R; row++){
        for(int col=0; col<C; col++){
            scanf("%d", &matrix[row][col]);
        }
    }
    boundedArray *bArr = getArrayFromMatrix(R, C, matrix);
    printf("Matrix:\n");
    for(int row=0; row<R; row++){
        for(int col=0; col<C; col++){
            printf("%d ",matrix[row][col]);
        }
        printf("\n");
    }
    printf("Array: ");
    for(int index=0; index<bArr->SIZE; index++){
        printf("%d ",bArr->arr[index]);
    }
    return 0;
}
