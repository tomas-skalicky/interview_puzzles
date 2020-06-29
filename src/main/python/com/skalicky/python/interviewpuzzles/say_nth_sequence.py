# Task:
#
# A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next term is
# obtained by describing the previous term. An example is easier to understand:
#
# Each consecutive value describes the prior value.
#
# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.
#
# Your task is, return the nth term of this sequence.
from typing import List


def generate_next_sequence(input_sequence: List[int]):
    counted_number: int = None
    counted_number_occurrence: int = 0
    i: int = 0
    result_sequence: List[int] = []
    while i < len(input_sequence):
        current_number: int = input_sequence[i]
        if counted_number is None:
            counted_number = current_number
            counted_number_occurrence = 1
        elif current_number == counted_number:
            counted_number_occurrence = counted_number_occurrence + 1
        else:
            result_sequence.append(counted_number_occurrence)
            result_sequence.append(counted_number)
            counted_number = current_number
            counted_number_occurrence = 1
        i = i + 1
    result_sequence.append(counted_number_occurrence)
    result_sequence.append(counted_number)
    return result_sequence


def generate_nth_sequence(n: int):
    if n < 1:
        raise Exception('non allowed n [{}]'.format(n))
    elif n == 1:
        return [1]
    else:
        current_sequence: List[int] = [1]
        for i in range(2, n + 1):
            current_sequence = generate_next_sequence(current_sequence)
        return current_sequence


print(generate_nth_sequence(1))
# 1
print(generate_nth_sequence(2))
# 11 ....... one 1's
print(generate_nth_sequence(3))
# 21 ....... two 1's
print(generate_nth_sequence(4))
# 1211 ..... one 2, and one 1.
print(generate_nth_sequence(5))
# 111221 ... one 1, one 2, and two 1's.
