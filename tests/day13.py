import unittest

from main.day13 import part_one

class Day13Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 480)

if __name__ == "__main__":
    unittest.main()
