a = "abcde"
b = 1
max_substring = 0

for i in range(len(a)-1):
    if((ord(a[i]) == ord(a[i+1])-1)):
        b+=1
    else:
        if max_substring < b:
            max_substring=b
        b=1

if(b>max_substring):
    max_substring = b
    
print(max_substring)