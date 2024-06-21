#for the given input print the next palindrome number 

n = int(input())
if str(n) == str(n)[::-1]:
    print("yes")
else:
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            print(n)
            break
    