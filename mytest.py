import pytest

# content of test_sample.py
def inc(x):
    return x + 1


# it must start with test before pytest can see it..
def test_answer():
    assert inc(3) == 5