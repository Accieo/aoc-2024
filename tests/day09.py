import unittest

from main.day09 import part_one, part_two

class Day09Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 1928)

    def test_part_two(self):
        self.assertEqual(part_two(input_source="examples"), 2858)

if __name__ == "__main__":
    unittest.main()
