def printChars(ch1,ch2):
    while ch1 != ch2:
        print(ch1,end="")
        ch1=chr(ord(ch1)+1)
        if ord(ch1) == ord('z')+1:
            ch1='a'
    print(ch1,end="")
S=input().strip()
for index in range(0,len(S)-1):
    printChars(S[index],S[index+1])