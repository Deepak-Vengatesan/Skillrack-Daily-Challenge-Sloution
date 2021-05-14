#include<stdio.h>
#include<stdlib.h>

vodi printMatrix(int R, int C, int matrix[][C]){
    for(int row = 0; row <R; row++){
        for(int col = 0; col<C; col++){
            printf("%d",matrix[row][col]);
        }
        printf("\n");
    }
}

//end of printMatrix function
int** addTwoMatrices(int R, int C, int *matrix1, int *matrix2){
    int **resultMatrix = malloc(R*sizeof(int*)*R);
    int index=0;
    for(int row=0; row<R; row++){
        resultMatrix[row] = malloc(sizeof(int)*C);
        for(int col=0; col<C; col++){
            resultMatrix[row][col] = *(matrix1+index)+ *(matix2+index);
            index++;

        }
    }
    return resultMatrix
}

int main(){
    int R,C;
    scanf("%d %d",&R,&C);
    int matrix1[R][C], matrix2[R][C];
    for(int row=0; row<R; row++){
        for(int col=0; col<C; col++){
            scanf("%d", &matrix1[row][col]);
        }
    }
    for(int row=0; row<R; row++){
        for(int col=0; col<C; col++){
            scanf("%d", &matrix2[row][col]);
        }
    }
    int **resultMatrix = addTwoMatrices(R,C,matrix1,matrix2);
    printf("Matrix 1: \n");
    printMatrix(R,C,matrix1);
    printf("Matrix 2: \n");
    printMatrix(R,C,matrix2);
    printf("Matrix sum: \n");
    for(int row=0; row<R; row++){
        for(int col=0; col<C; col++){
            printf("%d ",resultMatrix[row][col]);
        }
        printf("\n");
    }
    return 0;
    //end of main function
}