#include<stdio.h>
#include<math.h>

typedef struct point
{
    int X;
    int Y;

} Point;


double calculateDistance(Point *point1, Point *point2) 
{

    double distance = sqrt( (point2->X - point1->X)*(point2->X - point1->X) + (point2->Y - point1->Y)*(point2->Y - point1->Y) ); 
    return distance;
}


int main(){
    Point P1,P2,P3;
    scanf("%d %d\n",&P1.X,&P1.Y);
    scanf("%d %d",&P2.X,&P2.Y);
    printf("%.2lf", calculateDistance(&P1,&P2));
    return 0;
}
