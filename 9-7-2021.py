s1 = input().strip()
s2  = input().strip()
for ind in range(len(s2)):
    print(s1[:ind+1]*int(s2[ind]))