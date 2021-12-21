### Candidates

import numpy as np


# https://www.cs.helsinki.fi/group/goa/mallinnus/3dtransf/3drot.html
def rot_z(v, steps=1):
    x, y, z = tuple(v)
    for _ in range(steps):
        x, y, z = (-y, x, z)

    # x' = x*cos q - y*sin q
    # y' = x*sin q + y*cos q
    # z' = z
    return np.array((x, y, z))


def rot_x(v, steps=1):
    x, y, z = tuple(v)
    for _ in range(steps):
        x, y, z = (x, -z, y)

    # y' = y*cos q - z*sin q
    # z' = y*sin q + z*cos q
    # x' = x
    return np.array((x, y, z))


def rot_y(v, steps=1):
    x, y, z = tuple(v)
    for _ in range(steps):
        x, y, z = (z, y, -x)

    # z' = z*cos q - x*sin q
    # x' = z*sin q + x*cos q
    # y' = y
    return np.array((x, y, z))
