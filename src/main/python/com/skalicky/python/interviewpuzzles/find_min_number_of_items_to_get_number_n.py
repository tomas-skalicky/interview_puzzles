# Task:
#
# Given a list of possible coins in cents, and an amount (in cents) n, return the minimum number of coins needed to
# create the amount n. If it is not possible to create the amount using the given coin denomination, return None.
#
# Here's an example and some starter code:
#
# def make_change(coins, n):
#   # Fill this in.
#
# print(make_change([1, 5, 10, 25], 36))
# # 3 coins (25 + 10 + 1)
import sys
from collections import deque
from typing import List, Deque, Tuple, Optional


def make_change(coins: List[int], n: int) -> Optional[int]:
    coin_count: int = len(coins)
    if coin_count == 0:
        if n == 0:
            return 0
        else:
            return None
    else:
        sorted_coins: List[int] = sorted(coins, reverse=True)
        any_combination_found: bool = False
        min_collected_coin_count: int = sys.maxsize
        collected_coin_count_and_remaining_n_and_coin_index_to_process: Deque[Tuple[int, int, int]] = deque()
        collected_coin_count_and_remaining_n_and_coin_index_to_process.append((0, n, 0))
        while len(collected_coin_count_and_remaining_n_and_coin_index_to_process) > 0:
            collected_coin_count, remaining_n, coin_index_to_process = collected_coin_count_and_remaining_n_and_coin_index_to_process.pop()
            coin_to_process: int = sorted_coins[coin_index_to_process]
            if coin_to_process == remaining_n:
                min_collected_coin_count = min(min_collected_coin_count, collected_coin_count + 1)
                any_combination_found = True
            elif coin_to_process > remaining_n:
                collected_coin_count_and_remaining_n_and_coin_index_to_process.append(
                    (collected_coin_count, remaining_n, coin_index_to_process + 1))
            else:
                if (coin_count - coin_index_to_process) * coin_to_process >= remaining_n:
                    collected_coin_count_and_remaining_n_and_coin_index_to_process.append(
                        (collected_coin_count + 1, remaining_n - coin_to_process, coin_index_to_process + 1))
                elif (coin_count - coin_index_to_process - 1) * coin_to_process >= remaining_n:
                    collected_coin_count_and_remaining_n_and_coin_index_to_process.append(
                        (collected_coin_count, remaining_n, coin_index_to_process + 1))

        return min_collected_coin_count if any_combination_found else None


# 3 coins (25 + 10 + 1)
print(make_change([1, 5, 10, 25], 36))
# 3

print(make_change([1, 5, 10, 25], 32))
# None

# 2 coins (15 + 1)
print(make_change([1, 5, 10, 15, 25], 16))
# 2

print(make_change([], 0))
# 0

print(make_change([], 1))
# None

# The while-loop in the make_change function should have only one iteration, because
# (# of coins) * (max coin value) < (n)
print(make_change([1, 5, 10, 25], 101))
# None
