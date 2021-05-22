#include<stdio.h>
char* getUniqueUnitDigits(int SIZE, int arr[]){
    char *uniqueUniqueDigits = malloc(sizeof(char)*SIZE);
    int digits[10] = {0};
    for(int index=0; index<SIZE; index++){
        digits[arr[index]%10]++;
    }
    int index=0;
    for(int num=9; num>=0; num--){
        if(digits[num] != 0){
            uniqueUniqueDigits[index++] = num+'0';

        }

    }
    return uniqueUniqueDigits;
}

int main(){
    int N;
    scanf("%d", &N);
    int arr[N];
    for(int  index=0; index<N; index++){
        scanf("%d",&arr[index]);
    }
    char *str = getUniqueUnitDigits(N,arr);
    printf("Unique Unit Digits: %s", str);
    free(str);
    return 0;
}