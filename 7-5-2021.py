N =int(input())
marks = list(map(int,input().split()))
X = int(input())
Xthmark = marks[X-1]
marks = sorted(set(marks),reverse=True)
print(marks.index(Xthmark)+1)



''' 

5
55 60 55 50 60
4

'''