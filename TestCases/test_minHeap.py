
# test_min_heap.py

import unittest
from ProgrammeFiles.minHeap import MinHeap

class TestMinHeap(unittest.TestCase):

    def setUp(self):
        self.heap = MinHeap()
        for val in [50, 20, 30, 10, 60]:
            self.heap.insert(val)

    def test_insert_and_peek(self):
        self.assertEqual(self.heap.peek(), 10)

    def test_extract_min(self):
        self.assertEqual(self.heap.extract_min(), 10)
        self.assertEqual(self.heap.peek(), 20)
        self.assertEqual(self.heap.extract_min(), 20)
        self.assertEqual(self.heap.peek(), 30)

    def test_min_order(self):
        sorted_vals = []
        while self.heap.peek() is not None:
            sorted_vals.append(self.heap.extract_min())
        self.assertEqual(sorted_vals, sorted(sorted_vals))  # should be ascending order

    def test_empty_heap(self):
        empty_heap = MinHeap()
        self.assertIsNone(empty_heap.peek())
        self.assertIsNone(empty_heap.extract_min())

    def test_single_element(self):
        h = MinHeap()
        h.insert(99)
        self.assertEqual(h.peek(), 99)
        self.assertEqual(h.extract_min(), 99)
        self.assertIsNone(h.peek())

if __name__ == "__main__":
    unittest.main()
