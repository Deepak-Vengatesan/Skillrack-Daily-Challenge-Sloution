#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct BoundedArray
{
    int SIZE;
    char **words;
} boundedArray;

boundedArray* customSplit(char *str, char delimiter)
{
    boundedArray *bArr = malloc(sizeof(boundedArray));
    bArr->words = malloc(sizeof(char*)*1001);
    for(int index = 0; index<1001; index++){
        bArr->words[index] = malloc(sizeof(char)*1001);
    }
    bArr->SIZE = 0;
    char *ptr = strtok(str,&delimiter);
    while(ptr != NULL){
        strcpy(bArr->words[bArr->SIZE++],ptr);
        ptr = strtok(NULL,&delimiter);
    }
    return bArr;

}

int main(){
    char str[1001], delimiter;
    scanf("%s\n%c",str, &delimiter);
    boundedArray *bArr = customSplit(str,delimiter);
    printf("Words:\n");
    for(int index = 0; index < bArr->SIZE; index++){
        printf("%s\n", bArr->words[index]);
    }
    return 0;
}