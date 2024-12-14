import unittest

from main.day00 import part_one, part_two

class Day00Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 0)

    def test_part_two(self):
        self.assertEqual(part_two(input_source="examples"), 0)

if __name__ == "__main__":
    unittest.main()
