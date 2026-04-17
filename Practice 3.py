"""
Write a program to create function calculation() such that it can accept two variables and calculate
 addition and subtraction. Also, it must return both addition and subtraction in a single return call.
"""

def calculation(x,y):
    add= x + y
    subtract= x - y
    return add,subtract
print(calculation(8,2))
