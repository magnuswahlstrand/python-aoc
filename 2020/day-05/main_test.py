from main import parse_boarding_card

assert parse_boarding_card("FBFBBFFRLR") == (44, 5, 357)
assert parse_boarding_card("BFFFBBFRRR") == (70, 7, 567)
assert parse_boarding_card("FFFBBBFRRR") == (14, 7, 119)
assert parse_boarding_card("BBFFBBFRLL") == (102, 4, 820)
