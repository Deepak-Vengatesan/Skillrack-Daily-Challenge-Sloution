N = int(input())
arr = list(map(int,input().split()))
k = int(input())

maxval = -1
for ind in range(0,N):
    maxval = max(maxval,arr[ind])

    if (ind+1)%k == 0:
        print(maxval,end=" ")
        maxval = -1



'''

10
2 55 88 14 678 455 9899  12 545 222
4

10
2 55 88 14 678 455 9899 12 545 222
5


10
56 59 85 78 64 76 19 50 71 54
1

'''
