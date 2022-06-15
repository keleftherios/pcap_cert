numbers = (1, 2, 5, 9, 15)

def filter_numbers(num):
    nums = (1, 5, 17)
    if num in nums:
        return True
    else:
        return False

filtered_numbers = filter(filter_numbers, numbers)

for n in filtered_numbers:
    print(n)

print("\n###################################################")

def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in fun(2):
    print(x, end='')

print("\n###################################################")

from datetime import date

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2)


x = "\\\\"