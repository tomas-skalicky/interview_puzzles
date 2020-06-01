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

    def push(self, val):
        self.stack.append(val)
        if len(self.maximums) == 0:
            self.maximums.append(val)
        elif val > self.maximums[len(self.maximums) - 1]:
            self.maximums.append(val)
        else:
            self.maximums.append(self.maximums[len(self.maximums) - 1])

    def pop(self):
        if len(self.maximums) == 0:
            raise Exception('empty stack')
        else:
            self.maximums.pop()
            return self.stack.pop()

    def max(self):
        if len(self.maximums) == 0:
            return None
        else:
            return self.maximums[len(self.maximums) - 1]


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
s.pop()
s.pop()
print(s.max())
# None
s.pop()
# Exception
