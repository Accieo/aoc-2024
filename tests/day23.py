import unittest

from main.day23 import part_one

class Day23Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 7)

if __name__ == "__main__":
    unittest.main()
