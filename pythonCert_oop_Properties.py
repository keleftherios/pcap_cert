# class ExampleClass:
#     def __init__(self, val = 1):
#         self.__first = val
#
#     def set_second(self, val = 2):
#         self.__second = val
#
#
# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)
#
# example_object_2.set_second(3)
#
# example_object_3 = ExampleClass(4)
# example_object_3.__third = 5
#
#
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)


class ExampleClass:
    varia = 1

    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)
print()
print(ExampleClass.__dict__)
print()
print(example_object.__dict__)
