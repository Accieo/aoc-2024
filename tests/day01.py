import unittest

from main.day01 import part_one, part_two

class Day01Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 11)

    def test_part_two(self):
        self.assertEqual(part_two(input_source="examples"), 31)

if __name__ == "__main__":
    unittest.main()
