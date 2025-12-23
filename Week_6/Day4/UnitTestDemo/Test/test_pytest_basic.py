import pytest

from src.Calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_calculator(calculator):
    #calculator = Calculator()
    result = calculator.add(1,2)
    assert result == 3

def test_if_even(calculator):
    #calculator = Calculator()
    #result = calculator.is_even(2)
    assert calculator.is_even(2) is True
    assert not calculator.is_even(5)


def test_divide_by_zero(calculator):
    #calculator = Calculator()
    with pytest.raises(ZeroDivisionError) as context:
        calculator.divide(3,0)
    assert "zero" in str(context.value)


@pytest.mark.parametrize(
    "num1, num2, expected_sum",
    [
        (1,2,3),
        (0,0,0),
        (-1,5,4)
    ]
)

def test_calc_add_with_parameters(calculator, num1, num2, expected_sum):
    result = calculator.add(num1, num2)
    assert result == expected_sum

    @pytest.mark.skip(reason="This feature is under development")
    def test_new_feature():
        assert False