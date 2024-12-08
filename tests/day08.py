import unittest

from main.day08 import part_one, part_two

class Day08Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 14)

    def test_part_two(self):
        self.assertEqual(part_two(input_source="examples"), 34)

if __name__ == "__main__":
    unittest.main()
