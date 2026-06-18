import pytest
from app.split_integer import split_integer


@pytest.mark.parametrize("value, number_of_parts, expected", [
    (8, 1, [8]),
    (6, 2, [3, 3]),
    (17, 4, [4, 4, 4, 5]),
    (32, 6, [5, 5, 5, 5, 6, 6]),
    (1, 1, [1]),
    (10, 10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
    (5, 5, [1, 1, 1, 1, 1]),
    (7, 3, [2, 2, 3]),
])
def test_split_integer_returns_correct_result(
        value: int,
        number_of_parts: int,
        expected: list) -> None:
    assert split_integer(value, number_of_parts) == expected


@pytest.mark.parametrize("value, number_of_parts", [
    (8, 1), (6, 2), (17, 4), (32, 6), (7, 3), (10, 10),
])
def test_split_integer_returns_correct_length(
        value: int,
        number_of_parts: int) -> None:
    assert len(split_integer(value, number_of_parts)) == number_of_parts


@pytest.mark.parametrize("value, number_of_parts", [
    (8, 1), (6, 2), (17, 4), (32, 6), (7, 3), (10, 10),
])
def test_split_integer_sum_equals_value(
        value: int,
        number_of_parts: int) -> None:
    assert sum(split_integer(value, number_of_parts)) == value


@pytest.mark.parametrize("value, number_of_parts", [
    (8, 1), (6, 2), (17, 4), (32, 6), (7, 3), (10, 10),
])
def test_split_integer_max_min_difference_le_1(
        value: int,
        number_of_parts: int) -> None:
    result = split_integer(value, number_of_parts)
    assert max(result) - min(result) <= 1


@pytest.mark.parametrize("value, number_of_parts", [
    (8, 1), (6, 2), (17, 4), (32, 6), (7, 3), (10, 10),
])
def test_split_integer_is_sorted_ascending(
        value: int,
        number_of_parts: int) -> None:
    result = split_integer(value, number_of_parts)
    assert result == sorted(result)


@pytest.mark.parametrize("value, number_of_parts", [
    (11, 3), (10, 10), (9, 3),
])
def test_split_integer_equal_parts_when_divisible(
        value: int,
        number_of_parts: int) -> None:
    assert len(set(split_integer(value, number_of_parts))) == 1
