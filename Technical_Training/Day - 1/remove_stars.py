n = input()
b = []
for i in n:
    if (i!='*'):
        b.append(i)
    else:
        b.pop()
print(''.join(b))