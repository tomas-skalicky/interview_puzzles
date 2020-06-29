# Task:
#
# You are given an array. Each element represents the price of a stock on that particular day. Calculate and return
# the maximum profit you can make from buying and selling that stock only once.
#
# For example: [9, 11, 8, 5, 7, 10]
#
# Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5
# (profit = 10 - 5 = 5).
#
# Here's your starting point:
#
# def buy_and_sell(arr):
#   #Fill this in.
#
# print buy_and_sell([9, 11, 8, 5, 7, 10])
# # 5
from typing import List


def buy_and_sell(arr: List[int]):
    if len(arr) == 0:
        return 0
    else:
        largest_profit: int = 0
        current_min: int = arr[0]
        for i in range(1, len(arr)):
            current_price: int = arr[i]
            if current_price < current_min:
                current_min = current_price
            else:
                largest_profit = max(largest_profit, current_price - current_min)
        return largest_profit


print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
print(buy_and_sell([6, 12, 8, 5, 7, 10]))
# 6
