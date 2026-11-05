from pathlib import Path
import sys
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent))
module = importlib.import_module("40_gcd")


def test_standard_numbers():
    assert module.gcd(48, 18) == 6


def test_coprime_numbers():
    assert module.gcd(17, 13) == 1


def test_with_zero():
    assert module.gcd(0, 5) == 5
    assert module.gcd(5, 0) == 5


def test_same_numbers():
    assert module.gcd(12, 12) == 12


def test_negative_numbers():
    assert module.gcd(-48, 18) == 6
    assert module.gcd(48, -18) == 6
