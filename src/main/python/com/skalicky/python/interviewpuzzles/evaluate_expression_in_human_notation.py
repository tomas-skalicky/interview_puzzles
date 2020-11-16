# Task:
#
# Given a mathematical expression with just single digits, plus signs, negative signs, and brackets, evaluate
# the expression. Assume the expression is properly formed.
#
# Example:
# Input: - ( 3 + ( 2 - 1 ) )
# Output: -4
# Here's the function signature:
#
# def eval(expression):
#   # Fill this in.
#
# print eval('- (3 + ( 2 - 1 ) )')
# # -4
from abc import ABC, abstractmethod
from collections import deque
from typing import Deque, List


# Abstract Base Class
class AbstractItem(ABC):
    pass


class Number(AbstractItem):
    def __init__(self, value: int):
        self.value: int = value


class AbstractBinaryOperator(AbstractItem, ABC):
    @abstractmethod
    def apply(self, operand_one: Number, operand_two: Number):
        raise Exception('Must be implemented by children')


class BinaryPlus(AbstractBinaryOperator):
    def apply(self, operand_one: Number, operand_two: Number) -> int:
        return operand_one.value + operand_two.value


class BinaryMinus(AbstractBinaryOperator):
    def apply(self, operand_one: Number, operand_two: Number) -> int:
        return operand_one.value - operand_two.value


def squash_stacked_items_by_evaluation_of_binary_operator(stacked_items: Deque[AbstractItem]) -> None:
    operand_two = stacked_items.pop()
    assert isinstance(operand_two, Number)
    operator = stacked_items.pop()
    assert isinstance(operator, AbstractBinaryOperator)
    operand_one = stacked_items.pop()
    assert isinstance(operand_one, Number)
    stacked_items.append(Number(operator.apply(operand_one, operand_two)))


def evaluate_expression_without_parentheses(expression: List[str]) -> int:
    # We need a collection which offers an efficient remove from the beginning and end and efficient add at the end,
    # hence Deque.
    stacked_items: Deque[AbstractItem] = deque()
    item_index = 0
    while item_index < len(expression):
        item: str = expression[item_index]
        if item == '+':
            stacked_items.append(BinaryPlus())
        elif item == '-':
            stack_size = len(stacked_items)
            if stack_size == 0 or isinstance(stacked_items[stack_size - 1], AbstractBinaryOperator):
                unary_minus_count = 0
                while item == '-':
                    unary_minus_count = unary_minus_count + 1
                    item_index = item_index + 1
                    item = expression[item_index]
                number = int(item)
                if unary_minus_count % 2 == 1:
                    number = number * -1
                stacked_items.append(Number(number))
                if stack_size != 0:
                    squash_stacked_items_by_evaluation_of_binary_operator(stacked_items)
            else:
                stacked_items.append(BinaryMinus())
        else:
            stacked_items.append(Number(int(item)))
            if len(stacked_items) > 1:
                squash_stacked_items_by_evaluation_of_binary_operator(stacked_items)
        item_index = item_index + 1
    assert len(stacked_items) == 1
    number = stacked_items.popleft()
    assert isinstance(number, Number)
    return number.value


def evaluate_expression_in_human_notation(expression: str) -> int:
    stacked_expressions = []
    current_expression = []
    for c in list(expression):
        if c == '(':
            stacked_expressions.append(current_expression)
            current_expression = []
        elif c == ')':
            result = evaluate_expression_without_parentheses(current_expression)
            if len(stacked_expressions) > 0:
                current_expression = stacked_expressions.pop(len(stacked_expressions) - 1)
                current_expression.append(result)
            else:
                return result
        elif c != ' ':
            current_expression.append(c)
    return evaluate_expression_without_parentheses(current_expression)
