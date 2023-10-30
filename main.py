s="ZOho"
for i in range(len(s)):
    if(ord(s[i])<91):
        print(chr(ord(s[i])+32),end='')
    else:
        print(chr(ord(s[i])-32),end='')