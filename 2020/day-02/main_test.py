import main


def test_parse_passports():
    input = "1-2 a: foo\n" \
            "3-4 b: bar"
    expected = [
        ("1", "2", "a", "foo"),
        ("3", "4", "b", "bar")
    ]
    assert main.parse_passports(input) == expected


def test_day_01_input():
    assert main.count_valid_passports('input_text.txt') == 2
