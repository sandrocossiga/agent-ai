"""Tests for the planner stub using unittest.

The tests verify that the planner splits inputs into tasks and
handles empty inputs gracefully.
"""
import unittest

from src.agent.core import Agent


class TestPlanner(unittest.TestCase):
    def test_planner_splits_words(self) -> None:
        agent = Agent()
        tasks = agent.plan("Do the dishes")
        self.assertEqual(tasks, ["Task: Do", "Task: the", "Task: dishes"])

    def test_planner_handles_empty_input(self) -> None:
        agent = Agent()
        tasks = agent.plan("")
        self.assertEqual(tasks, [])


if __name__ == "__main__":
    unittest.main()
