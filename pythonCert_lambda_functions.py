two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


print("\n" * 3)

# The "map()" function: map(function, list)
# The map() function applies the function passed by its first argument to all its second argument's elements,
# and returns an iterator delivering all subsequent function results.

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_1)
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print("\n" * 3)

# The "filter()" function: filter(function, iterable)
# The filter() function extracts elements from an iterable (list, tuple etc.) for which a function returns True.
# Arguments:
#    - function: A function
#    - iterable: An iterable like sets, lists, tuple, etc.
# The filter function return an iterator!

from random import seed, randint

seed(10)
data = [randint(-10,10) for x in range(10)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
