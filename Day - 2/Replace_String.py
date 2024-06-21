# a = input()
# b = int(input())

# for i in a:
#     c = ord(i)
#     if ord(i) - b < 97:
#         c = ord(i) + 26
#     print(chr(c-b), end="")

a = input()
b = int(input())
c = b % 26
d =''
for i in a:
    if((ord(i)-c) >= 97):
        d = d + chr(ord(i)-c)
    else:
        d = d + chr(ord(i)-c + 26)

print(d)