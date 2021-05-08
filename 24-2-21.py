N = int(input())
sol = []
if N == 1:
    print("a",end=" ")
    sol.append("a")
else:
    print("a",end=" ")
    sol.append("a")
    print("b",end=" ")
    sol.append("b")
    for i in range(N-2):
        print(sol[i+1]+sol[i],end=" ")
        sol.append(sol[i+1]+sol[i])

