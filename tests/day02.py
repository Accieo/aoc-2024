import unittest

from main.day02 import part_one, part_two

class Day02Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 2)

    def test_part_two(self):
        self.assertEqual(part_two(input_source="examples"), 4)

if __name__ == "__main__":
    unittest.main()
