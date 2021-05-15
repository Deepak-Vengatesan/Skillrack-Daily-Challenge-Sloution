# S = input().split("-")
# temp = ['' for row in range(len(S))]
# ch =''
# for i in S:
#     point,ch = '', ''
#     for j in i:
#         if j.isdigit():
#             point += str(j)
#         else:
#             ch  += j  
#     temp[int(point)-1] = ch 
# print(''.join(temp))



s = input().strip().split("-")
d = dict()
for i in s:
    try:
        d[int(i[:-1])] = i[-1]
    except:
        d[int(i[1:])] = i[0]
for i in sorted(d):
    print(d[i],end="")


'''

4l-9k-R6-7a-k2-3i-S1-L5-8c

6n-4t-1c-o2-d10-11y-t3-8a-o5-7C-n9

'''