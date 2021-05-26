#include<stdio.h>
#include<stdlib.h>

typedef struct BoundedArray
{
    int SIZE;
    int *arr;
} boundedArray;

boundedArray* getColumn(int R,int C,int  matrix[][C],int K){
  int arr[10001],len=0;
  for(int i=0; i<R; i++){
      for(int j=0; j<C; j++){
          if(j == K-1){
              arr[len++] = matrix[i][j];
          }
      }
  }
  boundedArray bArr,*ptr  = &bArr;
    //store the array and len in bArr
    bArr.SIZE = len;
    bArr.arr = arr;
   
    return ptr;
}

int main(){
    int R,C,K;
    scanf("%d %d",&R,&C);
    int matrix[R][C];
    for(int row=0; row<R; row++){
        for(int col=0; col<C; col++){
            scanf("%d",&matrix[row][col]);
        }
    }
    scanf("%d", &K);
    boundedArray *bArr = getColumn(R,C,matrix,K);
    printf("Column %d: ",K);
    for(int index=0; index<bArr->SIZE; index++){
        printf("%d ",bArr->arr[index]);
    }
    return 0;
}




/** 
 5 4
 98 62 65 28
 37 47 14 89
 37 47 14 89
 19 66 48 43
 84 16 75 35
 62 88 77 94
 3
 **/