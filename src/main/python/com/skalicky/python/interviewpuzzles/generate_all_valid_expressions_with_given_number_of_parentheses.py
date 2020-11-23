# Task:
#
# Given a number n, generate all possible combinations of n well-formed brackets.
#
# Here are some examples and some starting code.
#
# def generate_brackets(n):
#   #Fill this in.
#
# print(generate_brackets(1))
# # ['()']
#
# print(generate_brackets(3))
# # ['((()))', '(()())', '()(())', '()()()', '(())()']
from collections import deque
from typing import Deque, List, Tuple


def generate_all_valid_expressions_with_given_number_of_parentheses(parenthesis_count: int) -> List[str]:
    if parenthesis_count == 0:
        return []
    else:
        expression_target_length: int = 2 * parenthesis_count
        result_expressions: List[str] = []
        already_generated_and_remaining_open_parenthesis_count: Deque[Tuple[str, int]] = deque()
        already_generated_and_remaining_open_parenthesis_count.append(('', parenthesis_count))
        while len(already_generated_and_remaining_open_parenthesis_count) > 0:
            already_generated, remaining_open_parenthesis_count = already_generated_and_remaining_open_parenthesis_count.popleft()

            if len(already_generated) == expression_target_length:
                assert remaining_open_parenthesis_count == 0
                result_expressions.append(already_generated)
            else:

                if remaining_open_parenthesis_count > 0:
                    already_generated_and_remaining_open_parenthesis_count.append(
                        (already_generated + '(', remaining_open_parenthesis_count - 1))

                max_length_with_current_number_of_open_parentheses: int = 2 * (
                            parenthesis_count - remaining_open_parenthesis_count)
                if len(already_generated) < max_length_with_current_number_of_open_parentheses:
                    already_generated_and_remaining_open_parenthesis_count.append(
                        (already_generated + ')', remaining_open_parenthesis_count))
        return result_expressions
