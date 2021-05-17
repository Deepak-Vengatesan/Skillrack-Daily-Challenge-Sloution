#include<stdio.h>
#include<stdlib.h>

int main(){
    int N;
    scanf("%d\n",&N);
    for(int ctr=1; ctr<=N; ctr++){
        int sum=0,len=0,num;
        char ch;
        while(1){
            scanf("%d%c",&num,&ch);
            sum+=num;
            len+=1 
            if(ch== '\n' || ch== '\r'){
                break;
            }
        }
        printf("%d %d\n",len,sum);
    }
}