def add(*args):
    sumval = sum([i for i in args])
    return sumval 

a,b,c,d,e= map(int,input().split())
print(add(a,b))
print(add(a,b,c))
print(add(a,b,c,d))
print(add(a,b,c,d,e))