import unittest

from main.day06 import is_facing_obstacle, get_pos_and_dir, move_guard, part_one, part_two

class Day06Tests(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(input_source="examples"), 41)

    def test_part_two(self):
        self.assertEqual(part_two(input_source="examples"), 6)

    # Obstacle detection tests
    def test_obs_up_detection(self):
        lab_map = [
            [".", ".", "#"],
            [".", ".", "^"],
            [".", ".", "."],
        ]
        (y, x), current_direction = get_pos_and_dir(lab_map)
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map, y=y, x=x, current_direction=current_direction)
        self.assertEqual(rotate_dir, ">")
        self.assertEqual(facing_obstacle, True)

    def test_obs_down_detection(self):
        lab_map = [
            [".", ".", "."],
            [".", ".", "v"],
            [".", ".", "#"],
        ]
        (y, x), current_direction = get_pos_and_dir(lab_map)
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map, y=y, x=x, current_direction=current_direction)
        self.assertEqual(rotate_dir, "<")
        self.assertEqual(facing_obstacle, True)

    def test_obs_left_detection(self):
        lab_map = [
            [".", ".", "."],
            ["#", "<", "."],
            [".", ".", "."],
        ]
        (y, x), current_direction = get_pos_and_dir(lab_map)
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map, y=y, x=x, current_direction=current_direction)
        self.assertEqual(rotate_dir, "^")
        self.assertEqual(facing_obstacle, True)

    def test_obs_right_detection(self):
        lab_map = [
            [".", ".", "."],
            [".", ">", "#"],
            [".", ".", "."],
        ]
        (y, x), current_direction = get_pos_and_dir(lab_map)
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map, y=y, x=x, current_direction=current_direction)
        self.assertEqual(rotate_dir, "v")
        self.assertEqual(facing_obstacle, True)

    def test_obs_nothingr_detection(self):
        lab_map = [
            [".", ".", "."],
            [".", ">", "."],
            [".", ".", "."],
        ]
        (y, x), current_direction = get_pos_and_dir(lab_map)
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map, y=y, x=x, current_direction=current_direction)
        self.assertEqual(rotate_dir, ">")
        self.assertEqual(facing_obstacle, False)

    def test_obs_nwallfaceu_detection(self):
        lab_map = [
            [".", "^", "."],
            [".", ".", "."],
            [".", ".", "."],
        ]
        (y, x), current_direction = get_pos_and_dir(lab_map)
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map, y=y, x=x, current_direction=current_direction)
        self.assertEqual(rotate_dir, "^")
        self.assertEqual(facing_obstacle, False)

    def test_obs_nwallfacer_detection(self):
        lab_map = [
            [".", ".", "."],
            [".", ".", ">"],
            [".", ".", "."],
        ]
        (y, x), current_direction = get_pos_and_dir(lab_map)
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map, y=y, x=x, current_direction=current_direction)
        self.assertEqual(rotate_dir, ">")
        self.assertEqual(facing_obstacle, False)

    def test_obs_nwallfacel_detection(self):
        lab_map = [
            [".", ".", "."],
            ["<", ".", "."],
            [".", ".", "."],
        ]
        (y, x), current_direction = get_pos_and_dir(lab_map)
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map, y=y, x=x, current_direction=current_direction)
        self.assertEqual(rotate_dir, "<")
        self.assertEqual(facing_obstacle, False)

    def test_obs_nwallfaced_detection(self):
        lab_map = [
            [".", ".", "."],
            [".", ".", "."],
            [".", "v", "."],
        ]
        (y, x), current_direction = get_pos_and_dir(lab_map)
        rotate_dir, facing_obstacle = is_facing_obstacle(lab_map=lab_map, y=y, x=x, current_direction=current_direction)
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
        (y, x), current_direction = get_pos_and_dir(lab_map_before)
        walked, lab_map = move_guard(lab_map=lab_map_before, start_y=y, start_x=x, current_direction=current_direction)
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
        (y, x), current_direction = get_pos_and_dir(lab_map_before)
        walked, lab_map = move_guard(lab_map=lab_map_before, start_y=y, start_x=x, current_direction=current_direction)
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
        (y, x), current_direction = get_pos_and_dir(lab_map_before)
        walked, lab_map = move_guard(lab_map=lab_map_before, start_y=y, start_x=x, current_direction=current_direction)
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
        (y, x), current_direction = get_pos_and_dir(lab_map_before)
        walked, lab_map = move_guard(lab_map=lab_map_before, start_y=y, start_x=x, current_direction=current_direction)
        self.assertEqual(walked, [[1,2], [1,1]])
        self.assertEqual(lab_map, lab_map_after)

if __name__ == "__main__":
    unittest.main()
