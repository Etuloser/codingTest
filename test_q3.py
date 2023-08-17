import pytest

from q3 import process_commands


class TestQ3:
    def test_push(self):
        commands = [["push", 5]]
        stack = process_commands(commands)
        assert stack[-1] == 5

    def test_pop(self):
        commands = [["push", 5], ["pop"]]
        stack = process_commands(commands)
        assert len(stack) == 0

    def test_inc(self):
        commands = [["push", 5], ["inc", 1, 5]]
        stack = process_commands(commands)
        assert stack == [10]
