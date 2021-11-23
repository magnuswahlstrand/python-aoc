import input


def find_product_day1(entries, wanted_sum):
    for i, e in enumerate(entries):
        for f in entries[i + 1:]:
            if e + f == wanted_sum:
                return e * f
    raise ValueError(f"no sum pairs found matching {wanted_sum}")


def find_product_day2(entries, wanted_sum):
    for i, e in enumerate(entries):
        for f in entries[i + 1:]:
            for g in entries[i + 1:]:
                if f == g:
                    continue

                if e + f + g == wanted_sum:
                    return e * f * g
    raise ValueError(f"no sum of values found matching {wanted_sum}")


if __name__ == "__main__":
    day_1 = find_product_day1(input.input, 2020)
    day_2 = find_product_day2(input.input, 2020)
    print(f"result for day 1 is: {day_1}")
    print(f"result for day 2 is: {day_2}")
