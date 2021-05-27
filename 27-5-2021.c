#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void customToUpper(char str[],char fromChar,char toChar){
    int from = fromChar,to = toChar;
    int find=0;
    for(int i=0;i<strlen(str);i++){
        find = str[i];
        if(find>=from && find<=to){
            str[i]=toupper(str[i]);
        }

    }

}


int main(){
    char str[101],fromChar,toChar ;
    scanf("%s\n%c %c",str,&fromChar,&toChar);
    customToUpper(str,fromChar,toChar);
    printf("Modified String: %s",str);
    return 0;
}




/**
 
SkillRack
h p
SKILLRack
 * */