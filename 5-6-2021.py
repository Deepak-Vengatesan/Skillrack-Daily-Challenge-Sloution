S = input().strip()
print(S[0]+S[-1])
for row in range(1,len(S)):
    print(S[:row+1][::-1]+S[len(S)-1-row:][::-1])