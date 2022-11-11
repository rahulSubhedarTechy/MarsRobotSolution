import unittest
from robot_handling import RobotInstructions

class Test_Robot(unittest.TestCase):

    def setUp(self):
        self.robo_inst = RobotInstructions(size='5x5', commands='FFRFLFLF')

    def test_check_initial_conditions(self):
        self.assertEqual(self.robo_inst.check_initial_conditions(), True)

    def test_if_to_be_moved(self):
        self.assertEqual(self.robo_inst.check_if_to_be_moved('F'), True)

    def test_check_if_command_valid(self):
        self.assertEqual(self.robo_inst.check_if_command_valid([-1, -1], [5, 5]), False)

    def test_final_result(self):
        self.assertEqual(self.robo_inst.process_commands(), ([1, 4], 'West'))

if __name__ == "__main__":
    unittest.main()