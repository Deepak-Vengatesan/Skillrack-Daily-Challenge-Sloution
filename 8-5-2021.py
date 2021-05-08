s1 = input().strip()
s2 = input().strip()

s1Ind = len(s1)//2
s2Ind = len(s2)//2

cStr = ""

for ctr in range(0,min(s1Ind,s2Ind)+1):
    substringofs1 = s1[s1Ind-ctr:s1Ind+ctr+1]
    substringofs2 = s2[s2Ind-ctr:s2Ind+ctr+1]
    # print(hello)
    if substringofs1 == substringofs2:
        cStr = substringofs1

if cStr == " ":
    print(-1)
else:
    print(cStr)



'''

doglionlizard
absolutionlizagging

'''