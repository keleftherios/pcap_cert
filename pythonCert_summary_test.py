class A:
    def __init__(self, v=2):
        self.v = v

    def set(self, v=1):
        self.v += v
        return self.v


a = A()
b = a
b.set()
print(a.v)

print("=============================")

# class A:
#     def m(self):
#         print("In class A")
#
# class B:
#     def m(self):
#         print("In class B")
#
# class C(B, A):
#     pass
#
# o = C()
# o.m()

class A:
    def a(self):
        print("a")

class B:
    def a(self):
        print("b")

class C(B, A):
    def c(self):
        self.a()

o = C()
o.c()

print("=============================")

from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)
print(datetime_1 - datetime_2)

print("=============================")

# class A:
#     def __init__(self):
#         pass
#
# a = A(1)
# print(hasattr(a, 'A'))



