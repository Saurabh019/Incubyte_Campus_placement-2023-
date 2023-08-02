# Create a Coordinate class to represent the x, y, z coordinates
class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Define the Direction enum to represent the spacecraft's directions
class Direction:
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
    UP = 5
    DOWN = 6

# Define the Chandrayaan3 class to handle spacecraft control
class Chandrayaan3:
    def __init__(self, x, y, z, initial_direction):
        self.current_position = Coordinate(x, y, z)
        self.current_direction = initial_direction

    def move_forward(self):
        if self.current_direction == Direction.NORTH:
            self.current_position.y += 1
        elif self.current_direction == Direction.SOUTH:
            self.current_position.y -= 1
        elif self.current_direction == Direction.EAST:
            self.current_position.x += 1
        elif self.current_direction == Direction.WEST:
            self.current_position.x -= 1
        elif self.current_direction == Direction.UP:
            self.current_position.z += 1
        elif self.current_direction == Direction.DOWN:
            self.current_position.z -= 1

    def move_backward(self):
        if self.current_direction == Direction.NORTH:
            self.current_position.y -= 1
        elif self.current_direction == Direction.SOUTH:
            self.current_position.y += 1
        elif self.current_direction == Direction.EAST:
            self.current_position.x -= 1
        elif self.current_direction == Direction.WEST:
            self.current_position.x += 1
        elif self.current_direction == Direction.UP:
            self.current_position.z -= 1
        elif self.current_direction == Direction.DOWN:
            self.current_position.z += 1

    def rotate_left(self):
        if self.current_direction == Direction.NORTH:
            self.current_direction = Direction.WEST
        elif self.current_direction == Direction.WEST:
            self.current_direction = Direction.SOUTH
        elif self.current_direction == Direction.SOUTH:
            self.current_direction = Direction.EAST
        elif self.current_direction == Direction.EAST:
            self.current_direction = Direction.NORTH

    def rotate_right(self):
        if self.current_direction == Direction.NORTH:
            self.current_direction = Direction.EAST
        elif self.current_direction == Direction.EAST:
            self.current_direction = Direction.SOUTH
        elif self.current_direction == Direction.SOUTH:
            self.current_direction = Direction.WEST
        elif self.current_direction == Direction.WEST:
            self.current_direction = Direction.NORTH

    def turn_up(self):
        if self.current_direction == Direction.NORTH:
            self.current_direction = Direction.UP
        elif self.current_direction == Direction.UP:
            self.current_direction = Direction.SOUTH
        elif self.current_direction == Direction.SOUTH:
            self.current_direction = Direction.DOWN
        elif self.current_direction == Direction.DOWN:
            self.current_direction = Direction.NORTH

    def turn_down(self):
        if self.current_direction == Direction.NORTH:
            self.current_direction = Direction.DOWN
        elif self.current_direction == Direction.DOWN:
            self.current_direction = Direction.SOUTH
        elif self.current_direction == Direction.SOUTH:
            self.current_direction = Direction.UP
        elif self.current_direction == Direction.UP:
            self.current_direction = Direction.NORTH

    def process_commands(self, commands):
        for command in commands:
            if command == 'f':
                self.move_forward()
            elif command == 'b':
                self.move_backward()
            elif command == 'r':
                self.rotate_right()
            elif command == 'l':
                self.rotate_left()
            elif command == 'u':
                self.turn_up()
            elif command == 'd':
                self.turn_down()

    def get_current_position(self):
        return self.current_position

    def get_current_direction(self):
        return self.current_direction
