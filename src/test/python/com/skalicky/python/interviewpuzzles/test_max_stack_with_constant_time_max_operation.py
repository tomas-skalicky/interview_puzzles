from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.max_stack_with_constant_time_max_operation import MaxStack


class TestMaxStack(TestCase):
    def test_pop__when_stack_is_empty__then_pop_throws_exception(self):
        max_stack: MaxStack = MaxStack()
        self.assertRaisesRegex(RuntimeError, 'empty stack', max_stack.pop)

    def test_max__when_stack_is_empty__then_max_is_none(self):
        max_stack: MaxStack = MaxStack()
        self.assertIsNone(max_stack.max())

    def test_max__when_max_is_3_and_3_is_not_last_element__then_3_is_returned(self):
        max_stack: MaxStack = MaxStack()
        max_stack.push(1)
        max_stack.push(2)
        max_stack.push(3)
        max_stack.push(2)
        self.assertEqual(3, max_stack.max())

    def test_max__when_max_is_2_and_2_is_last_element__then_2_is_returned(self):
        max_stack: MaxStack = MaxStack()
        max_stack.push(1)
        max_stack.push(2)
        self.assertEqual(2, max_stack.max())
