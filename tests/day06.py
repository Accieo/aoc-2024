import unittest

from main.day06 import is_facing_obstacle, move_guard, part_one, part_two

class Day06Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 41)

    def test_part_two(self):
        pass

    # Obstacle detection tests
    def test_obs_up_detection(self):
        lab_map = [
            [".", ".", "#"],
            [".", ".", "^"],
            [".", ".", "."],
        ]
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map)
        self.assertEqual(rotate_dir, ">")
        self.assertEqual(facing_obstacle, True)

    def test_obs_down_detection(self):
        lab_map = [
            [".", ".", "."],
            [".", ".", "v"],
            [".", ".", "#"],
        ]
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map)
        self.assertEqual(rotate_dir, "<")
        self.assertEqual(facing_obstacle, True)

    def test_obs_left_detection(self):
        lab_map = [
            [".", ".", "."],
            ["#", "<", "."],
            [".", ".", "."],
        ]
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map)
        self.assertEqual(rotate_dir, "^")
        self.assertEqual(facing_obstacle, True)

    def test_obs_right_detection(self):
        lab_map = [
            [".", ".", "."],
            [".", ">", "#"],
            [".", ".", "."],
        ]
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map)
        self.assertEqual(rotate_dir, "v")
        self.assertEqual(facing_obstacle, True)

    def test_obs_nothingr_detection(self):
        lab_map = [
            [".", ".", "."],
            [".", ">", "."],
            [".", ".", "."],
        ]
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map)
        self.assertEqual(rotate_dir, ">")
        self.assertEqual(facing_obstacle, False)

    def test_obs_nwallfaceu_detection(self):
        lab_map = [
            [".", "^", "."],
            [".", ".", "."],
            [".", ".", "."],
        ]
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map)
        self.assertEqual(rotate_dir, "^")
        self.assertEqual(facing_obstacle, False)

    def test_obs_nwallfacer_detection(self):
        lab_map = [
            [".", ".", "."],
            [".", ".", ">"],
            [".", ".", "."],
        ]
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map)
        self.assertEqual(rotate_dir, ">")
        self.assertEqual(facing_obstacle, False)

    def test_obs_nwallfacel_detection(self):
        lab_map = [
            [".", ".", "."],
            ["<", ".", "."],
            [".", ".", "."],
        ]
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map)
        self.assertEqual(rotate_dir, "<")
        self.assertEqual(facing_obstacle, False)

    def test_obs_nwallfaced_detection(self):
        lab_map = [
            [".", ".", "."],
            [".", ".", "."],
            [".", "v", "."],
        ]
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map)
        self.assertEqual(rotate_dir, "v")
        self.assertEqual(facing_obstacle, False)

    # Movement tests
    def test_mv_up(self):
        lab_map_before = [
            [".", "#", "."],
            [".", ".", "."],
            [".", "^", "."],
        ]
        lab_map_after = [
            [".", "#", "."],
            [".", "^", "."],
            [".", ".", "."],
        ]
        walked, lab_map = move_guard(lab_map=lab_map_before)
        self.assertEqual(walked, [[2,1], [1,1]])
        self.assertEqual(lab_map, lab_map_after)

    def test_mv_down(self):
        lab_map_before = [
            [".", "v", "."],
            [".", ".", "."],
            [".", "#", "."],
        ]
        lab_map_after = [
            [".", ".", "."],
            [".", "v", "."],
            [".", "#", "."],
        ]
        walked, lab_map = move_guard(lab_map=lab_map_before)
        self.assertEqual(walked, [[0,1], [1,1]])
        self.assertEqual(lab_map, lab_map_after)

    def test_mv_right(self):
        lab_map_before = [
            [".", ".", "."],
            [">", ".", "#"],
            [".", ".", "."],
        ]
        lab_map_after = [
            [".", ".", "."],
            [".", ">", "#"],
            [".", ".", "."],
        ]
        walked, lab_map = move_guard(lab_map=lab_map_before)
        self.assertEqual(walked, [[1,0], [1,1]])
        self.assertEqual(lab_map, lab_map_after)

    def test_mv_left(self):
        lab_map_before = [
            [".", ".", "."],
            ["#", ".", "<"],
            [".", ".", "."],
        ]
        lab_map_after = [
            [".", ".", "."],
            ["#", "<", "."],
            [".", ".", "."],
        ]
        walked, lab_map = move_guard(lab_map=lab_map_before)
        self.assertEqual(walked, [[1,2], [1,1]])
        self.assertEqual(lab_map, lab_map_after)

if __name__ == "__main__":
    unittest.main()
