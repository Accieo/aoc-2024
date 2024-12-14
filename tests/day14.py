import unittest

from main.day14 import part_one

class Day14Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 12)

if __name__ == "__main__":
    unittest.main()
