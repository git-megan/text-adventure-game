"""
Megan Brown
CS 5001 - Final Project
Tests for game.py

Requires some manual testing - read the printed instructions when testing
"""
import game
from scene import Scene


def print_instructions(case: str, notes: str = "n/a"):
    """
    Prints special instructions for manual testing
    Args:
        case (str): What the tester should be testing
        notes (str): Any spceial instructions
    """
    print(f"Manual testing: Check for {case}")
    print(f"Special instructions: {notes}")


def get_tester_score() -> int:
    """
    Gets a test score
    Used when doing manual testing
    Args:
        None
    Returns:
        int: 0 if correct, 1 if failed test
    """
    score = input("\nType '0' if correct, '1' if failed test: ")
    while (score.strip() != '0') and (score.strip() != '1'):
        score = input("Type '0' if correct, '1' if error: ")
    return int(score)


def test_get_title() -> int:
    """
    Tests that get_title returns the correct title
    Args:
        None
    Returns:
        int: Number of tests failed
    """
    print("\nTesting get_title...")
    fails = 0

    title = "\nEscape of the Bees"
    subtitle = "\nA text adventure game by Megan Brown"
    expected = title + subtitle
    actual = game.get_title()
    if (actual != expected):
        print(f"Failed get_title: \nActual: {actual} \n Expected: {expected}")
        fails += 1
    return fails


def test_menu() -> int:
    """
    Tests if menu returns correct tuple
    Should return cleaned_string, actual_string
    Args:
        None
    Returns:
        int: Number of tests failed
    """
    print("\nTesting menu...")
    fails = 0
    entry_1 = " play"
    entry_2 = "exit "
    entry_3 = "Pause"
    # test for preceeding space
    print_instructions("spaces in entries", f"Enter '{entry_1}' when prompted")
    if (game.menu() != ("play", " play")):
        print(f"Failed test with '{entry_1}' as input")
        fails += 1
    # test for trailing space
    print_instructions("spaces in entries", f"Enter '{entry_2}' when prompted")
    if (game.menu() != ("exit", "exit ")):
        print(f"Failed test with '{entry_2}' as input")
        fails += 1
    # test for correct cases
    print_instructions("spaces in entries", f"Enter '{entry_3}' when prompted")
    if (game.menu() != ("pause", "Pause")):
        print(f"Failed test with '{entry_3}' as input")
        fails += 1
    return fails


def test_get_status() -> int:
    """
    Manual testing for get_status
    Status should print as non-negative health scores from dictionary
    Args:
        None
    Returns:
        int: test case fail count
    """
    print("\nTesting 'get_status'...")
    fails = 0
    health_dict_1 = {"Robin": 70, "Martin": 80, "You": 50}
    print_instructions("correct formatting", f"Uses {health_dict_1} for data")
    print(game.get_status(health_dict_1))
    fails += get_tester_score()

    # Test case for negative health score
    health_dict_2 = {"Robin": 70, "Martin": 0, "You": -5}
    print_instructions("non-negative health percentages", f"Uses {health_dict_2} for data")
    print(game.get_status(health_dict_2))
    fails += get_tester_score()
    return fails


def test_update_scores() -> int:
    """
    Tests if function correctly updates player's health scores
    Args:
        None
    Returns:
        int: test case fail count
    """
    print("\nTesting 'update_scores'...")
    fails = 0
    test_dict_1 = {"Robin": 100, "Martin": 100, "You":100}
    expected_1 = {"Robin": 100, "Martin": 100, "You":100, "Miles": 85}
    test_dict_2 = {"Robin": 100, "Martin": 100, "You":100}
    expected_2 = {"Robin": 80, "Martin": 80, "You":80}
    test_dict_3 = {"Robin": 100, "Martin": 100, "You":100}
    expected_3 = {"Robin": 100, "Martin": 100, "You":90}
    # test if given an update for a player not accounted for
    if (game.update_scores(test_dict_1, "Miles", 15) != expected_1):
        print("Failed test: incorrect scores when updating a player not in original dict")
        fails += 1
    # test if given an update for all players
    if (game.update_scores(test_dict_2, "everyone", 20) != expected_2):
        print("Failed test: Did not correctly update 20 damage for 'everyone'")
        fails += 1
    # test is given an update for 'You'
    if (game.update_scores(test_dict_3, "You", 10) != expected_3):
        print("Failed test: Did not correctly update 10 damage from 'You'")
        fails += 1
    return fails


