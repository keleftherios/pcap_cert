# Scenario
# As you already know, a stack is a data structure realizing the so-called LIFO (Last In - First Out) model.
# It's easy and you've already grown perfectly accustomed to it.
#
# Let's taste something new now. A queue is a data model characterized by the term FIFO: First In - Fist Out.
# Note: a regular queue (line) you know from shops or post offices works
# exactly in the same way - a customer who came first is served first too.
#
# Your task is to implement the Queue class with two basic operations:
#
# put(element), which puts an element at end of the queue;
# get(), which takes an element from the front of the queue and returns it as the result
# (the queue cannot be empty to successfully perform it.)
# Follow the hints:
#
# use a list as your storage (just like we did in stack)
# put() should append elements to the beginning of the list,
# while get() should remove the elements from the list's end;
# define a new exception named QueueError (choose an exception to derive it from)
# and raise it when get() tries to operate on an empty list.
# Complete the code we've provided in the editor. Run it to check whether its output is similar to ours.
#
# Expected output
# 1
# dog
# False
# Queue error

class QueueError(Exception):
    pass


class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, elem):
        self.__queue_list.insert(0, elem)

    def get(self):
        if len(self.__queue_list) == 0:
            raise QueueError
        else:
            return self.__queue_list.pop()


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

