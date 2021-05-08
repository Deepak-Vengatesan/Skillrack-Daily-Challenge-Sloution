S = input().strip() 
alphaStr=digitStr=""
for ch in S:
    if ch.isalpha():
        alphaStr+=ch 
    else:
        digitStr+=ch 
points=0
if S == S[::-1]:
    points+=1
if alphaStr == alphaStr[::-1] and alphaStr:
    points+=1 
if digitStr == digitStr[::-1] and digitStr:
    points+=1
result =["NO","Single","Double","Triple"]
print(result[points],"Palindrome")


"""
output:

a34bc143ba

"""