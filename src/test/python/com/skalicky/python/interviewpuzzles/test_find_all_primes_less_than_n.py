from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.find_all_primes_less_than_n import find_all_primes_less_than_n


class Test(TestCase):
    def test_find_all_primes_less_than_n__when_n_is_not_prime__then_n_is_not_in_result(self):
        self.assertListEqual([2, 3, 5, 7, 11, 13], find_all_primes_less_than_n(14))

    def test_find_all_primes_less_than_n__when_n_is_prime__then_n_is_not_in_result(self):
        self.assertListEqual([2, 3, 5, 7], find_all_primes_less_than_n(11))

    def test_find_all_primes_less_than_n__when_n_equals_2__then_no_prime(self):
        self.assertListEqual([], find_all_primes_less_than_n(2))
