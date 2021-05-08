s1=input().strip()
s2=input().strip()
count=0
for index in range(len(s1)):
    if s1[index] != s2[index]:
        count+=1
    if s1.count(s1[index]) != s2.count(s1[index]):
        print("NO")
        break 
else:
    if count <= 2:
        print("YES")
    else:
        print("NO")

