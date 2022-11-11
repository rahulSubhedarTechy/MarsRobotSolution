class RobotInstructions():
    def __init__(self, size, commands) -> None:
        self.size_info = size.split('x') # size_info store row size at 0 and column size at 1 index
        self.commands = commands # string
        self.current_cell_coordinates = [1, 1] # When the robot is not in the grid at all
        self.current_facing = 'North' # Always be North at the start
        self.direction_guide = {   # Guides for the direction and calculation of cell moved for the command
            'North': {'L': 'West', 'R': 'East', 'F': 'North', 'calculation': [0, 1]},
            'East': {'L': 'North', 'R': 'South', 'F': 'East', 'calculation': [1, 0]},
            'West': {'L': 'South', 'R': 'North', 'F': 'West', 'calculation': [-1, 0]},
            'South': {'L': 'East', 'R': 'West', 'F': 'South', 'calculation': [0, -1]}
        }

    def check_if_to_be_moved(self, command) -> bool:
        if command == 'F':
            return True
        return False

    def check_if_command_valid(self, coordintes, max_size) -> bool:
        if (coordintes[0] < int(max_size[0]) and coordintes[0] > -1) and (coordintes[1] < int(max_size[1]) and coordintes[1] > -1):
            return True
        return False

    def check_initial_conditions(self) -> bool:
        if self.current_cell_coordinates == [1, 1] and self.current_facing == 'North':
            return True
        return False

    # The function checks if the command is possible is yes take necessary actions
    # Params:
    # command - the cuurent command
    def is_command_possible(self, command):
        next_facing_direction = self.direction_guide[self.current_facing][command] # Get the resultant direction for the current command from 'direction_guide'
        calculation_to_perform = self.direction_guide[next_facing_direction]['calculation'] # Get the resultant coordinates for the current command from 'direction_guide'
        
        next_cell_coordinates = [sum(i) for i in zip(self.current_cell_coordinates, calculation_to_perform)] # Calculate resultant coordinates

        # Check if it is a boundary condition, if ignore command 
        if self.check_if_command_valid(next_cell_coordinates, self.size_info):
            self.current_facing = next_facing_direction # change direction if command valid

            # move if the command is 'F' and valid
            if self.check_if_to_be_moved(command):
                self.current_cell_coordinates = next_cell_coordinates 
                
    def process_commands(self) -> tuple:
        # Considering that commands with always be string and have R F L only, continued.

        for command in self.commands:
            self.is_command_possible(command)

        return self.current_cell_coordinates, self.current_facing
                
if __name__ == "__main__":
    grid_size = str(input())
    commands = str(input())
    robo_instance = RobotInstructions(grid_size, commands)
    if robo_instance.check_initial_conditions():
        coordinates, direction = robo_instance.process_commands()
        print(str(coordinates[0]) +","+ str(coordinates[1]) +","+ direction)