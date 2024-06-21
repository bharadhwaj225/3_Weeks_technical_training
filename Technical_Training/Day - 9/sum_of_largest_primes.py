# # print the sum of the largest prime numbers btween the two consecutive numbers in the array
def isprime(x):
    for i in range(2,(x//2)+1):
        if(x%i == 0):
            return 0
    return 1



def longest_prime(n , m):
    for i in range(m-1 , n , -1):
        if(isprime(i)):
            return i
    return 0


a = list(map(int,input().split()))
sum = 0
for i in range(len(a) - 1):
    sum = sum + longest_prime(a[i],a[i+1])
print(sum)


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def largest_prime_between(a, b):
#     primes = [i for i in range(a+1, b) if is_prime(i)]
#     return max(primes) if primes else 0

# arr = list(map(int,input().split()))
# sum_of_largest_primes = 0
# for i in range(len(arr) - 1):
#     sum_of_largest_primes += largest_prime_between(arr[i], arr[i+1])

# print(sum_of_largest_primes)