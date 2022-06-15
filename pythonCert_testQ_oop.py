# class A:
#     def __str__(self):
#         return 'a'
#
# class B(A):
#     def __str__(self):
#         return 'b'
#
# class C(B):
#     pass
#
# o = C()
# print(o)
########################################################
########################################################
# class A:
#     v = 2
#
# class B(A):
#     v = 1
#
# class C(B):
#     pass
#
# o = C()
# print(o.v)
########################################################
########################################################
# class A:
#     def __str__(self):
#         return 'a'
#
# class B:
#     def __str__(self):
#         return 'b'
#
# class C(A, B):
#     pass
#
# o = C()
# print(o)
########################################################
########################################################
class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(B, A):
    def c(self):
            self.a()

o = C()
o.C()
