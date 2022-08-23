'''
1. Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
2. enqueue() adds a new item to the rear of the queue. It needs the item and returns nothing.
3. dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified
4. is_empty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
5. size() returns the number of items in the queue. It needs no parameters and returns an integer.
'''


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        _result = self.items.insert(0, item)
        return _result

    def dequeue(self):
        _result = self.items.pop()
        return _result

    def is_empty(self):
        return self.items == []

    def size(self):
        _size = len(self.items)
        return _size

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
print(q.items)
print(q.dequeue())
print(q.items)
q.dequeue()
print(q.items)