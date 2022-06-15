# Scenario
# A text file contains some text (nothing unusual)
# but we need to know how often (or how rare) each letter appears in the text.
# Such an analysis may be useful in cryptography,
# so we want to be able to do that in reference to the Latin alphabet.
#
# Your task is to write a program which:
#
# asks the user for the input file's name;
# reads the file (if possible) and counts all the Latin letters
# (lower- and upper-case letters are treated as equal)
#
# prints a simple histogram in alphabetical order
# (only non-zero counts should be presented)
#
# Create a test file for the code,
# and check if your histogram contains valid results.
#
# Assuming that the test file contains just one line filled with:
#
# aBc
#
# the expected output should look as follows:
#
# a -> 1
# b -> 1
# c -> 1
#
# Tip:
# We think that a dictionary is a perfect data collection medium for storing the counts.
# The letters may be keys while the counters can be values.

import string
from os import strerror

# file = input("Enter your file: ")

file = 'samplefile.txt'
# file = 'file.bin'
# file = 'r.bin'

D = {char: 0 for char in string.ascii_lowercase}
try:
    data = open(file, 'rt', encoding='UTF-8')
except Exception as e:
    print(f"Following Error occured: {e} \nCause: {strerror(e.errno)} \nError Num: {e.errno}")
else:
    for char in data.read().lower():
        if char.isalpha():
            D[char] += 1
    data.close()

    for key, value in D.items():
        if value > 0:
            print(f"{key} --> {value}")
