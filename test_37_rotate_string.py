from pathlib import Path
import sys
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent))
module = importlib.import_module("37_rotate_string")


def test_standard_rotation():
    assert module.rotate_string("abcdef", 2) == "efabcd"


def test_k_larger_than_length():
    assert module.rotate_string("abc", 5) == "bca"


def test_negative_k_rotation():
    assert module.rotate_string("abcdef", -1) == "bcdefa"


def test_empty_string():
    assert module.rotate_string("", 3) == ""
