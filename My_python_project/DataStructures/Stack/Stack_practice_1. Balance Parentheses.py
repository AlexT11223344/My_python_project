"""
Given parentheses, check if it balanced
Example: ()()(), ((())), (())(), (())(() etc.
"""
from Stack import *

s = Stack()
print(s.items)


def par_checker(par_string):
    balanced = True
    index = 0
    while index < len(par_string) and balanced:
        par = par_string[index]
        if par == "(":
            s.push(par)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False

print(par_checker("(())"))
print(par_checker("(()"))
