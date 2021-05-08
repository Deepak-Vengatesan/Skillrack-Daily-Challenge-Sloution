#include<stdio.h>
#include<stdlib.h>

int indexof(char ch,char str[]){
    for(int i=0;i<strlen(str);i++){
        if(ch == str[i]) return i;
    }
}

int main(){
    char firstHalf[] = "abcdefghijklm";
    char secondHalf[] = "nopqurstuvwxyz";
    char str[101];
    while(scanf("%s ",str) == 1){
        for(int i=0;i<strlen(str);i++){
            char ch=str[i];
            ch=tolower(ch);
            if(ch <= 'm'){
                int index = indexof(ch,firstHalf);
                char op = secondHalf[index];
                printf("%c",isupper(str[i]) ? toupper(op) : op);
            }
            else{
                int index = indexof(ch,secondHalf);
                char op = firstHalf[index];
                printf("%c",isupper(str[i]) ? toupper(op) : op);
            }
        }
        printf(" ");
    }
    return 0;
}