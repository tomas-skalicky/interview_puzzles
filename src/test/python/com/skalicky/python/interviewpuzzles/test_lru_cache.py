from unittest import TestCase

from src.main.python.com.skalicky.python.interviewpuzzles.lru_cache import LruCache


class TestLruCache(TestCase):
    def test_lru_cache__when_cache_is_empty__then_get_returns_none(self):
        cache: LruCache = LruCache(1)
        self.assertIsNone(cache.get('foo'))
        self.assertEqual(
            'capacity=1, linked list starting with head=(None), linked list starting with tail=(None)', str(cache))

    def test_lru_cache__when_searched_key_is_head__then_head_value_is_returned(self):
        cache: LruCache = LruCache(1)
        cache.put('foo', 'F')
        self.assertEqual('F', cache.get('foo'))
        self.assertEqual(
            'capacity=1, linked list starting with head=(foo -> None), linked list starting with tail=(foo -> None)',
            str(cache))

    def test_lru_cache__when_cache_is_full_and_usage_is_same__then_oldest_entry_by_insertion_time_is_evicted(self):
        cache: LruCache = LruCache(1)
        cache.put('foo', 'F')
        cache.put('bar', 'B')
        self.assertIsNone(cache.get('foo'))
        self.assertEqual('B', cache.get('bar'))
        self.assertEqual(
            'capacity=1, linked list starting with head=(bar -> None), linked list starting with tail=(bar -> None)',
            str(cache))

    def test_lru_cache__when_cache_is_full_and_usage_is_not_same__then_least_used_entry_is_evicted(self):
        cache: LruCache = LruCache(2)
        cache.put('foo', 'F')
        cache.put('bar', 'B')
        self.assertEqual(
            'capacity=2, linked list starting with head=(bar -> foo -> None), linked list starting with tail=(foo -> None)',
            str(cache))

        cache.get('foo')
        self.assertEqual(
            'capacity=2, linked list starting with head=(foo -> bar -> None), linked list starting with tail=(bar -> None)',
            str(cache))

        cache.put('baz', 'Z')
        self.assertIsNone(cache.get('bar'))
        self.assertEqual('F', cache.get('foo'))
        self.assertEqual('Z', cache.get('baz'))
        self.assertEqual(
            'capacity=2, linked list starting with head=(baz -> foo -> None), linked list starting with tail=(foo -> None)',
            str(cache))
