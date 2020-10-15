from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.swap_bits_in_integer import swap_bits


class Test(TestCase):
    def test_swap_bits__when_0b10101010101010101010101010101010__then_1431655765(self):
        self.assertEqual(1431655765, swap_bits(0b10101010101010101010101010101010))

    def test_swap_bits__when_2863311530__then_1431655765(self):
        self.assertEqual(1431655765, swap_bits(2863311530))

    def test_swap_bits__when_2__then_1(self):
        self.assertEqual(1, swap_bits(2))

    def test_swap_bits__when_3__then_3(self):
        self.assertEqual(3, swap_bits(3))

    def test_swap_bits__when_5__then_3(self):
        self.assertEqual(3, swap_bits(5))
