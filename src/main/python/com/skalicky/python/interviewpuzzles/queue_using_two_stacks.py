# Task:
#
# Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol
# (First in = first out). Your class should support the enqueue and dequeue methods like a standard queue.
#
# Here's a starting point:
#
# class Queue:
#   def __init__(self):
#     # Fill this in.
#
#   def enqueue(self, val):
#     # Fill this in.
#
#   def dequeue(self):
#     # Fill this in.
#
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print q.dequeue()
# print q.dequeue()
# print q.dequeue()
# # 1 2 3


class Stack:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0


# Idea from https://www.geeksforgeeks.org/queue-using-stacks/
class QueueWithExpensiveEnqueue:
    def __init__(self):
        self.stack_for_enqueue = Stack()
        self.stack_for_dequeue = Stack()

    def enqueue(self, val):
        while not self.stack_for_dequeue.empty():
            self.stack_for_enqueue.enqueue(self.stack_for_dequeue.dequeue())
        self.stack_for_enqueue.enqueue(val)
        while not self.stack_for_enqueue.empty():
            self.stack_for_dequeue.enqueue(self.stack_for_enqueue.dequeue())

    def dequeue(self):
        return self.stack_for_dequeue.dequeue()


# Idea from https://www.geeksforgeeks.org/queue-using-stacks/
class QueueWithExpensiveDequeue:
    def __init__(self):
        self.stack_for_enqueue = Stack()
        self.stack_for_dequeue = Stack()

    def enqueue(self, val):
        return self.stack_for_enqueue.enqueue(val)

    def dequeue(self):
        while not self.stack_for_enqueue.empty():
            self.stack_for_dequeue.enqueue(self.stack_for_enqueue.dequeue())
        retrieved_item = self.stack_for_dequeue.dequeue()
        while not self.stack_for_dequeue.empty():
            self.stack_for_enqueue.enqueue(self.stack_for_dequeue.dequeue())
        return retrieved_item


q = QueueWithExpensiveEnqueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3
q2 = QueueWithExpensiveDequeue()
q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)
print(q2.dequeue())
print(q2.dequeue())
print(q2.dequeue())
# 1 2 3
