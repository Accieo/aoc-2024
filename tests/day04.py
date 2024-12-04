import unittest

from main.day04 import part_one, part_two

class Day04Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 18)

    def test_part_two(self):
        self.assertEqual(part_two(input_source="examples"), 9)

if __name__ == "__main__":
    unittest.main()
