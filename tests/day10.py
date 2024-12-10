import unittest

from main.day10 import part_one, part_two

class Day10Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 36)

    def test_part_two(self):
        self.assertEqual(part_two(input_source="examples"), 81)

if __name__ == "__main__":
    unittest.main()
