# Scenario
# Do you know what a palindrome is?
#
# It's a word which look the same when read forward and backward.
# For example, "kayak" is a palindrome, while "loyal" is not.
#
# Your task is to write a program which:
#
# asks the user for some text;
# checks whether the entered text is a palindrome, and prints result.
# Note:
#
# assume that an empty string isn't a palindrome;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent;
# there are more than a few correct solutions - try to find more than one.
# Test your code using the data we've provided.
#
# Test data
# Sample input:
#
# Ten animals I slam in a net
#
# Sample output:
#
# It's a palindrome
#
#
# Sample input:
#
# Eleven animals I slam in a net
#
# Sample output:
#
# It's not a palindrome

text = input("Please enter a text: ")

L = text.lower().strip().split()
newText = ''.join(L)

if newText == newText[::-1] and len(L) != 0:
    print("Its a palindrome")
else:
    print("It's not a palindrome")
