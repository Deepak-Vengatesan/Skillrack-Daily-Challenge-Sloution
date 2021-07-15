#include <stdio.h>
#include <stdlib.h>
#include<string.h>

void findTotalMarks(char *file1name, char *file2name){
    FILE *fpNames = fopen(file1name,"r"), *fpMarks = fopen(file2name,"r");
    char names[101][101];
    int marks[101],index = 0;
    while(1){
        int mark1,mark2,mark3;
        fscanf(fpNames,"%s",names[index]);
        fscanf(fpMarks,"%d %d %d",&mark1,&mark2,&mark3);
        marks[index++] = mark1+mark2+mark3;
        char ch = fgetc(fpNames);
        if(ch == EOF){
            break;
        }
    }
    FILE *fp = fopen(file1name, "w");
    for(int ind = 0; ind<index; ind++ ){
        fprintf(fp,"%s %d\n",names[ind],marks[ind]);
    }
    fclose(fp);
}


void printFileContent(char *filename){
    FILE *fp = fopen(filename,"r");
    char ch;
    while((ch = fgetc(fp)) != EOF)
    {
        printf("%c", ch);
    }
    fclose(fp);
} 

int main(){
    char file1name[31], file2name[31];
    scanf("%s\n%s", file1name, file2name);
    findTotalMarks(file1name,file2name);
    printf("Studnets and Total Marks:\n");
    printFileContent(file1name);
    return 0;
}