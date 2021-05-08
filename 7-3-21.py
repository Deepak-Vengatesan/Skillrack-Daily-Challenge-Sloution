R,C = map(int,input().split())
M1=[list(input().split())for i in range(R)]
M2=[list(input().split())for i in range(R)]
for i in range(R):
    counter1,counter2 = 0,0
    minimum = min(len(M1[i]),len(M2[i]))
    for j in range(minimum):
        if M1[i][counter1] == M2[i][counter2]:
            print(M1[i][counter1],end=" ")
            counter1+=1
            counter2+=1
        elif M1[i][counter1] != M2[i][counter2] and counter1 != minimum and counter2!= minimum:
            print("-1",end=" ")


