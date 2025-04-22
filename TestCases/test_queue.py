
import unittest

from ProgrammeFiles.queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_is_empty_on_new_queue(self):
        self.assertTrue(self.queue.is_empty())

    def test_size_on_new_queue(self):
        self.assertEqual(self.queue.size(), 0)

    def test_add_element(self):
        self.queue.add_element(10)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 1)

    def test_display_after_adding_elements(self):
        self.queue.add_element(10)
        self.queue.add_element(20)
        self.queue.add_element(30)
        self.assertEqual(self.queue.display(), [10, 20, 30])

    def test_remove_element(self):
        self.queue.add_element(10)
        self.queue.add_element(20)
        removed_element = self.queue.remove_element()
        self.assertEqual(removed_element, 10)
        self.assertEqual(self.queue.size(), 1)

    def test_remove_element_until_empty(self):
        self.queue.add_element(10)
        self.queue.remove_element()
        self.assertTrue(self.queue.is_empty())
        self.assertIsNone(self.queue.remove_element())  # Should return None

    def test_size_after_removals(self):
        self.queue.add_element(10)
        self.queue.add_element(20)
        self.queue.remove_element()  # Remove 10
        self.assertEqual(self.queue.size(), 1)  # Should be 1 after one removal

    def test_display_after_removals(self):
        self.queue.add_element(10)
        self.queue.add_element(20)
        self.queue.remove_element()  # Remove 10
        self.assertEqual(self.queue.display(), [20])  # Should only have 20 left


if __name__ == '__main__':
    unittest.main()