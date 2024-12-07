import unittest

from main.day07 import part_one, part_two

class Day07Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 3749)

    def test_part_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
