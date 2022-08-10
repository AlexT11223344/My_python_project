"""
Given parentheses, check if it balanced
Example: ({})()([]), ([{}]), ({{}})]])(),[[] etc.
"""
from Stack import *

s = Stack()
print(s.items)


def par_checker(par_string):
    balanced = True
    index = 0
    while index < len(par_string) and balanced:
        par = par_string[index]
        if par in "([{":
            s.push(par)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, par):
                    return False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def match(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


print(par_checker("(({([])}))"))
print(par_checker("((]}"))
