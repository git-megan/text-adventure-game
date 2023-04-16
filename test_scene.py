"""
Megan Brown
CS 5001 - Final Project
Tests for scene.py
"""
from scene import Scene
from typing import Tuple


def test_outcomes(good: Tuple[str, int], bad: Tuple[str, int], sample_scene: Scene) -> int:
    """
    Tests if the object's outcomes dictionary matches intended dict
    
    Args:
        good Tuple[str, int]: the original good outcome story and damage
        bad Tuple[str, int]: the original bad outcome story and damage
        sample_scene (Scene): the scene created using sample_dict
    Returns:
        int: 0 if passed test, 1+ if failed test
    """
    fails = 0
    if good != sample_scene.good_outcome:
        print("Failed test_outcomes: Tuples for good outcome didn't match")
        fails += 1
    if bad != sample_scene.bad_outcome:
        print("Failed test_outcomes: Tuples for bad outcome didn't match")
        fails += 1
    return fails


def test_play(sample_scene: Scene) -> int:
    """
    Tests if the scene plays and returns a tuple of the result

    Args:
        sample_scene (Scene): the scene object
    Returns:
        int: 0 if passed test, 1+ if failed
    """
    fails = 0

    # playing the scene should result in a tuple
    player, damage = sample_scene.play()

    if player != sample_scene.player:
        print("Failed test_play: Did not return player correctly")
        print(f"Actual player: {player}")
        fails += 1
    
    # health damage comes from outcomes tuple at index 1
    if not ((damage == sample_scene.good_outcome[1]) or (damage == sample_scene.bad_outcome[1])):
        print("Failed test_play: Incorrect damage score")
        print(f"Actual damage: {damage}")
        fails += 1
    return fails


def main() -> None:
    """
    Runs all unit tests for scene
    """
    fail_count = 0

    # create variables for scene object
    impact = "if you out-run the swarm"
    good_outcome = ("You out run the swarm, but get stung once.", 2)
    bad_outcome = ("You trip and get attacked by the swarm", 20)

    # create scene object
    test_scene = Scene("test_scene", impact, "You", 4, good_outcome, bad_outcome)

    # check if printing the object info works
    print(test_scene)

    # run tests
    fail_count += test_outcomes(good_outcome, bad_outcome, test_scene)
    fail_count += test_play(test_scene)

    print(f"Fail count: {fail_count}")


if __name__ == "__main__":
    main()

