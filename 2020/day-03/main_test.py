from main import coordinates

assert list(coordinates(10, 1, 1))[1] == (1, 1)
assert list(coordinates(10, 3, 1))[1] == (3, 1)
assert list(coordinates(10, 7, 1))[1] == (7, 1)
assert list(coordinates(10, 1, 2))[1] == (1, 2)
