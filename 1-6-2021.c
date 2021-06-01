#include<stdio.h>
#include<stdlib.h>

void toggle(int *val);

void invertSubmatrix(int R, int C, int matrix[R][C], int sRow, int sCol,int K){
    sRow-=1,sCol-=1,K-=1;
    for(int i=sRow; i<=sRow+K; i++){
        for(int j=sCol; j<=sCol+K; j++){
             toggle(&matrix[i][j]);
         }
    }
}


void toggle(int *val){
    if(*val == 0){
        *val = 1;
    }
    else{
        *val = 0;
    }
}


int main(){
    int R,C,K,sRow,sCol;
    scanf("%d %d",&R,&C);
    int matrix[R][C];
    for(int row=0; row<R; row++){
        for(int col=0; col<C; col++){
            scanf("%d", &matrix[row][col]);
        }
    }
    scanf("%d %d\n%d",&sRow,&sCol,&K);
    invertSubmatrix(R ,C, matrix, sRow, sCol, K);
    for(int row=0; row<R; row++){
        for(int col=0; col<C; col++){
            printf("%d ",matrix[row][col]);
        }
        printf("\n");
    }
    return 0;

}



/**
 

 5 6
 0 1 0 1 0 0 
 0 1 1 0 0 0
 1 1 0 0 1 0
 1 1 0 1 0 0
 0 1 1 1 0 0
 2 3
 3

 6 4
 0 0 1 0
 0 1 0 0
 1 1 0 1
 1 1 1 1
 0 0 0 1
 1 1 0 0
 3 1
 4

 **/