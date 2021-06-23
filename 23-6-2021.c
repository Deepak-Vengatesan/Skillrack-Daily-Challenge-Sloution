#include<stdio.h>
#include<stdlib.h>

typedef struct time
{
    int hh, mm, ss;
} Time;

Time* addSeconds(Time *time, int X)
{
    Time *newTime = (Time*)malloc(sizeof(Time));
    newTime->ss = (time->ss+X)%60;
    newTime->mm = (time->mm + (time->ss+X)/60)%60;
    newTime->hh = (time->hh + (time->mm +(time->ss+X)/60)/60)%24;
    return newTime;

}

int main(){
    Time *time = (Time*)malloc(sizeof(Time));
    scanf("%d:%d:%d", &time->hh, &time->mm, &time->ss);
    int X;
    scanf("%d",&X);
    Time *newTime = addSeconds(time,X);
    printf("Old Time:\n");
    printf("%02d:%02d:%02d", time->hh, time->mm, time->ss);
    printf("\nNew Time:\n");
    printf("%02d:%02d:%02d",newTime->hh,newTime->mm, newTime->ss);
    return 0;
}