N = int(input())
person = {}
for ctr in range(1,N+1):
    name = input().strip() 
    person[name] = person.get(name,0)+1
    print(name,end="")
    if person[name] > 1:
        print(person[name],end=" ")
    print()




