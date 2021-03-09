# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



def isNumberOdd(num):
    if (num % 2) == 0:
        return 0
    else:
        return 1


num = int(input("Give me your number\n"))
if isNumberOdd(num):
    print(num.__str__()+" is odd")
else:
    print(num.__str__()+" is even")