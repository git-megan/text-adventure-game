"""
    Megan Brown
    CS 5001 - Final Project
    Tests for dice.py
"""
from dice import Dice
import unittest


class DiceTest(unittest.TestCase):
    def test_init(self):
        """
        Test if dice initializes correctly
        """
        d6_default = Dice("d6")
        self.assertEqual(d6_default.name, "d6")
        self.assertEqual(d6_default.sides, 6)
        d20 = Dice("d20", 20)
        self.assertEqual(d20.name, "d20")
        self.assertEqual(d20.sides, 20)


    def test_roll(self):
        """
        Tests if 10 rolls on a d6 are in range (1-6)
        """
        d6_default = Dice("d6")
        # manually check if print function works
        print(d6_default)
        for i in range(10):
            test_roll = d6_default.roll()
            self.assertIn(test_roll, range(1, 7))
            print(f"{d6_default.name} rolled a", str(test_roll))


    def test_health_roll(self):
        """
        Tests if the health_roll works
        Checks if 10 rolls of a d6 are in range (1-6)

        Note: Manually check printed strings
        """
        d6_default = Dice("d6")
        for i in range(10):
            health_roll_outcome = d6_default.health_roll("if you can jump over the gap")
            self.assertIn(health_roll_outcome, range(1, 7))
            print(f"{d6_default.name} rolled a", str(health_roll_outcome))


def main():
    # runs unit tests with more verbosity
    unittest.main(verbosity = 3)


if __name__ == "__main__":
    main()