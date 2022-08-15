"""
Operations:
1. Stack(): Create an empty stack
2. push(item): Adds a new item to the top of the stack, needs the items and return nothing.
3. pop(): Check the last inserted element
4. is_empty(): Check if stack is empty
5. size(): Check the length of stack
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        _result = self.items.append(item)
        return _result

    def pop(self):
        _result = self.items.pop()
        return _result

    def peek(self):
        _len = len(self.items)
        _result = self.items[_len - 1]
        return _result

    def is_empty(self):
        # if self.items == []:
        #     return True
        # else:
        #     return False
        return self.items == []

    def size(self):
        _size = len(self.items)
        return _size

# s = Stack()
# print(s.items)
# s.push("hello")
# print(s.items)
# s.push("a")
# print(s.items)
# print(s.size())
# print(s.peek())
# s.pop()
# print(s.items)
# print(s.size())
# print(s.is_empty())
# print(s.items)
# print(s.size())
# s.pop()
# print(s.is_empty())