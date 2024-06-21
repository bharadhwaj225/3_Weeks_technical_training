#co-prime

import math

x = int(input())
y = int(input())

# while y:
#     x, y = y, x % y
# if x == 1:
#     print("co-prime")
# else:
#     print("not co-prime")


z = math.gcd(x, y)
print(z)
if z == 1:
    print("Coprime")
else:
    print("Not Coprime")