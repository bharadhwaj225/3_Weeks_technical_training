n = int(input())
m = []
for i in range ():
    m.append(input())
s = input()
for i in range(len(s)):
    if(s[i] not in m[i%n]):
        print("No")
        break
else:
    print("Yes")

    


# n = int(input())
# s = [input() for i in range(n)]
# print(s)
# c = 0
# j = 0

# a = input()
# for i in range(len(a)):
#     if j==n:
#         j= 0
#     if a[i] in s[j]:
#         c = 0
#         j += 1
#     else:
#         c = 1
# print("No" if c else "Yes")