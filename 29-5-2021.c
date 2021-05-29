#include<stdio.h>
#include<stdlib.h>

void printAlarmTiming(char startTime[],char endTime[],int X){
    int startMM = atoi(&startTime[3]),endMM = atoi(&endTime[3]);
    startTime[2] = '\0'; endTime[2]='\0';
    int startHH = atoi(startTime),endHH = atoi(endTime);
    int startTimeInMins = (startHH*60)+startMM;
    int endTimeInMins = (endHH*60)+endMM;

    startTimeInMins+=X;
    while(startTimeInMins <= endTimeInMins){
        printfTimeFormat(startTimeInMins);
        startTimeInMins+=X;
    }
}

void printfTimeFormat(int Time){
    int HH = Time/60;
    Time = Time - (HH*60);
    int MM = Time;
    printf("%02d:%02d\n",HH,MM);
}
int main(){
    char startTime[6],endTime[6];
    int X;
    scanf("%s\n%s\n%d",startTime,endTime,&X);
    printAlarmTiming(startTime, endTime,X);
    return 0;
}