# Task:
#
# You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed in order
# to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.
#
# Example:
#
# "()())()"
#
# The following input should return 1.
#
# ")("
#
# Here's a start:
#
# def count_invalid_parenthesis(string):
#   # Fill this in.
#
# print count_invalid_parenthesis("()())()")
# # 1


def count_invalid_parenthesis(string: str) -> int:
    invalid_parenthesis_count: int = 0
    open_parenthesis_count: int = 0
    for c in list(string):
        if c == '(':
            open_parenthesis_count += 1
        else:
            if open_parenthesis_count > 0:
                open_parenthesis_count -= 1
            else:
                invalid_parenthesis_count += 1
    invalid_parenthesis_count += open_parenthesis_count
    return invalid_parenthesis_count


print(count_invalid_parenthesis(""))
# 0
print(count_invalid_parenthesis("()())()"))
# 1
print(count_invalid_parenthesis("()(())()"))
# 0
print(count_invalid_parenthesis("()()))(()"))
# 3
