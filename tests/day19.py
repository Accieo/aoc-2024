import unittest

from main.day19 import part_one, part_two

class Day19Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 6)

if __name__ == "__main__":
    unittest.main()
