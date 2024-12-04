import unittest

from main.day04 import part_one, part_two, xmas_count

class Day04Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 18)

    def test_part_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
