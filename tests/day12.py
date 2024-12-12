import unittest

from main.day12 import part_one, part_two

class Day12Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 1930)

    def test_part_two(self):
        self.assertEqual(part_two(input_source="examples"), 1206)

if __name__ == "__main__":
    unittest.main()
