def fun(n):
    for i in range(n):
        yield i

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

if __name__ == "__main__":

    for v1 in fun(5):
        print(v1)

    print("------------------------------------")

    for v2 in powers_of_2(8):
        print(v2)

    print("------------------------------------")

    # Generators and "list comprenhansions"
    t = [x for x in powers_of_2(5)]
    print(t)

    print("------------------------------------")

    # The "list()" function
    t2 = list(powers_of_2(3))
    print(t2)

    print("------------------------------------")

    # The "in" operator
    for i in range(20):
        if i in powers_of_2(4):
            print(i)

    print("------------------------------------")

    # The "Fibonacci" number generator
    fibs = list(fibonacci(10))
    print(fibs)