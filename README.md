# Robot Movement Simulator

This project simulates the movement of multiple robots on a grid-based terrain. Each robot follows directional commands (e.g., N4, E3, S2, W1) to move within the grid. The robots will stop if they encounter a boundary or another robot at their destination. The system also includes unit tests to verify key functionalities like collision detection, boundary checks, and correct movement.

## Features

- **Multiple Robots**: You can create multiple robots, each with a unique ID.
- **Grid-based Movement**: Robots can move North, South, East, or West.
- **Collision Detection**: Robots will stop if they encounter another robot at their destination.
- **Boundary Checks**: Robots cannot move outside the grid.
- **Unit Testing**: Unit tests verify the functionality of the movement logic, boundary checks, and collision detection.

## Code Structure

- **Robot Class**: Manages each robot's ID, position, and movement logic.
- **Terrain Class**: Handles the grid, robot placement, and movement commands.
- **Unit Test (TestRobotMovement)**: Contains unit tests for initial position, movement, collision detection, and boundary checks.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/robot-movement-simulator.git
   cd robot-movement-simulator


Ensure that Python 3 is installed on your system. You can check by running:
bash
Copy code
python3 --version

Usage
Running the Simulation
To run the robot movement simulation, you can use the following Python code:

python
Copy code
terrain = Terrain(5, 5)
terrain.add_robot(1)
terrain.add_robot(2)

# Move robot 1 East by 3 steps
terrain.move_robot(1, 'E3')

# Move robot 2 South by 2 steps
terrain.move_robot(2, 'S2')

# Print current positions of robots
print(terrain.get_robot_position(1))  # Expected output: (0, 3)
print(terrain.get_robot_position(2))  # Expected output: (2, 0)

# Test invalid direction
terrain.move_robot(1, 'Z5')  # Invalid direction, no movement

Unit Tests
To run unit tests and check the core functionalities, use Python’s unittest framework. Run the following command in the terminal:

bash
Copy code
python -m unittest test_robot_movement.py

This will run the test cases for:

Initial positions of robots
Valid movements and boundary checks
Collision detection
Commands
N: Move North
S: Move South
E: Move East
W: Move West
Each command should be followed by the number of steps. For example:

N2: Move north by 2 steps.
E3: Move east by 3 steps.
Example
python
Copy code
# Initialize a 5x5 grid and add two robots
terrain = Terrain(5, 5)
terrain.add_robot(1)
terrain.add_robot(2)

# Move robots
terrain.move_robot(1, 'E3')   # Robot 1 moves East by 3 steps
terrain.move_robot(2, 'S2')   # Robot 2 moves South by 2 steps

# Check positions
print(terrain.get_robot_position(1))  # Expected output: (0, 3)
print(terrain.get_robot_position(2))  # Expected output: (2, 0)
Running the Tests
To run the tests for boundary checks, collisions, and movement validation, you can use:

python -m unittest test_robot_movement.py




### Steps to add this to your GitHub:

1. Create a `README.md` file in your project directory.
2. Paste the content above into the file.
3. Save the file.
4. Commit and push it to your GitHub repository using Git.

This `README.md` provides clear documentation of your project, including installation steps, usage, and t
