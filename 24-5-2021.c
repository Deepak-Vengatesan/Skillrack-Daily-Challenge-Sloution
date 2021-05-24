#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int customCompare(char str1[], char str2[]){
    char S1[101],S2[101];
    int l=0, k=0;
    int maxLen = strlen(str1)>strlen(str2) ? strlen(str1) : strlen(str2);
    for(int i=0; i<maxLen; i++){
        if(i<strlen(str1) && isupper(str1[i])){
            S1[l++] = str1[i];
        }
        if(i<strlen(str2) && isupper(str2[i])){
            S2[k++] = str2[i];

        }
    }
    S1[l] = '\0';
    S2[k] = '\0';
    if(strcmp(S1,S2) == 0){
        return 1;
    }
    else{
        return 0;
    }

}
int main(){
    char str1[101],str2[101];
    scanf("%s\n%s",str1,str2);
    printf("%d", customCompare(str1,str2));
    return 0;
}