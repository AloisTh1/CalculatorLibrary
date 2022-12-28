import calculator


class TestCalculator:
    def test_addition(self):
        assert calculator.add(x1=2, x2=2) == 4

    def test_substraction(self):
        assert calculator.substract(x1=2, x2=2) == 0
