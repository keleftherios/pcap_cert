# Scenario
# Prof. Jekyll conducts classes with students and regularly makes notes in a text file.
# Each line of the file contains three elements:
# - the student's first name,
# - the student's last name, and
# - the number of point the student received during certain classes.
#
# The elements are separated with white spaces.
# Each student may appear more than once inside Prof. Jekyll's file.
#
# The file may look as follows:
#
# John Smith 5
# Anna Boleyn 4.5
# John Smith 2
# Anna Boleyn 11
# Andrew Cox 1.5
#
# Your task is to write a program which:
# asks the user for Prof. Jekyll's file name;
# reads the file contents and counts the sum of the received points for each student;
# prints a simple (but sorted) report, just like this one:
#
# Andrew Cox 1.5
# Anna Boleyn 15.5
# John Smith 7.0
#
# Note:
# ++ your program must be fully protected against all possible failures:
#    the file's non-existence, the file's emptiness, or any input data failures;
#    encountering any data error should cause immediate program termination, and
#    the erroneous should be presented to the user;
#
# ++ implement and use your own exceptions hierarchy - we've presented it in the editor;
#    the second exception should be raised when a bad line is detect, and
#    the third when the source file exists but is empty.
#
# Tip:
# Use a dictionary to store the students' data.
#

class StudentsDataException(Exception):
    """Base class for other exceptions"""
    pass


class BadLine(StudentsDataException):
    # Write your code here.
    def __init__(self, message):
        super().__init__(message)

class FileEmpty(StudentsDataException):
    # Write your code here.
    def __init__(self, message):
        super().__init__(message)


# import errno
from os import strerror

# file = input("Please enter your file: ")
# file = 'profJekellyFile.txt'
# file = 'empty.txt'
file = 'profJekellyBadLine.txt'
# file = 'file.bin'
# file = 'noExist.txt'

D = {}
try:
    data = open(file, 'rt', encoding='UTF-8')
    lines = data.readlines()
    data.close()
    if not len(lines):
        raise FileEmpty("The file is empty...")
    for num, line in enumerate(lines):
        dataRow = line.split()
        if len(dataRow) != 3:
            raise BadLine(f"Got bad line... \nNumber of line: {num} \nLine: {' '.join(dataRow)}")
        studentName, studentSurname, studentPoint = dataRow[0], dataRow[1], dataRow[2]
        if not studentName.isalpha() or not studentSurname.isalpha():
            raise BadLine(f"Wrong student name at line {num}. Student Name: {studentName} {studentSurname}")
        for digit in studentPoint.split('.'):
            if not digit.isnumeric():
                raise BadLine(f"Not a valid mark at line {num}. Mark: {studentPoint}")
        fullName = studentName + ' ' + studentSurname
        try:
            D[fullName] += float(studentPoint)
        except KeyError:
            D[fullName] = float(studentPoint)
except FileEmpty as e:
    print(f"{e}")
except BadLine as e:
    print(f"{e}")
except Exception as exc:
        print(f"Got unexpected error number {exc.errno} - {strerror(exc.errno)}")
else:
    for name, point in sorted(D.items()):
        print(f"{name} --> {point}")


filesToTest = ["profJekellyFile.txt", "empty.txt", "profJekellyBadLine.txt", "file.bin", "noExist.txt"]

