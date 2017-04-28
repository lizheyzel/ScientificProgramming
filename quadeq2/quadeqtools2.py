def str2point(point_str):
    """
    Convert a string with two comma seperated numbers into a tuple of
    two numbers.

      >>> type(str2point('1, 2'))
      <class 'tuple'>
      >>> str2point('1, 2')
      (1, 2)
    """
    x, y = point_str.split(', ')
    return (int(x), int(y))


def read_point_set_from_file(fname, line_num):
    """
    Read in a set of 3 points at line_num from the fname file and convert
    them to a list of 2-tuples.

      >>> read_point_set_from_file('test_point_sets.dat', 1)
      [(-3, -65), (4, -16), (-10, -408)]
    """
    f = open(fname, 'r')
    point_str =  f.readlines()[line_num - 1][:-1]
    points = point_str.split('), ')
    points = [point[1:] for point in points]
    points[-1] = points[-1][:-1]
    points = [str2point(point) for point in points]

    return points



if __name__ == '__main__':
    import doctest
    doctest.testmod()
