"""
Given a integer, convert it to the binary number
8-> 1000, 9-> 1001
"""

from Stack import *
stack = Stack()


def convert(x, divide_num):
    while x > 0:
        binary = x % divide_num
        stack.push(binary)
        x = x // divide_num
    bin_str = ""
    while not stack.is_empty():
        bin_str = bin_str + str(stack.pop())
    return bin_str


print(convert(8, 2))

