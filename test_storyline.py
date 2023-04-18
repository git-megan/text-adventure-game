"""
    Megan Brown
    CS 5001 - Final Project
    Tests for storyline.py
"""
import storyline
import unittest


class StorylineTest(unittest.TestCase):
    def test_clean_string(self):
        """
        Test if correctly removes spaces and lowers string
        """
        str_test_1 = "continue "
        str_test_2 = "    fast"
        str_test_3 = "WAlk"
        self.assertEqual(storyline.clean_string(str_test_1), "continue")
        self.assertEqual(storyline.clean_string(str_test_2), "fast")
        self.assertEqual(storyline.clean_string(str_test_3), "walk")



    def test_get_choice(self):
        """
        Tests if get_choice returns correct index
        Test requires a manual tester to choose 'continue' as the choice
        Tester may also test if program reprompts when choosing an option that's not listed
        """
        print("Manual testing: choose 'continue' when prompted")
        outcome_1 = storyline.get_choice(["continue"])
        outcome_2 = storyline.get_choice(["run", "jump", "continue"], "moving")
        outcome_3 = storyline.get_choice(["continue", "leave", "ask"])
        self.assertEqual(outcome_1, 0)
        self.assertEqual(outcome_2, 2)
        self.assertEqual(outcome_3, 0)


def main():
    # runs unit tests with more verbosity
    unittest.main(verbosity = 3)


if __name__ == "__main__":
    main()