
from isNullOrEmpty.is_null_or_empty import is_null_or_empty


def test_with_none():
    """Tests if the function returns True when the parameter is None."""
    assert is_null_or_empty(None) == True, "Failed for None"

def test_with_empty_string():
    """Tests if the function returns True for an empty string."""
    assert is_null_or_empty("") == True, "Failed for empty string"

def test_with_empty_list():
    """Tests if the function returns True for an empty list."""
    assert is_null_or_empty([]) == True, "Failed for empty list"

def test_with_empty_dict():
    """Tests if the function returns True for an empty dictionary."""
    assert is_null_or_empty({}) == True, "Failed for empty dictionary"

def test_with_non_empty_string():
    """Tests if the function returns False for a non-empty string."""
    assert is_null_or_empty("Some text") == False, "Failed for non-empty string"

def test_with_non_empty_list():
    """Tests if the function returns False for a non-empty list."""
    assert is_null_or_empty([1, 2, 3]) == False, "Failed for non-empty list"

def test_with_non_empty_dict():
    """Tests if the function returns False for a non-empty dictionary."""
    assert is_null_or_empty({"key": "value"}) == False, "Failed for non-empty dictionary"

def test_with_zero():
    """Tests if the function returns False for the number 0, which is not considered 'empty' by the function's context."""
    assert is_null_or_empty(0) == False, "Failed for 0"

def test_with_false():
    """Tests if the function returns False for the boolean False, which is not considered 'empty' by the function's context."""
    assert is_null_or_empty(False) == False, "Failed for False"
