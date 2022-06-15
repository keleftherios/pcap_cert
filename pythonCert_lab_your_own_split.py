# Scenario
# You already know how split() works. Now we want you to prove it.
#
# Your task is to write your own function,
# which behaves almost exactly like the original split() method, i.e.:
#
# it should accept exactly one argument - a string;
# it should return a list of words created from the string,
# divided in the places where the string contains whitespaces;
#
# if the string is empty, the function should return an empty list;
# its name should be mysplit()
# Use the template in the editor. Test your code carefully.
#
# Expected output
# ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
# ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
# []
# ['abc']
# []


def mysplit(strng):
    strng = strng.strip()
    if not len(strng):
        return []
    return strng.split()

def mysplit_v2(strng):
    """
    Function that does not use the split() method.
    """
    mylist = []
    start = 0
    strng = strng.strip()
    if strng.find(' ') == -1:
        mylist.append(strng)
        return mylist
    for index, letter in enumerate(strng):
        if letter == ' ':
            mylist.append(strng[start:index])
            start = index + 1
    mylist.append(strng[start:])
    return mylist


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))