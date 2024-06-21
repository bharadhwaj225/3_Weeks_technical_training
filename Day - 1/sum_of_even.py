#2+4+6+8=20

def sum_of_even():
    numbers = []
    for i in range(0, 10):
        if i % 2 == 0:
            numbers.append(i)
    return sum(numbers)

print(sum_of_even()) 