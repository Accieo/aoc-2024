import unittest

from main.day11 import part_one

class Day11Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 55312)

if __name__ == "__main__":
    unittest.main()
