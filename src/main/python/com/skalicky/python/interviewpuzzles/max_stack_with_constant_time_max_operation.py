# Task:
#
# Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max()
# which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant
# time.
#
# class MaxStack:
#   def __init__(self):
#     # Fill this in.
#
#   def push(self, val):
#     # Fill this in.
#
#   def pop(self):
#     # Fill this in.
#
#   def max(self):
#     # Fill this in.
#
# s = MaxStack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(2)
# print s.max()
# # 3
# s.pop()
# s.pop()
# print s.max()
# # 2


class MaxStack:
    def __init__(self):
        self.stack = []
        self.maximums = []

    def push(self, value):
        self.stack.append(value)
        if len(self.maximums) == 0:
            self.maximums.append(value)
        elif value > self.maximums[len(self.maximums) - 1]:
            self.maximums.append(value)
        else:
            self.maximums.append(self.maximums[len(self.maximums) - 1])

    def pop(self):
        if len(self.maximums) == 0:
            raise RuntimeError('empty stack')
        else:
            self.maximums.pop()
            return self.stack.pop()

    def max(self):
        """Idea taken from https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
        """

        return self.maximums[len(self.maximums) - 1] if len(self.maximums) > 0 else None
