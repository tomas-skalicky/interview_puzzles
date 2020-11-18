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
from typing import List, Optional


def say_next_sequence(input_sequence: List[int]) -> List[int]:
    counted_number: Optional[int] = None
    counted_number_occurrence: int = 0
    i: int = 0
    result_sequence: List[int] = []
    while i < len(input_sequence):
        current_number: int = input_sequence[i]
        if counted_number is None:
            counted_number = current_number
            counted_number_occurrence = 1
        elif current_number == counted_number:
            counted_number_occurrence += 1
        else:
            result_sequence.append(counted_number_occurrence)
            result_sequence.append(counted_number)
            counted_number = current_number
            counted_number_occurrence = 1
        i += 1
    result_sequence.append(counted_number_occurrence)
    result_sequence.append(counted_number)
    return result_sequence


def say_nth_sequence(n: int) -> List[int]:
    if n < 1:
        raise RuntimeError('non allowed n [{}]'.format(n))
    else:
        current_sequence: List[int] = [1]
        for i in range(2, n + 1):
            current_sequence = say_next_sequence(current_sequence)
        return current_sequence
