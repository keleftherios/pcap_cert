# Scenario
# An anagram is a new word formed by rearranging the letters of a word,
# using all the original letters exactly once.
#
# For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.
#
# Your task is to write a program which:
#
# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.
# Note:
#
# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent
# Test your code using the data we've provided.
#
# Test data
# Sample input:
#
# Listen
# Silent
#
# Sample output:
#
# Anagrams
#
#
# Sample input:
#
# modern
# norman
#
# Sample output:
#
# Not anagrams

text_1 = input("Enter text_1: ")
text_2 = input("Enter text_2: ")

# Solution_1
anagram = True
if len(text_1) == len(text_2):
    for i in text_1.lower():
        if text_2.lower().find(i) == -1:
            print("Not anagrams")
            anagram = False
            break
    if anagram:
        print("Anagrams")
else:
    print("Not anagrams")

# Solution_2
T1 = sorted(list(text_1.lower()))
T2 = sorted(list(text_2.lower()))

# NOTE:
# The code "T1.sort() == T2.sort()" always results to True.
# Reason is that "T1.sort()" returns "None" and so "T2.sort()" - so None == None

if T1 == T2:
    print("Anagrams!!!")
else:
    print("Not anagrams...")
