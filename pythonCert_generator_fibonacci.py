#####################
### CODE ANALYSIS ###
#####################
# lines 30 through 34:
# the class constructor prints a message (we'll use this to trace the class's behavior),
# prepares some variables:
#   __n to store the series limit,
#   __i to track the current Fibonacci number to provide, and
#   __p1 along with __p2 to save the two previous numbers;
#
# lines 36 through 38:
# the __iter__ method is obliged to return the iterator object itself;
# its purpose may be a bit ambiguous here, but there's no mystery;
# try to imagine an object which is not an iterator (e.g., it's a collection of some entities),
# but one of its components is an iterator able to scan the collection;
# the __iter__ method should extract the iterator and entrust it with the execution of the iteration protocol;
# as you can see, the method starts its action by printing a message;
#
# lines 40 through 49:
# the __next__ method is responsible for creating the sequence;
# it's somewhat wordy, but this should make it more readable;
# first, it prints a message, then it updates the number of desired values,
# and if it reaches the end of the sequence,
# the method breaks the iteration by raising the StopIteration exception;
# the rest of the code is simple, and it precisely reflects the definition we showed you earlier;
#
# lines 51 and 52 make use of the iterator.

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

for i in Fib(10):
    print(i)

