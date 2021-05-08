def isPrime(num):
    for ctr in range(2,int(num**0.5)+1):
        if num%ctr == 0:
            return False 
    return True  

N = int(input())
for num in range(3,N+1):
    if not isPrime(num) and isPrime(num-1) and isPrime(num+1):
        print(num,end=" ")
