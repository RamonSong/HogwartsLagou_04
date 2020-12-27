import pytest

from personalhomework_pytest02.core.calc import Calc


class TestCalc:
    def setup_class(self):
        self.calc = Calc()
    def setup(self):
        pass

    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, -1],
        [1, -1, "kong"],
        [1, 0, 0],
        [1, 0, "#"],
        [-1, 0, -1],
        ["#", 1, "##"],
        [0.1, 0.1, 0.01],
        [0.1, -0.01, 0.001],
        [-0.1, -0.1, 0.01],
        [0.1, "#", "0.#"],
        ['a', 'b', 'c'],
        [-0.1, 0.1, "##"],
        [0, 99, 99],
        [0, 1, 0],
        [0, -0.05, 0.05],
        [0, "#", "0*#"],
        ['#', '#', '##']
    ])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c


    @pytest.mark.parametrize('a, b, c', [
        [1, 1, 0.5],
        [2, 1, 2],
        [1, 0.5, 2],
        [0.5, 0.5, 1],
        [0.5, 0.5, -1],
        [-0.9, -0.03, 30],
        [-0.8, 0.4, 2],
        ["#", '-1', "#"],
        [10, 3, 3.33],
        ['a', 'b', 'c'],
        [-1, 0.05, 20],
        [5, -2, -2.5],
        ['#', '#', 1]
    ])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    @pytest.mark.parametrize('a,b', [
        [2, 0],
        [0.5, 0],
        [-1, 0],
        [0, 0],
        [0, 1],
        [0, -1],
        [0, 0.05],
        ["#", 0],
        [3.1415, 0],
        [0, "a"],
        [0, 3.45678],
        [0, -0.15]
    ])
    def test_div01(self, a, b):
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(a, b)


    def test_process01(self):
        a = self.calc.div(2,1)
        b = self.calc.mul(1,2)
        assert a == 2
        assert b == 2


    def test_process02(self):
        c = self.calc.mul(3,2)
        d = self.calc.div(2,3)
        assert c == 6
        assert d == 0.66






