""" Sample tests using pytest and hypothesis """
import hypothesis.strategies as st
from hypothesis import given
from app import flappy-py


def test_sample_method_add() -> None:
    """ testing for sample_method_add """
    sample_class = flappy-py.SampleClass()
    assert sample_class.sample_method_add(2, 4) == 6  # nosec


def test_sample_func_subtract() -> None:
    """ testing for sample_function_subtract """
    assert flappy-py.sample_func_subtract(4, 3) == 1  # nosec


@given(st.integers(), st.integers())
def test_hypothesis_test_of_calc(first_int: int, second_int: int) -> None:
    """ hypothesis test """
    sample_class = flappy-py.SampleClass()
    assert (  # nosec
        sample_class.sample_method_add(first_int, second_int) == first_int + second_int
    )
