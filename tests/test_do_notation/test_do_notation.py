# -*- coding: utf-8 -*-

from dry_monads.do_notation import do_notation
from dry_monads.either import Either, Failure, Success


@do_notation
def _example1(number: int) -> Either[int, str]:
    first = Success(1).unwrap()
    second = Success(number).unwrap() if number else Failure('E').unwrap()
    return Success(first + second)


@do_notation
def _example2(number: int) -> Success[int]:
    first: int = Success(1).unwrap()
    return Success(first + Failure(number).unwrap())


def test_do_notation_success():
    """Ensures that do notation works well for Success."""
    assert _example1(5) == Success(6)


def test_do_notation_failure():
    """Ensures that do notation works well for Failure."""
    assert _example1(0) == Failure('E')
    assert _example2(0) == Failure(0)