import pytest

from q2 import count_matches


class TestQ2:
    def test_case1(self):
        teamA = [1, 2, 3]
        teamB = [2, 4]
        got = count_matches(teamA, teamB)
        want = [2, 3]
        assert got == want

    def test_case2(self):
        teamA = [1, 1, 2]
        teamB = [2, 2, 2]
        got = count_matches(teamA, teamB)
        want = [3, 3, 3]
        assert got == want

    def test_case3(self):
        teamA = [3, 4, 5]
        teamB = [1, 2]
        got = count_matches(teamA, teamB)
        want = [0, 0]
        assert got == want
