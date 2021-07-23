#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct BoundedArray
{
    int SIZE;
    char **words;
 
} boundedArray;

boundedArray* getEvenLengthWords(char str[])
{
    boundedArray *bArr = malloc(sizeof(boundedArray));
    bArr->words = malloc(sizeof(char*)*1001);
    for(int index =0; index < 1001; index++){
        bArr->words[index] = malloc(sizeof(char)*1001);
    }
    bArr->SIZE = 0;
    char *tok = strtok(str," ");
    while(tok != NULL)
    {
        if(strlen(tok)%2 == 0)
        {
            bArr->words[bArr->SIZE] = malloc(sizeof(char)*1001);
            strcpy(bArr->words[bArr->SIZE++],tok);

        }
        tok = strtok(NULL," ");
    }
    if(bArr->SIZE == 0){
        // store -1;
        strcpy(bArr->words[bArr->SIZE++],"-1");
    }
    return bArr;
}

int main(){
    char str[1001];
    scanf("%[^\n]",str);

    boundedArray *bArr = getEvenLengthWords(str);
    printf("Even Length Wrods:\n");
    for(int index= 0; index < bArr->SIZE; index++){
        printf("%s\n", bArr->words[index]);
    }

    return 0;
}