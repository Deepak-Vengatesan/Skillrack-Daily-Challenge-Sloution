l = input().split()
cnt = True 
while True:
    try:
        l.append(input().strip())
        cnt = False
    except:
        break
if cnt:
    print(*l[::-1],sep="\n")
else:
    print(*l[::-1])

print(len(l))