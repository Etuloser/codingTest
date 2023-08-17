import pytest

from q1 import maximize_u


class TestQ1:
    def test_case1(self):
        arr = [1, 2, 4, 6, 8, 12]
        got = maximize_u(arr)
        want = 32
        assert got == want

    def test_case2(self):
        arr = [1, 2, 4, 6]
        got = maximize_u(arr)
        want = 12
        assert got == want
