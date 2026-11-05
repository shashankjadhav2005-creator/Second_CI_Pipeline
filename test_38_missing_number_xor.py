from pathlib import Path
import sys
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent))
module = importlib.import_module("38_missing_number_xor")


def test_missing_number_in_zero_to_n():
    assert module.find_missing_number([3, 0, 1]) == 2


def test_missing_last_element():
    assert module.find_missing_number([0, 1]) == 2


def test_larger_range():
    assert module.find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_range_with_zero_and_one():
    assert module.find_missing_number([0]) == 1
