
# Test the Stack Implementation using python

import unittest
from ProgrammeFiles.stack import Stack

class stack_test(unittest.TestCase) :

    def setUp(self):
        # It Runs at the Begining of every Execution
        self.stack = Stack()
    
    def test_push_pop(self):
        self.stack.add_element(20)
        self.stack.add_element(30)
        self.assertEqual(self.stack.remove_element(),30)
        self.assertEqual(self.stack.remove_element(),20)

    def test_peek(self):
        self.stack.add_element(100)
        self.assertEqual(self.stack.top_element(), 100)
        self.assertEqual(self.stack._size(), 1)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.add_element(1)
        self.assertFalse(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack._size(), 0)
        self.stack.add_element(1)
        self.stack.add_element(2)
        self.assertEqual(self.stack._size(), 2)

    def test_pop_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.remove_element()

    def test_peek_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.top_element()

if __name__ == '__main__':
    unittest.main()


