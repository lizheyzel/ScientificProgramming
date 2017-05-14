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


def polar_to_cartesian(p):
    """
    Convert a point provided as an ordered 2-tuple representing the polar
    coordinates to the same point in cartesian coordinates.

      >>> p = polar_to_cartesian((5, 0.9272952180016122))
      >>> int(round(p[0]))
      3
      >>> int(round(p[1]))
      4
      >>> p2 = polar_to_cartesian((13, 1.17605207095135))
      >>> int(round(p2[0]))
      5
      >>> int(round(p2[1]))
      12
    """
    r, theta = p[0], p[1]

    return r * math.cos(theta), r * math.sin(theta)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
