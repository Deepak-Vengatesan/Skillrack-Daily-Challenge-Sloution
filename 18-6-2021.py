words = list(input().split())
flag = 1
for i in range(len(words)):
    for j in range(len(words)):
        if(words[i] == words[j]):
            continue 
        elif (words[i]+words[j]) == (words[i]+words[j])[::-1]:
            print(words[i]+words[j])
            flag = 0 
if flag == 1:
    print(-1)



'''

tiger register regit egit all a la

'''
