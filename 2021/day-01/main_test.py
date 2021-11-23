import input
import main


def test_day_01_input():
    assert main.find_product_day1(input.test_input, 2020) == 514579


def test_day_02_input():
    assert main.find_product_day2(input.test_input, 2020) == 241861950
