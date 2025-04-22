# test_max_heap.py

import unittest
from ProgrammeFiles.maxHeap import MaxHeap

class TestMaxHeap(unittest.TestCase):

    def setUp(self):
        self.heap = MaxHeap()
        for val in [10, 40, 30, 60, 90, 70]:
            self.heap.insert(val)

    def test_insert_and_peek(self):
        self.assertEqual(self.heap.peek(), 90)

    def test_extract_max(self):
        max1 = self.heap.extract_max()
        self.assertEqual(max1, 90)
        self.assertEqual(self.heap.peek(), 70)

        max2 = self.heap.extract_max()
        self.assertEqual(max2, 70)
        self.assertEqual(self.heap.peek(), 60)

    def test_heap_order(self):
        sorted_vals = []
        while self.heap.peek() is not None:
            sorted_vals.append(self.heap.extract_max())
        self.assertEqual(sorted_vals, sorted(sorted_vals, reverse=True))

    def test_empty_extract(self):
        empty_heap = MaxHeap()
        self.assertIsNone(empty_heap.extract_max())
        self.assertIsNone(empty_heap.peek())

    def test_single_element(self):
        h = MaxHeap()
        h.insert(42)
        self.assertEqual(h.peek(), 42)
        self.assertEqual(h.extract_max(), 42)
        self.assertIsNone(h.peek())


if __name__ == "__main__":
    unittest.main()
