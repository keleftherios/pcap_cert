class Level1:
    variable_1 = 100

    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Level2(Level1):
    variable_2 = 200

    def __init__(self):
        super().__init__()
        self.var_2 = 201

    def fun_2(self):
        return 202


class Level3(Level2):
    variable_3 = 300

    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


obj = Level3()

print(obj.variable_1, obj.var_1, obj.fun_1())
print(obj.variable_2, obj.var_2, obj.fun_2())
print(obj.variable_3, obj.var_3, obj.fun_3())


print("================================================")

class SuperA:
    var_a = 10
    def fun_a(self):
        return 11


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())

print("================================================")

# We can say that Python looks for object components in the following order:
#
# - Inside the object itself;
# - In its superclasses, from bottom to top;
# - If there is more than one class on a particular inheritance path,
#   Python scans them from left to right.


class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())

print("================================================")


