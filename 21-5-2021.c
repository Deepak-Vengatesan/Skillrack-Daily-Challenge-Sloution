#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    int arr[1001];
    char str[10001];
    int len=0,flag=0;
    while(scanf("%[^\n]\n",&str)==1)
    {
        char *token = strtok(str," ");
        int cnt=0;
        while(token!=NULL)
        {
            // store the integer value of token into array
            arr[len++] = atoi(token);
            cnt++;
            token = strtok(NULL," ");
        }
        if(cnt>1) flag=1;
    }
        for(int i=len-1; i>=0; i--){
            printf("%d",arr[i]);
            if(flag==1){
                printf("\n");
            }
            else{
                printf(" ");
            }
    }

}