import math


def cartesian_to_polar(p):
    """
    Convert a point provided as an ordered 2-tuple representing the cartesian
    coordinates to the same point in polar coordinates.

      >>> cartesian_to_polar((3, 4))
      (5.0, 0.9272952180016122)
      >>> cartesian_to_polar((5, 12))
      (13.0, 1.176005207095135)
    """
    r = (p[0] ** 2 + p[1] ** 2) ** 0.5
    theta = math.atan2(p[1], p[0])

    return (r, theta)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
