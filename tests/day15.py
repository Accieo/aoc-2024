import unittest

from main.day15 import part_one, part_two

class Day15Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 10092)

    def test_part_two(self):
        pass

if __name__ == "__main__":
    unittest.main()
