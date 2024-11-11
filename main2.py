import unittest

class Robot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.position = (0, 0)

    def move(self, direction, steps, grid_size, occupied_positions):
        x, y = self.position
        for _ in range(steps):
            new_position = x, y
            if direction == 'N':
                new_position = (x - 1, y)
            elif direction == 'S':
                new_position = (x + 1, y)
            elif direction == 'E':
                new_position = (x, y + 1)
            elif direction == 'W':
                new_position = (x, y - 1)
            else:
                print(f"invalid direction: {direction}")
                return

            # Check boundaries and collision
            if new_position[0] < 0 or new_position[0] >= grid_size[0] or \
                    new_position[1] < 0 or new_position[1] >= grid_size[1] or \
                    new_position in occupied_positions:
                break  # Stop moving if there's a boundary or collision
            x, y = new_position
        self.position = (x, y)
        print(f"Robot {self.robot_id} goes {steps} steps to {direction}")

    def get_position(self):
        return self.position


class Terrain:
    def __init__(self, rows, cols):
        self.grid_size = (rows, cols)
        self.robots = {}

    def add_robot(self, robot_id):
        if robot_id in self.robots:
            raise ValueError(f"Robot with ID {robot_id} already exists.")
        self.robots[robot_id] = Robot(robot_id)

    def move_robot(self, robot_id, command):
        if robot_id not in self.robots:
            print(f"Robot ID {robot_id} doesn't exist")
            return
        if len(command) != 2 or not command[1].isdigit():
            print("Invalid command format. Expected format is <Direction><Steps>.")
            return

        robot = self.robots[robot_id]
        direction = command[0].upper()
        steps = int(command[1])

        # Get all occupied positions of other robots
        occupied_positions = {r.get_position() for rid, r in self.robots.items() if rid != robot_id}

        # Move the robot
        robot.move(direction, steps, self.grid_size, occupied_positions)

    def get_robot_position(self, robot_id):
        if robot_id not in self.robots:
            print(f"Robot ID {robot_id} doesn't exist")
            return None
        return self.robots[robot_id].get_position()




class TestRobotMovement(unittest.TestCase):# unit testing started
    def setUp(self):
        self.terrain = Terrain(5, 5)
        self.terrain.add_robot(1)
        self.terrain.add_robot(2)

    def test_initial_position(self):
        self.assertEqual(self.terrain.get_robot_position(1), (0, 0))
        self.assertEqual(self.terrain.get_robot_position(2), (0, 0))

    def test_move_robot(self):
        self.terrain.move_robot(1, 'N2')
        self.assertEqual(self.terrain.get_robot_position(1), (0, 0))  # Cannot move north from start
        self.terrain.move_robot(1, 'E3')
        self.assertEqual(self.terrain.get_robot_position(1), (0, 3))

        self.terrain.move_robot(2, 'S2')
        self.assertEqual(self.terrain.get_robot_position(2), (2, 0))

    def test_collision_detection(self):
        self.terrain.move_robot(1, 'E3')
        self.terrain.move_robot(2, 'E3')  # Should stop before colliding with robot 1
        self.assertEqual(self.terrain.get_robot_position(2), (0, 2))

    def test_boundary_check(self):
        self.terrain.move_robot(1, 'S5')
        self.assertEqual(self.terrain.get_robot_position(1), (4, 0))  # Boundary stops at last row




if __name__ == "__main__":
    unittest.main()

terrain = Terrain(5, 5)
terrain.add_robot(1)
terrain.add_robot(2)

terrain.move_robot(1, 'E3')
terrain.move_robot(2, 'S2')
terrain.move_robot(1, 'Z5')  # Invalid direction

print(terrain.get_robot_position(1))  # Outputs: (0, 3)
print(terrain.get_robot_position(2))  # Outputs: (2, 0)
