string = list(input().strip())
counter,ctr = 0,0
vowels = ['a','e','i','o','u','A','E','I','O','U']
while(counter != len(string)):
    if(string[counter] in vowels):
        if(ctr == 0):
            fptr = counter 
            ctr+=1
        else:
            string[counter],string[fptr] = string[fptr], string[counter]
            ctr=0
    counter+=1 
print(''.join(string))