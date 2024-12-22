import unittest

from main.day22 import part_one

class Day22Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 37327623)

if __name__ == "__main__":
    unittest.main()
