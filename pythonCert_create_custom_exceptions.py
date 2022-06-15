class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print('Division by zero')

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print('My division by zero')
    except ZeroDivisionError:
        print('Original division by zero')


print("===============================================")

# class PizzaError(Exception):
#     def __init__(self, pizza, message):
#         # Exception.__init__(self, message)
#         super().__init__(message)
#         self.pizza = pizza
#
# class TooMuchCheeseError(PizzaError):
#     def __init__(self, pizza, cheese, message):
#         # PizzaError.__init__(self, pizza, cheese, message)
#         super().__init__(pizza, message)
#         self.cheese = cheese

print("===============================================")

# The previous solution, although elegant and efficient, has one important weakness.
# Due to the somewhat easygoing way of declaring the constructors,
# the new exceptions cannot be used as-is, without a full list of required arguments.
#
# We'll remove this weakness by setting the default values for all constructor parameters.


class PizzaError(Exception):
    def __init__(self, pizza='uknown', message=''):
        # Exception.__init__(self, message)
        super().__init__(message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uknown', cheese='>100', message=''):
        # PizzaError.__init__(self, pizza, message)
        super().__init__(pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

