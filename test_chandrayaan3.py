import unittest
from chandrayaan3 import Chandrayaan3, Coordinate, Direction

class TestChandrayaan3(unittest.TestCase):

    def test_move_forward(self):
        spacecraft = Chandrayaan3(0, 0, 0, Direction.NORTH)
        spacecraft.move_forward()
        self.assertEqual(spacecraft.get_current_position(), Coordinate(0, 1, 0))

    def test_move_backward(self):
        spacecraft = Chandrayaan3(0, 0, 0, Direction.NORTH)
        spacecraft.move_backward()
        self.assertEqual(spacecraft.get_current_position(), Coordinate(0, -1, 0))

    def test_rotate_left(self):
        spacecraft = Chandrayaan3(0, 0, 0, Direction.NORTH)
        spacecraft.rotate_left()
        self.assertEqual(spacecraft.get_current_direction(), Direction.WEST)

    def test_rotate_right(self):
        spacecraft = Chandrayaan3(0, 0, 0, Direction.NORTH)
        spacecraft.rotate_right()
        self.assertEqual(spacecraft.get_current_direction(), Direction.EAST)

    def test_turn_up(self):
        spacecraft = Chandrayaan3(0, 0, 0, Direction.NORTH)
        spacecraft.turn_up()
        self.assertEqual(spacecraft.get_current_direction(), Direction.UP)

    def test_turn_down(self):
        spacecraft = Chandrayaan3(0, 0, 0, Direction.NORTH)
        spacecraft.turn_down()
        self.assertEqual(spacecraft.get_current_direction(), Direction.DOWN)

    def test_example_commands(self):
        spacecraft = Chandrayaan3(0, 0, 0, Direction.NORTH)
        spacecraft.process_commands(['f', 'r', 'u', 'b', 'l'])
        self.assertEqual(spacecraft.get_current_position(), Coordinate(0, 1, -1))
        self.assertEqual(spacecraft.get_current_direction(), Direction.WEST)

# Run the test cases

unittest.main()
