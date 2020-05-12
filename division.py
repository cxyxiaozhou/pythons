#!/usr/bin/python
#coding:UTF-8
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero!")
"""
print("Give me two numbers and I'll divide them.")
print("Enter '9' to quit.")

while True:
    first_number=input("\nFirst name:")
    if first_number=='q':
        break
    second_number=input("\nSecond_number:")
    try:
        answer=int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can divide by 0!")
    else:
        print(answer)