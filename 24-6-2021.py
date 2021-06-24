N = int(input())
ls = list(map(int,input().split()))
sums = 0
for i in range(0,N):
  length = len(str(ls[i]))
  sVal = str(length)+str(ls[i])
  sums += int(sVal)
print(sums)