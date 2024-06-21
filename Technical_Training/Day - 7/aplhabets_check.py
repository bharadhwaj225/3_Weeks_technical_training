# a = "the quick brown fox jumps over the lazy dog"
# b = set(a)
# if len(b) == 27:
#     print("yes")
# else:
#     print("no")


# l = "the 4quick br$%^own foENDx j45umps o.ver the lazy dog"

a = "the quick brown fox jumps over the lazy dog"
d = [0] * 26
for i in a:
    if(i.islower()):
        d[ord(i) - 97] += 1
        # d.add(i)
print(d)