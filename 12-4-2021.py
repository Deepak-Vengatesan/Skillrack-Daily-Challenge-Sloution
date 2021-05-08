def reverse(num):
    return int(str(num)[::-1])
N = int(input())
series = [0,1]
for ctr in range(1,N+1):
    series.append(reverse(series[-1])+reverse(series[-2]))
print(*series[:N])