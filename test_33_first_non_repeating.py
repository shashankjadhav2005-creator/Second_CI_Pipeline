from pathlib import Path
import sys
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parent))
module = importlib.import_module("33_first_non_repeating")


def test_standard_case():
    assert module.first_non_repeating("swiss") == "w"


def test_first_character_is_unique():
    assert module.first_non_repeating("python") == "p"


def test_all_characters_repeated():
    assert module.first_non_repeating("aabbcc") is None


def test_empty_string():
    assert module.first_non_repeating("") is None
