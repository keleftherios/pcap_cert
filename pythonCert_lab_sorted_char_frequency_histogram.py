# Scenario
# The previous code needs to be improved. It's okay, but it has to be better.
#
# Your task is to make some amendments, which generate the following results:
#
# the output histogram will be sorted based on the characters' frequency
# (the bigger counter should be presented first)
# the histogram should be sent to a file with the same name as the input one,
# but with the suffix '.hist'
# (it should be concatenated to the original name)
#
# Assuming that the input file contains just one line filled with:
#
# cBabAa
#
# the expected output should look as follows:
#
# a -> 3
# b -> 2
# c -> 1
#
# Tip: Use a lambda to change the sort order.

import string
from os import strerror

# file = input("Please enter your file: ")
file = 'samplefile.txt'

fileName = file.split(".")[0]

D = {char: 0 for char in string.ascii_lowercase}

try:
    data = open(file, 'rt', encoding='UTF-8')
except Exception as e:
    cause = strerror(e.errno)
    errNum = e.errno
    print(f"Got Exception: {e} \n{cause=} \n{errNum=}")
else:
    for char in data.read().lower():
        if char.isalpha():
            D[char] += 1
    data.close()

histFile = fileName + '.hist'
try:
    newFile = open(histFile, 'wt', encoding='UTF-8')
    text = ''
    for key, value in sorted(D.items(), key=lambda x: x[1], reverse=True):
        if value > 0:
            text += str(key) + ' --> ' + str(value) + "\n"
    print(text)
    newFile.write(text)
    newFile.close()
except IOError as e:
    print(f"I/O Error occurred... {strerror(e.errno)}")