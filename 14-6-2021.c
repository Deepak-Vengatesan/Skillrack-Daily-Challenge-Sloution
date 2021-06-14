typedef struct point{
    int X;
    int Y;
} Point;

int getRectangleArea(Point *point1,Point *point2){
    int l,b,area=0;
    l = (point2->X) - (point1->X);
    b = (point2->Y) - (point1->Y);
    area = abs(l*b);
    return area;

}

int main(){
    Point P1,P2,P3;
    scanf("%d %d\n", &P1.X,&P1.Y);
    scanf("%d %d\n", &P2.X,&P2.Y);
    printf("%d",getRectangleArea(&P1,&P2));
    return 0;

}