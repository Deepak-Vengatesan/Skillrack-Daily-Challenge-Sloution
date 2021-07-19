sb = ""
while True:
    try:
        currLine = input().split()
        for word in currLine:
            sb+=word[-1]
    except:
        break
print(sb[::-1])