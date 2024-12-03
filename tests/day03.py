import unittest

from main.day03 import part_one, part_two

class Day03Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 161)

    def test_part_two(self):
        self.assertEqual(part_two(input_source="examples"), 48)

if __name__ == "__main__":
    unittest.main()
