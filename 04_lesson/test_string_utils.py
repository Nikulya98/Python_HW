import pytest
from StringUtils import StringUtils


@pytest.mark.parametrize("input_text, expected_output", [
    ("skypro", "Skypro"),
    ("SkyPro", "SkyPro"),
    ("", ""),
    (" ", " ")
])
def test_capitalize(input_text, expected_output):
    utils = StringUtils()
    assert utils.capitilize(input_text) == expected_output


@pytest.mark.parametrize("input_text, expected_output", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("  ", ""),
    ("", "")
])
def test_trim(input_text, expected_output):
    utils = StringUtils()
    assert utils.trim(input_text) == expected_output


@pytest.mark.parametrize("input_text, delimiter, expected_output", [
    ("a,b,c", ",", ["a", "b", "c"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
    (None, ",", [])
])
def test_to_list(input_text, delimiter, expected_output):
    utils = StringUtils()
    assert utils.to_list(input_text, delimiter) == expected_output


@pytest.mark.parametrize("string, symbol, expected_output", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("", "S", False),
    (None, "S", False)
])
def test_contains(string, symbol, expected_output):
    utils = StringUtils()
    assert utils.contains(string, symbol) == expected_output


@pytest.mark.parametrize("string, symbol, expected_output", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("", "S", ""),
    (None, "S", "")
])
def test_delete_symbol(string, symbol, expected_output):
    utils = StringUtils()
    assert utils.delete_symbol(string, symbol) == expected_output


@pytest.mark.parametrize("string, symbol, expected_output", [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("", "S", False),
    (None, "S", False)
])
def test_starts_with(string, symbol, expected_output):
    utils = StringUtils()
    assert utils.starts_with(string, symbol) == expected_output


@pytest.mark.parametrize("string, symbol, expected_output", [
    ("SkyPro", "o", True),
    ("SkyPro", "y", False),
    ("", "S", False),
    (None, "S", False)
])
def test_ends_with(string, symbol, expected_output):
    utils = StringUtils()
    assert utils.ends_with(string, symbol) == expected_output


@pytest.mark.parametrize("string, expected_output", [
    ("", True),
    (" ", True),
    ("SkyPro", False),
    (None, True)
])
def test_is_empty(string, expected_output):
    utils = StringUtils()
    assert utils.is_empty(string) == expected_output


@pytest.mark.parametrize("lst, joiner, expected_output", [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    ([], ", ", ""),
    (None, ", ", "")
])
def test_list_to_string(lst, joiner, expected_output):
    utils = StringUtils()
    assert utils.list_to_string(lst, joiner) == expected_output


if __name__ == "__main__":
    pytest.main()
