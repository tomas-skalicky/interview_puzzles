# Task:
#
# Given an expression (as a list) in reverse polish notation, evaluate the expression. Reverse polish notation is where
# the numbers come before the operand. Note that there can be the 4 operands '+', '-', '*', '/'. You can also assume
# the expression will be well formed.
#
# Example
#
# Input: [1, 2, 3, '+', 2, '*', '-']
# Output: -9
#
# The equivalent expression of the above reverse polish notation would be (1 - ((2 + 3) * 2)).
#
# Here's some starter code:
#
# def reverse_polish_notation(expr):
#   # Fill this in.
#
# # 1 - (2 + 3) * 2
# print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# # -9
from typing import List, Set

BINARY_OPERATORS: Set[str] = {'+', '-', '*', '/'}


def evaluate_operator(operator: str, operand1: int, operand2: int) -> int:
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    else:
        return int(operand1 / operand2)


def reverse_polish_notation(expr: List[object]) -> int:
    expression_length: int = len(expr)
    if expression_length == 0:
        return None
    else:
        queued_expression_parts: List[object] = list()
        next_index: int = 0
        queued_expression_parts.append(expr[next_index])
        next_index += 1
        while next_index < expression_length:
            queued_expression_parts.append(expr[next_index])
            next_index += 1

            queued_expression_parts_count: int = len(queued_expression_parts)
            previous_iteration_parts_count: int = None

            while queued_expression_parts_count > 1 and queued_expression_parts_count != previous_iteration_parts_count:
                previous_iteration_parts_count = queued_expression_parts_count
                last_part = queued_expression_parts.pop()
                one_before_last_part = queued_expression_parts.pop()

                if queued_expression_parts_count == 2:
                    if last_part == '-' and isinstance(one_before_last_part, int):
                        return -1 * int(one_before_last_part)

                    else:
                        queued_expression_parts.append(one_before_last_part)
                        queued_expression_parts.append(last_part)

                else:
                    # queued_expression_parts_count >= 3
                    two_before_last_part = queued_expression_parts.pop()
                    if last_part == '-' and isinstance(one_before_last_part, int) and not isinstance(
                            two_before_last_part, int):
                        queued_expression_parts.append(two_before_last_part)
                        queued_expression_parts.append(-1 * int(one_before_last_part))

                    elif BINARY_OPERATORS.__contains__(last_part) and isinstance(one_before_last_part,
                                                                                 int) and isinstance(
                        two_before_last_part, int):
                        queued_expression_parts.append(evaluate_operator(str(last_part), int(two_before_last_part),
                                                                         int(one_before_last_part)))

                    else:
                        queued_expression_parts.append(two_before_last_part)
                        queued_expression_parts.append(one_before_last_part)
                        queued_expression_parts.append(last_part)
        return int(queued_expression_parts.pop())


# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# -9

print(reverse_polish_notation([]))
# None

print(reverse_polish_notation([8, '-']))
# -8
