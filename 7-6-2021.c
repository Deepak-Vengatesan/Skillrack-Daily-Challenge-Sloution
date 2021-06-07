#include<stdio.h>
#include<stdlib.h>

int** getMatrixFromArrays(int M, int arr1[], int N, int arr2[]){
    int size = sqrt(M+N);
    int **matrix = malloc(sizeof(int)*(101));
    int actr=0,bctr=0;
    for(int i=0; i<size; i++){
        matrix[i] = malloc(sizeof(int)*(101));
        for(int j=0; j<size; j++){
            if(actr != M){
                matrix[i][j]  = arr1[actr++];
            }
            else{
                matrix[i][j] = arr2[bctr++];
            }

        }
    }
    return matrix;

}


int main(){
    int M, N;
    scanf("%d", &M);
    int arr1[M];
    for(int index=0; index<M; index++){
        scanf("%d", &arr1[index]);
    }
    scanf("%d",&N);
    int arr2[N], SIZE = sqrt(M+N);
    for(int index=0; index<N; index++){
        scanf("%d",&arr2[index]);
    }
    int **newMatrix = getMatrixFromArrays(M, arr1, N, arr2);
    printf("Matrix:\n");
    for(int row=0; row<SIZE; row++){
        for(int col=0; col<SIZE; col++){
            printf("%d ",newMatrix[row][col]);
        }
        printf("\n");
    }
    return 0;
}