def test_play_narrative() -> int:
    """
    Test if the correct narrative plays
    Requires manual testing
    Args:
        None
    Returns:
        int: Number of tests play_narrative failed
    """
    print("\nTesting 'play_narrative'...")
    fails = 0

    # Test case for part_3_scene
    name_2 = "part_3"
    impact_2 = "if your group out ran the bees"
    player_2 = "everyone"
    cut_off_2 = 3
    good_outcome_2 = ("Everyone made it safely inside the stranger's house.", 0)
    bad_outcome_2 = ("The bees swarm and sting you as your run, but you make it inside the house.", 20)

    # create scene object
    part_3_scene = Scene(name_2, impact_2, player_2, cut_off_2, good_outcome_2, bad_outcome_2)

    print_instructions("correct narrative for part 3", "Uses part_3_scene for arg")
    game.play_narrative(part_3_scene)
    fails += get_tester_score()
    return fails


def test_run_part() -> int:
    """
    Tests that run_part returns correct health dictionary and menu command tuple
    Args:
        None
    Returns:
        int: Failed test count
    """
    print("\nTesting run_part...")
    fails = 0
    print_instructions("n/a", "Type 'play' when game menu appears, then play")
    # Test case uses part_3_scene
    name_2 = "part_3"
    impact_2 = "if your group out ran the bees"
    player_2 = "everyone"
    cut_off_2 = 3
    good_outcome_2 = ("Everyone made it safely inside the stranger's house.", 0)
    bad_outcome_2 = ("The bees swarm and sting you as your run, but you make it inside the house.", 20)
    # create scene object and health dictionaries
    part_3_scene = Scene(name_2, impact_2, player_2, cut_off_2, good_outcome_2, bad_outcome_2)
    health_start = {"Robin": 100, "Martin": 100, "You": 100}
    health_bad_outcome = {"Robin": 80, "Martin": 80, "You": 80}

    health_outcome, command = game.run_part(part_3_scene, health_start)
    if (health_outcome != health_start) and (health_outcome != health_bad_outcome):
        print("Failed test: Incorrect health dictionary returned")
        fails += 1
    if (command != "play"):
        print("Failed test: command returned is not 'play'")
        fails += 1
    return fails


def test_create_scenes() -> int:
    """
    Test if function creates the correct scenes for the game
    Args:
        None
    Returns:
        int: Number of tests failed
    """
    print("\nTesting 'create_scenes'...")
    fails = 0
    intro, part_2, part_3 = game.create_scenes()
    if intro.name != "intro":
        print(f"Failed name test case: expected 'intro', actual '{intro.name}'")
        fails += 1
    if part_2.impact != "if any bees have followed you":
        print(f"Failed impact test case: actual for part_2 - '{part_2.impact}'")
        fails += 1
    if part_2.player != "You":
        print(f"Failed player test case: expected 'You' for part_2, actual '{part_2.player}'")
        fails += 1
    expected_good_outcome = ("Everyone made it safely inside the stranger's house.", 0)
    if part_3.good_outcome != expected_good_outcome:
        print(f"Failed good outcome: For part 3, actual - '{part_3.good_outcome}'")
        fails += 1
    return fails


def test_main() -> int:
    """
    Tests that the game plays in correct order
    Requires manual testing
    Args:
        None
    Returns:
        int: Number of times main failed test cases
    """
    print("\nTesting 'main'...")
    fails = 0
    print_instructions("correct order of game", "Also ensure resolution does not play before game ending")
    game.main()
    fails += get_tester_score()
    return fails


def main() -> None:
    """
    Runs all test cases for game.py
    Args:
        None
    Returns:
        None
    """
    fail_count = 0
    print("Running all tests for game.py...")
    fail_count += test_get_title()
    fail_count += test_menu()
    fail_count += test_get_status()
    fail_count += test_update_scores()
    fail_count += test_play_narrative()
    fail_count += test_run_part()
    fail_count += test_create_scenes()
    fail_count += test_main()
    print(f"\nFail count for game.py: {fail_count}")


if __name__ == "__main__":
    main()